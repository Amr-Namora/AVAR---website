from django.db.models import CharField, CASCADE, PROTECT
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models
from django.core.exceptions import ValidationError


class NewRealEstate(models.Model):
    types = (
        ('مزرعة', 'مزرعة'),
        ('فيلا', 'فيلا'),
        ('شقة', 'شقة'),

    )
    address_choices = (
        ('خارج سوريا', 'خارج سوريا'),
        ('ادلب', 'ادلب'),
        ('دمشق', 'دمشق'),
        ('حلب', 'حلب'),
        ('ريف دمشق', 'ريف دمشق'),
        ('حماه', 'حماه'),
        ('حمص', 'حمص'),
        ('درعا', 'درعا'),
        ('القنيطرة', 'القنيطرة'),
        ('السويداء', 'السويداء'),
        ('دير الزور', 'دير الزور'),
        ('القامشلي', 'القامشلي'),
        ('الحسكة', 'الحسكة'),
        ('اللاذقية', 'اللاذقية'),
        ('طرطوس', 'طرطوس'),
    )
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='اسمك')
    phone_num = CharField(max_length=20, blank=True, null=True, verbose_name='رقمك')
    address = models.CharField(max_length=30, blank=True, null=True, choices=address_choices, verbose_name='المحافظة')
    address_detail = models.CharField(max_length=30, blank=True, null=True, verbose_name='المدينة او البلدة')
    type=models.CharField(max_length=30,blank=True,null=True,choices=types,verbose_name='نوع العقار')
    notes=models.CharField(max_length=500,blank=True,null=True,verbose_name='ملاحظات')


class Person(models.Model):
    un_booked=models.ForeignKey(NewRealEstate,blank=True,null=True,on_delete=PROTECT,verbose_name='طلبات لنشر عقار')
    user=models.OneToOneField(User,verbose_name='user',on_delete=CASCADE)
    name=models.CharField(max_length=20,blank=True,null=True,verbose_name='اسمك')
    phone_num=models.CharField(max_length=20,unique=True,blank=True,null=True,verbose_name='رقمك')
    us=models.CharField(max_length=20,blank=True,null=True,verbose_name='من اين سمعت عنا ؟')
    city=models.CharField(max_length=20,blank=True,null=True,verbose_name='محافظتك')
    birth=models.IntegerField(blank=True,null=True,verbose_name='عمرك')
    def __str__(self):
       return self.user.username



class RealEstate_Images(models.Model):
    image=models.ImageField(upload_to='photos/%y/%m/%d',blank=True,null=True,verbose_name='الصورة')


class City(models.Model):
    name=models.CharField(max_length=40,blank=True,null=True)
    def __str__(self):
        return self.name

class Town(models.Model):
    city=models.ForeignKey(City,on_delete=PROTECT,blank=True,null=True)
    name=models.CharField(max_length=40,blank=True,null=True)
    def __str__(self):
        return self.name


class RealEstate(models.Model):
    types = (
        ('مزرعة','مزرعة'),
        ('فيلا','فيلا'),
        ('شقة','شقة'),
    )
    periods = (
        ('بالليلة','بالليلة'),
        ('بالشهر','بالشهر'),
    )

    person = models.ForeignKey(Person, verbose_name='صاحب العقار', on_delete=models.CASCADE)
    type = models.CharField(max_length=30, blank=True, null=True, choices=types, verbose_name='نوع العقار')
    address = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True, verbose_name='المحافظة')
    town = models.ForeignKey(Town, on_delete=models.PROTECT, blank=True, null=True, verbose_name='المدينة او البلدة')
    address_detail2 = models.TextField(max_length=30, blank=True, null=True, verbose_name='العنوان بالتفصيل (اسم الحارة والشارع)')
    price = models.IntegerField(blank=True, null=True, verbose_name='السعر')
    main_image = models.ImageField(upload_to='photos/%y/%m/%d', default='photos/25/01/10/Prépare_tes_vacances.jpg', verbose_name='الصورة')
    Images = models.ForeignKey(RealEstate_Images, on_delete=models.PROTECT, blank=True, null=True, verbose_name='صور العقار')
    time = models.CharField(max_length=30, blank=True, null=True, choices=periods, verbose_name='اقل مدة زمنية لحجز العقار')
    slug = models.SlugField(unique=True, blank=True, null=True)
    average_rating = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            super(RealEstate, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.person.user.username}-{self.id}")
        super(RealEstate, self).save(*args, **kwargs)

    def __str__(self):
        return self.person.user.username


class Favourits(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name='الزبون', related_name='favourites')
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE,verbose_name='العقار', related_name='favourites_list')
    def __str__(self):
        return self.person.user.username


class MyReservations(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name='صاحب العقار', related_name='reservations')
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE,verbose_name='العقار', related_name='reservation_list')
    def __str__(self):
        return self.person.name

class Comment(models.Model):
        real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, related_name='comments')
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return self.text

class Rating(models.Model):
        real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, related_name='ratings')
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
        created_at = models.DateTimeField(auto_now_add=True)


# models.py

# models.py



class Reservation(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    real_estate = models.ForeignKey('RealEstate', on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Check for overlapping reservations
        overlapping = Reservation.objects.filter(
            real_estate=self.real_estate,
            status__in=['pending', 'approved'],
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(id=self.id)

        if overlapping.exists():
            raise ValidationError('The selected dates overlap with an existing reservation.')

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        # Calculate total_price before saving
        delta = self.end_date - self.start_date
        days_reserved = delta.days + 1
        if days_reserved <= 0:
            raise ValidationError('End date must be after start date.')
        self.total_price = days_reserved * self.real_estate.price
        super(Reservation, self).save(*args, **kwargs)

    def __str__(self):
        return f"Reservation {self.id} by {self.user.username}"
