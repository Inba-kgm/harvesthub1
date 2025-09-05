from django.urls import path,include
from.views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('otpgeneration/',otpgeneration,name="otpgeneration"),
    path('logotpgen/',logotpgen,name='logotpgen'),
    path('verify/',verify,name='verify'),
    path('forgotpasspage/',forgotpasspage,name='forgotpasspage'),
    path('passchange/',passchange,name='passchange'),
    path('logotpverification/',logotpverification,name='logotpverification'),


]
