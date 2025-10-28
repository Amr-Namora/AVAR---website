from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [

    path('home/',views.home,name='main'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('gallery/',views.gallery,name='gallery'),
    path('newres/',views.newres,name='newres'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editMyProfile/',views.editMyProfile,name='editMyProfile'),
    path('help/',views.help,name='help'),
    path('resProfile/<slug:slug>/',views.resProfile,name='resProfile'),
]
