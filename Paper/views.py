from django.shortcuts import render, redirect,HttpResponse
from .models import FeedBack
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def home(request):
    return render(request, "home.html")

def help(request):
    return render(request, "help.html")

# def send(request):
#     return render(request, "sendfeed.html")

def send_feedback(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone_no = request.POST.get('phone')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')

        FeedBack.objects.create(
            name=Name,
            email=Email,
            phone=Phone_no,
            subject=Subject,
            message=Message,
        )
       
        return HttpResponse('thank_you')  # URL ka name "thank_you" hona chahiye
    return render(request, 'sendfeed.html')


def about(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request,'contact.html')

def term_page(request):
    return render(request, "term_page.html")


def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request,'Password do not match')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request,'User already exist with this email')
            return redirect('register')
        user = User.objects.create_user(
            username= fullname,
            email=email,
            password=password,
            # first_name= fullname
        )
        user.save()
        messages.success(request,'Account created successfully, please login')
        return redirect('login_page')
            
    return render(request, "register.html")


def login_page(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in successfully')
            return HttpResponse('your dashborad')
        else:
            messages.error(request,'Invalid Email or Password')
            return redirect('login_page')
        
    return render(request,'login.html')
