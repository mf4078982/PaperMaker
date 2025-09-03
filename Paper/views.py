from django.shortcuts import render, redirect,HttpResponse
from .models import FeedBack
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html")

def help(request):
    return render(request, "help.html")

def send(request):
    return render(request, "sendfeed.html")

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
        send_mail(
            subject=f'New feedback from {Name}',
            message=f'Name: {Name}\nEmail: {Email}\nPhone: {Phone_no}\nMessage: {Message}',
            from_email=None,
            recipient_list=['bismashehzadi842@gmail.com'],
        )
        return HttpResponse('thank_you')  # URL ka name "thank_you" hona chahiye
    return render(request, 'sendfeed.html')
