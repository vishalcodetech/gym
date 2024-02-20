from django.urls import path
from.views import*

urlpatterns = [
    path('',home,name="home"),
    path('account/',account,name="account"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('classes/',classes,name="classes"),
    path('login/',Loginuser,name="login"),
    path('photo/',photo,name="photo"),
    path('signup/',Signup,name="signup"),
    path('logout/',Loginuser, name="logout"),
    path('service/',service,name='service')
]