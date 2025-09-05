from django.shortcuts import render
from .models import cracc
from farmer.models import *
import json

# Create your views here.
def login_page(request):
    return render(request,'login/login.html')


def signup_page(request):
    return render(request,'login/signup.html')

def over(request):
    myname=request.session.get('myname')
    products=farmerproduct.objects.all()
    products_list=list(products.values())
    context={'products_json':json.dumps(products_list),'products_count':products.count,'myname':myname}
    return render(request,'over/cover.html',context)
