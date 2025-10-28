from .forms import login_form,signup_form,UnBookedForm,edit_My_Profile_form,search_forms
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from .models import Reservation,Person,RealEstate,Town,City,MyReservations,Favourits
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import RealEstate, Comment, Rating, Favourits, Reservation
from django.shortcuts import render, redirect, get_object_or_404
from .models import RealEstate, Reservation
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from datetime import timedelta
import json
from django.db.models import Avg


def home(request):
    return render(request,'home.html')
# views.py


def help(request):
    return render(request,'help.html')

@csrf_exempt
@login_required(login_url='home:login')
def resProfile(request, slug):
    real_estate = get_object_or_404(RealEstate, slug=slug)
    person = get_object_or_404(Person, user=request.user)

    # Check if the property is a favorite of the user
    is_favorite = Favourits.objects.filter(person=person, realestate=real_estate).exists()

    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            action = data.get('action')

            if action == 'reserve_dates':
                # Handle reservation submission
                start_date_str = data.get('start_date')
                end_date_str = data.get('end_date')

                start_date = parse_date(start_date_str)
                end_date = parse_date(end_date_str)

                if start_date and end_date and start_date <= end_date:
                    # Check for overlapping approved reservations
                    overlapping_reservations = Reservation.objects.filter(
                        real_estate=real_estate,
                        status='approved',
                        start_date__lte=end_date,
                        end_date__gte=start_date
                    )

                    if overlapping_reservations.exists():
                        return JsonResponse({'status': 'error', 'message': 'تم حجز هذه التواريخ بالفعل.'})

                    # Calculate total price
                    days_reserved = (end_date - start_date).days + 1
                    total_price = days_reserved * real_estate.price

                    # Create a new reservation with 'pending' status
                    reservation = Reservation.objects.create(
                        user=request.user,
                        real_estate=real_estate,
                        start_date=start_date,
                        end_date=end_date,
                        total_price=total_price,
                        status='pending'  # Default status is 'pending'
                    )

                    return JsonResponse({
                        'status': 'success',
                        'message': 'تم إنشاء الحجز بنجاح.',
                        'total_price': total_price,
                        'warning': 'ان عدم المصداقية قد تؤدي الى الملاحقة القانونية'
                    })
                else:
                    return JsonResponse({'status': 'error', 'message': 'نطاق التواريخ غير صالح.'})

            elif action == 'toggle_favorite':
                # Handle toggling favorite status
                if is_favorite:
                    # Remove from favorites
                    Favourits.objects.filter(person=person, realestate=real_estate).delete()
                    is_favorite = False
                else:
                    # Add to favorites
                    Favourits.objects.create(person=person, realestate=real_estate)
                    is_favorite = True

                return JsonResponse({'is_favorite': is_favorite})

        else:
            # Handle form submissions (comments and ratings)
            if 'comment' in request.POST:
                # Handle comment submission
                comment_text = request.POST.get('comment_text')
                if comment_text:
                    Comment.objects.create(
                        user=request.user,
                        real_estate=real_estate,
                        text=comment_text
                    )
                    # Optionally redirect or add a success message here

            elif 'rating_submit' in request.POST:
                # Handle rating submission
                rating_value = request.POST.get('rating')
                if rating_value:
                    rating_value = int(rating_value)
                    # Update or create the user's rating for this property
                    Rating.objects.update_or_create(
                        user=request.user,
                        real_estate=real_estate,
                        defaults={'rating': rating_value}
                    )
                    # Recalculate the average rating
                    average_rating = Rating.objects.filter(real_estate=real_estate).aggregate(Avg('rating'))['rating__avg']
                    real_estate.average_rating = average_rating
                    real_estate.save()

    # Fetch existing approved reservations for the property
    reservations = real_estate.reservations.filter(status='approved')

    # Prepare reserved dates to send to the template
    reserved_dates = []
    for reservation in reservations:
        current_date = reservation.start_date
        while current_date <= reservation.end_date:
            reserved_dates.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)

    # Fetch comments for the property
    comments = real_estate.comments.all()

    # Calculate average rating for the property
    ratings = Rating.objects.filter(real_estate=real_estate)
    if ratings.exists():
        average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
        real_estate.average_rating = average_rating
        real_estate.save()
    else:
        average_rating = None

    # Compute full_stars and half_stars based on average_rating
    if average_rating:
        full_stars = int(average_rating)
        decimal_part = average_rating - full_stars
        half_stars = 1 if 0.25 <= decimal_part <= 0.75 else 0
        if decimal_part > 0.75:
            full_stars += 1  # Round up if the decimal part is greater than 0.75
            half_stars = 0
        empty_stars = 5 - full_stars - half_stars
    else:
        full_stars = 0
        half_stars = 0
        empty_stars = 5

    # Pass ranges to the template for looping
    context = {
        'real_estate': real_estate,
        'reserved_dates': json.dumps(reserved_dates),
        'is_favorite': is_favorite,
        'comments': comments,
        'average_rating': average_rating,
        'full_stars': range(full_stars),
        'half_stars': range(half_stars),
        'empty_stars': range(empty_stars),
    }

    return render(request, 'resProfile.html', context)

@login_required(login_url='home:login')
def editMyProfile(request):
    if request.method == 'POST':
        form = edit_My_Profile_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            old_password = form.cleaned_data['old_password']
            password = form.cleaned_data['password']
            conferm_password = form.cleaned_data['conferm_password']
            phone_num = form.cleaned_data['phone_num']
            print("her  ",phone_num)
            if password == conferm_password and check_password(old_password, request.user.password):
                user = request.user
                user.username = username
                user.set_password(password)  # Use set_password to hash the password
                person = user.person
                person.phone_num = phone_num
                user.save()
                person.save()
                print("done")
                # Re-authenticate the user to update the session with the new password
                update_session_auth_hash(request, user)

                return redirect('home:myprofile')
    else:
            user = request.user
            person = user.person
            initial_data = { 'username': user.username, 'phone_num': person.phone_num, }
            form = edit_My_Profile_form(initial=initial_data)
    return render(request, 'editMyProfile.html', {'form': form})


@login_required(login_url='home:login')
def myprofile(request):
    person=request.user.person

    real_estate = RealEstate.objects.all().filter(person=person)
    case='1'
    filter = request.GET.get('filter', 'عقاراتي')

    if filter == 'عقاراتي':
        real_estate = RealEstate.objects.all().filter(person=person)
        case = '1'
        print("33333333333333333  ",real_estate)
    elif filter == 'المفضلة':
        real_estate = Favourits.objects.all().filter(person=person)
        case = '2'
        print('asfafghfgdh')
        print("22222222222222  ", Favourits.objects.all())

    elif filter == 'حجوزاتي':
        real_estate =MyReservations.objects.all().filter(person=person)
        case = '2'
        print("1111111111  ",real_estate)

    return render(request,'myprofile.html',
                  {'person':person ,'real_estate':real_estate,'case':case })


def gallery(request):
    # Initialize the form with towns data
    towns = {}
    cities = City.objects.all()
    for city in cities:
        towns[city.name] = [town.name for town in city.town_set.all()]

    form = search_forms(request.GET or None, towns=towns)

    realEstates = RealEstate.objects.all()
    print(1)
    print(realEstates)
    if request.method == 'GET':
      print(3)
      if form.is_valid():


        # Filter based on form data
        city = form.cleaned_data.get('city')
        aqar_type = form.cleaned_data.get('Aqar')
        madena = form.cleaned_data.get('Madena')
        alser = form.cleaned_data.get('Alser')

        if city:
            realEstates = realEstates.filter(address__name=city)
        if aqar_type:
            realEstates = realEstates.filter(type=aqar_type)
        if madena:
            realEstates = realEstates.filter(town__name=madena)
        if alser:
            realEstates = realEstates.filter(price__lte=float(alser))
        print(2)
        print(realEstates)
        return render(request, 'gallery.html', {
        'form': form,
        'realEstates': realEstates,
        'towns': towns,
        })
    filter = request.GET.get('filter', 'all')

    if filter == 'all':
                realEstates = RealEstate.objects.all()
    elif filter == 'شقة':
                realEstates = RealEstate.objects.filter(type='شقة')
    elif filter == 'مزارع':
                realEstates = RealEstate.objects.filter(type='مزرعة')
    elif filter == 'فيلا':
                realEstates = RealEstate.objects.filter(type='فيلا')
    elif filter == 'popular':
                # Assuming you have a 'popular' field or a way to filter popular real estates
                realEstates = RealEstate.objects.filter(popular=True)
    else:
                realEstates = RealEstate.objects.all()

    return render(request, 'gallery.html', {'realEstates': realEstates, 'filter': filter, 'towns': towns, 'form': form})

    #


def signup(request):
    case='0'
    if request.method=='POST':

        form = signup_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            conferm_password = form.cleaned_data['conferm_password']
            city = form.cleaned_data['city']
            phone_num = form.cleaned_data['phone_num']
            us = form.cleaned_data['us']
            birth = form.cleaned_data['birth']
            user=User.objects.filter(username=username).count()
            person=Person.objects.filter(phone_num=phone_num).count()
            if user == 1:
               case='1'
               print(case)
               form = signup_form()
               return render(request, 'signup.html', {'form': form, 'case': case})
            if person >= 1:

               case='2'
               print(case)

               form = signup_form()
               return render(request, 'signup.html', {'form': form, 'case': case})
            if phone_num[0] == '0' and phone_num[1]=='9' and  len(phone_num) ==10:
              if password == conferm_password:
                # Create new user
                user = User.objects.create_user(username=username, password=password)
                # Create associated Person instance
                person = Person.objects.create(
                    user=user,
                    city=city,
                    phone_num=phone_num,
                    us=us,
                    birth=birth
                )
                user.save()
                person.save()

                # Authenticate and log in the user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home:main')
            else:
                case = '3'
                form = signup_form()
                print(case)

                return render(request, 'signup.html', {'form': form, 'case': case})
        else: print(7)

    form = signup_form()
    print(request.method)

    return render(request, 'signup.html', {'form': form , 'case':case})


def login(request):
    form = login_form()
    if request.method=='POST':
            form =login_form(request.POST)
            if form.is_valid():

               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               user = authenticate(request, username=username, password=password)
               if user is not None:
                    #if user is not empty
                    auth_login(request,user)
                    return redirect('home:main')
                    #go to the link that have usename=accounts then the page whose name=doctorlist
    form = login_form()
    return render(request,'login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('home:login')


@login_required(login_url='home:login')
def newres(request):
    form=UnBookedForm()
    if request.method=='POST':
        form = UnBookedForm(request.POST)
        if form.is_valid():
            newrealestate = form.save(commit=False)
            person = request.user.person
            newrealestate.name=person.name
            newrealestate.phone_num=person.phone_num
            newrealestate.save()
            return redirect('home:main')
    return render(request,'newRealEstate.html',{'form':form})