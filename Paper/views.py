from django.shortcuts import render,HttpResponse

# Create your views here.



def home(request):
    return render(request, "home.html") 
def help(request):
    return render(request, "help.html") 

def send(request):
    return render(request, "sendfeed.html")

def about(request):
    return render(request, 'about.html')

def userList(request):
    return render(request, 'user_list.html')

def contact_page(request):
    return render(request,'contact.html')

def term_page(request):
    return render(request, "term_page.html")

def login_page(request):
    return render(request, "login.html")
def register(request):
    return render(request, "register.html")

def navbar_user(request):
    return render(request, "navbar_user.html")