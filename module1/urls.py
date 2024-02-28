from django.contrib import admin
from django.urls import path

from . import views
from . views import *

urlpatterns = [
    path('hello1/', views.hello, name='hello1'),
    path('', views.newhomepage, name='newhomepage'),
    path('travelpackage/', views.travelpackage, name="travelpackage"),
    path('print/', print1, name="print"),
    path('print_to_console1/', print_to_console, name='print_to_console1'),
    path('cusoon/',views.abcd, name='under'),
    path('otp/',otp,name='otp'),
    path('otps/',views.otps,name='otpgenerator'),
    path('date/',get_date,name='get_date'),
    path('dateu/',getdate,name='getdate'),
    path('register/',views.registercall,name='register'),
    path('registers/',views.registerloginfunction,name='registers'),
    path('chart/',pie_chart,name='pie_chart'),
    path('car/',callcar,name='car'),
    path('weather/',views.weatherpagecall,name='weather'),
    path('weathers/',views.weatherlogic,name='weatherlogic'),
    path('feedbackcall/',views.feebackcall,name='feedbackcall'),
    path('feedbackcalls',views.feeback,name='feedbackcalls'),
    #calling
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('login1/',views.login1,name='login1'),
    path('signup1/',views.signup1,name='signup1')

]
