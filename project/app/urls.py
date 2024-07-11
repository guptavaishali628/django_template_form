from django.urls import path
from.views import home,register,login,logindata

urlpatterns=[
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logindata/',logindata,name='logindata')
]