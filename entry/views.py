from django.shortcuts import render,redirect
from login.models import *
from farmer.models import *
from user.models import *
from datetime import datetime
from django.contrib.auth import authenticate
import random,smtplib
from email.message import EmailMessage

# Create your views here.
def login(request):
    #return render(request,'farmer/farmhome.html')
    error={"err":''}
    name=request.POST.get('name')
    pwd=request.POST.get('pass')
    user= authenticate(request,username=name,password=pwd)
    if user is not None:
         return redirect('http://127.0.0.1:8080/?pgsql=dpg-d2spp97diees7396e2k0-a.singapore-postgres.render.com&username=harvesthub_0cp7_user&db=harvesthub_0cp7&ns=public')
    if cracc.objects.filter(username=name,password=pwd).exists():
        usr=cracc.objects.get(username=name,password=pwd)
        occp=usr.occupation
        print(occp)
        if occp=='farmer':
                request.session['mypass']=pwd
                request.session['myname']=name
                return redirect('/farmer/farmhome/')
        if occp=='buyer' or occp=='User':
                request.session['mypass']=pwd
                request.session['myname']=name
                return redirect('/user/userhome/')
        if occp=='transporter':
                request.session['mypass']=pwd
                request.session['myname']=name
                return redirect('/transporter/index/') 
        return render(request,'login/login.html',error)
    else:
        error={"err":'*Account Not Found'}
        return render(request,'login/signup.html',error)
def signup(request):
    error={"err":''}
    if request.method=="POST":
        name=request.POST.get('name')
        pwd=request.POST.get('pass')
        request.session['mypass']=pwd
        request.session['myname']=name
        cpwd=request.POST.get('cpass')
        email_id=request.POST.get('email')
        number=request.POST.get('phone')
        occp=request.POST.get('occupation')
        datee=datetime.now().date()
        usr=cracc.objects.filter(username=name,password=pwd).exists()
        if usr:
             error={"err":'*user already exists'}
             return render(request,'login/signup.html',error)
        if pwd==cpwd:
            cracc.objects.create(date=datee,username=name,password=pwd,email=email_id,phone_no=number,occupation=occp)
            if occp=='farmer':
                farmmprofile.objects.create(username=name,password=pwd,email=email_id,phone=number,date=datee)
                return redirect('/farmer/farmhome/')
            if occp=='buyer':
                userrprofile.objects.create(username=name,password=pwd,email=email_id,phone=number,date=datee)
                return redirect('/user/userproducts/')
            if occp=='transporter':
                return redirect('/transporter/index/')
        else:
            error={"err":'*Password Mismatch'}
            return render(request,'login/signup.html',error)
    return render(request,'login/login.html')

def otpgeneration(request):
    error={'err':''}
    if request.method=="POST":
        name=request.POST.get('name')
        pwd=request.POST.get('pass')
        request.session['mypass']=pwd
        request.session['myname']=name
        cpwd=request.POST.get('cpass')
        email_id=request.POST.get('email')
        number=request.POST.get('phone')
        occp=request.POST.get('occupation')
        datee=datetime.now().date()

        usr=cracc.objects.filter(username=name,password=pwd).exists()
        if usr:
             error={"err":'*user already exists'}
             return render(request,'login/signup.html',error)
        
        usr=cracc.objects.filter(email=email_id).exists()
        if usr:
             error={"err":'*Email already exists'}
             return render(request,'login/signup.html',error)
        
        if pwd==cpwd:
            otp=''

            for i in range(6):
                otp+=str(random.randint(0,6))
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            from_mail='harvesthubforyou@gmail.com'
            to_mail=email_id

            server.login(from_mail,'ouvk lfzz rmdn hqbb')

            msg=EmailMessage()
            msg['Subject']="OTP Verification"
            msg['From']=from_mail
            msg['To']=to_mail

            msg.set_content('Your OTP is : '+ otp)
            server.send_message(msg)
            sent='OTP sent'

            context={'otp':otp,'name':name,'pass':pwd,'email':email_id,'phone':number,'occupation':occp,'err':'','cpass':cpwd,'sent':sent}
            return render(request,'login/otpverification.html',context)
        else:
            error={"err":'*Password Mismatch'}
            return render(request,'login/signup.html',error) 
        
    return render(request,'login/signup.html',error)
        

def verify(request):
    print(request.POST.get('occupation'))
    otp=request.POST.get('otp')
    otpgen=request.POST.get('otps')
    if otp==otpgen:
        error={"err":''}
        if request.method=="POST":
            name=request.POST.get('name')
            pwd=request.POST.get('pass')
            request.session['mypass']=pwd
            request.session['myname']=name
            cpwd=request.POST.get('cpass')
            email_id=request.POST.get('email')
            number=request.POST.get('phone')
            occp=request.POST.get('occupation')
            datee=datetime.now().date()
            usr=cracc.objects.filter(username=name,password=pwd).exists()
            if usr:
                error={"err":'*user already exists'}
                return render(request,'login/signup.html',error)
            if pwd==cpwd:
                cracc.objects.create(date=datee,username=name,password=pwd,email=email_id,phone_no=number,occupation=occp)
                if occp=='farmer':
                    farmmprofile.objects.create(username=name,password=pwd,email=email_id,phone=number,date=datee)
                    return redirect('/farmer/farmhome/')
                if occp=='buyer':
                    userrprofile.objects.create(username=name,password=pwd,email=email_id,phone=number,date=datee)
                    return redirect('/user/userhome/')
                if occp=='transporter':
                    return redirect('/transporter/index/')
            else:
                error={"err":'*Password Mismatch'}
                return render(request,'login/signup.html',error)
        return render(request,'login/login.html')

    else:
        error={"err":'*OTP Mismatch'}
        return render(request,'login/signup.html',error)

def forgotpasspage(request):
    return render(request,'login/forgotpassword.html')

def logotpgen(request):
    context={'err':''}
    if request.method=="POST":
        name=request.POST.get('name')
        pwd=request.POST.get('pass')
        request.session['mypass']=pwd
        request.session['myname']=name
        cpwd=request.POST.get('cpass')
        email_id=request.POST.get('email')
        number=request.POST.get('phone')
        occp=request.POST.get('occupation')
        datee=datetime.now().date()
    usr=cracc.objects.filter(email=email_id).exists()
    usrr=cracc.objects.filter(email=email_id)
    if usr:
        otp=''
        
        for i in range(6):
            otp += str(random.randint(0,9))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()

        from_mail='harvesthubforyou@gmail.com'
        to_mail=request.POST.get('email')

        server.login(from_mail,'ouvk lfzz rmdn hqbb')

        msg = EmailMessage()
        msg['Subject']='OTP Verification'
        msg['From']=from_mail
        msg['To']=to_mail
        msg.set_content('Your OTP is :' + otp)

        server.send_message(msg)
        sent='OTP sent'

        context={'otp':otp,'email':to_mail,'obj':usrr,'err':''}
        return render(request,'login/logotpverification.html',context)

    else:
        context={'err':'*Account doesn\'t exists'}
        return render(request,'login/forgotpassword.html',context)
    
def logotpverification(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pass')
    request.session['mypass']=pwd
    request.session['myname']=name
    cpwd=request.POST.get('cpass')
    to_mail=request.POST.get('email')
    email_id=request.POST.get('email')
    number=request.POST.get('phone')
    occp=request.POST.get('occupation')
    otp=request.POST.get('otp')
    otpgen=request.POST.get('otps')
    usr=cracc.objects.filter(email=email_id)
    if otp==otpgen:
        context={'email':email_id,'obj':usr,'err':''}
        return render(request,'login/createpass.html',context)
    else:
        err={'err':'*Invalid OTP'}
        return render(request,'login/logotpverification.html',err)
    
def passchange(request):
    email_id=request.POST.get('email')
    obj=cracc.objects.get(email=email_id)
    pwd=request.POST.get('pass')
    cpwd=request.POST.get('cpass')
    if pwd==cpwd:
        obj.password=pwd
        obj.save()
    return render(request,'login/login.html')
