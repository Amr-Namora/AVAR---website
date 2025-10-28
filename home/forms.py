from django import forms
from .models import NewRealEstate
from .models import Comment, Rating


class login_form(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'id': 'username',
            'name': 'username',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'اسم المستخدم'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'كلمة المرور'
        })
    )

class signup_form(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'id': 'username',
            'name': 'username',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'الاسم',
            'verbose_name':'الاسم'
        })
    )
    password = forms.CharField(
        label='',

        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'كلمة المرور'
        })
    )
    conferm_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'id': 'conferm_password',
            'name': 'conferm_password',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'تاكيد كلمة المرور'
        })
    )
    phone_num = forms.CharField(
        label='',

        widget=forms.TextInput(attrs={
            'id': 'phone_num',
            'name': 'phone_num',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'رقم الهاتف'
        })
    )
    CITY_CHOICES =[
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
     ]
    city = forms.ChoiceField(choices=CITY_CHOICES,
     label='',
     widget=forms.Select(


        attrs={ 'id': 'city',
                'name': 'city',
                'required': 'required',
                'class': 'form-control',
                'placeholder': 'رقم الهاتف'
    })
    )
    US_CHOICES =[
        ('فيسبوك', 'فيسبوك'),
        ('انستغرام', 'انستغرام'),
        ('من اصدقائك', 'من اصدقائك'),
        ('أخرى', 'أخرى'),
     ]
    us = forms.ChoiceField(choices=US_CHOICES,
       label='',
       widget=forms.Select(
        attrs={ 'id': 'us',
                'name': 'us',
                'required': 'required',
                'class': 'form-control',
                'placeholder': 'من اين سمعت عنا ؟'
    })
    )
    birth = forms.IntegerField(
        label='',

        widget=forms.TextInput(
        attrs={ 'id': 'birth',
                'name': 'birth',
                'required': 'required',
                'class': 'form-control',
                'placeholder':'مواليد عام'
    })
    )


class search_forms(forms.Form):
    CITY_CHOICES = [
        ('', 'اختيار محافظة'),
        ('ادلب', 'ادلب'),
        ('حلب', 'حلب'),
        ('دمشق', 'دمشق'),
        ('ريف دمشق', 'ريف دمشق'),
        ('حماه', 'حماه'),
        ('حمص', 'حمص'),
        ('درعا', 'درعا'),
        ('القنيطرة', 'القنيطرة'),
        ('السويداء', 'السويداء'),
        ('دير الزور', 'دير الزور'),
        ('الرقة', 'الرقة'),
        ('الحسكة', 'الحسكة'),
        ('اللاذقية', 'اللاذقية'),
        ('طرطوس', 'طرطوس'),
    ]

    Aqar_CHOICES = [
        ('', 'اختيار نوع العقار'),
        ('مزارع', 'مزارع'),
        ('شقة', 'شقق'),
        ('مسابح', 'مسابح'),
        ('فيلا', 'فيلات'),
    ]

    Alser_CHOICES = [
        ('', 'اختيار الحد الاعلى'),
        ('50', '50$'),
        ('100', '100$'),
        ('150', '150$'),
        ('200', '200$'),
        ('250', '250$'),
        ('300', '300$'),
        ('350', '350$'),
        ('400', '400$'),
        ('450', '450$'),
        ('500', '500$'),
        ('600', '600$'),
        ('700', '700$'),
        ('800', '800$'),
        ('900', '900$'),
        ('1000', '1000$'),
    ]

    city = forms.ChoiceField(
        choices=CITY_CHOICES,
        label='',
        widget=forms.Select(
            attrs={'id': 'city', 'name': 'city', 'required': 'required'}
        )
    )

    Aqar = forms.ChoiceField(
        choices=Aqar_CHOICES,
        label='',
        widget=forms.Select(
            attrs={'id': 'Aqar', 'name': 'Aqar', 'required': 'false'}
        )
    )

    Madena = forms.ChoiceField(
        label='',
        widget=forms.Select(
            attrs={'id': 'Madena', 'name': 'Madena', 'required': 'required'}
        )
    )

    Alser = forms.ChoiceField(
        choices=Alser_CHOICES,
        label='',
        widget=forms.Select(
            attrs={'id': 'Alser', 'name': 'Alser', 'required': 'false'}
        )
    )

    def __init__(self, *args, **kwargs):
        towns = kwargs.pop('towns', {})
        super(search_forms, self).__init__(*args, **kwargs)
        self.fields['Madena'].choices = [('', 'اختيار مدينة أو بلدة')] + [
            (town, town) for city_towns in towns.values() for town in city_towns
        ]



class edit_My_Profile_form(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'id': 'username',
            'name': 'username',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'الاسم',
            'verbose_name':'الاسم'
        })
    )
    old_password = forms.CharField(
        label='',

        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'كلمة المرور'
        })
    )
    password = forms.CharField(
        label='',

        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'كلمة المرور'
        })
    )

    conferm_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'id': 'conferm_password',
            'name': 'conferm_password',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'تاكيد كلمة المرور'
        })
    )
    phone_num = forms.CharField(
        label='',

        widget=forms.TextInput(attrs={
            'id': 'phone_num',
            'name': 'phone_num',
            'required': 'required',
            'class': 'form-control',
            'placeholder': 'رقم الهاتف'
        })
    )




class UnBookedForm(forms.ModelForm):
    class Meta:
        model = NewRealEstate
        fields = [ 'notes', 'type', 'address_detail','address']
        widgets = {
            'notes': forms.Textarea
            (attrs={'id': 'user-input', 'name': 'user-input',
                    'rows': 4, 'cols': 50,
                 'placeholder': '... أدخل التفاصيل هنا ',
                    'class': 'text',
                    }),
            'address_detail': forms.Textarea
            (attrs={'id': 'location-input', 'name': 'location-input',
                    'rows': 4, 'cols': 50,
                 'placeholder': '... أدخل الموقع بالتفصيل  هنا '
                   }),
            'type': forms.Select(attrs={'class': 'wide'}),
            'address': forms.Select(attrs={'class': 'wide'}),
        #so you can make sure that day_of_week can be entered (by the user) just as selections
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
