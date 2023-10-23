from django.urls import path
from . import views



urlpatterns=[
    path('signupaccounts/',views.signupaccounts,name='signupaccounts'),
    path('logout/',views.logoutaccount,name='logoutaccount'),
    path('login/',views.loginaccount,name='loginaccount'),
]