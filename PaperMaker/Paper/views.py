from django.shortcuts import render,HttpResponse

# Create your views here.



def home(request):
    return render(request, "home.html") 
def help(request):
    return render(request, "help.html") 

def send(request):
    return render(request, "sendfeed.html")

def about(request):
    return render(request, "about.html")