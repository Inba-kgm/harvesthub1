from django.urls import path,include
from .views import *


urlpatterns = [
    path('login_page',login_page,name='login_page'),
    path('',over,name='over'),
    path('login',login_page,name='login_page'),
    path('signup_page',signup_page,name='signup_page'),
]
