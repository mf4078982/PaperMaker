from django.shortcuts import render,HttpResponse

# Create your views here.



def home(request):
    return render(request, "home.html") 
def help(request):
    return render(request, "help.html") 

def send(request):
<<<<<<< HEAD
    return render(request, "sendfeed.html")
=======
    return render(request, "sendfeed.html")
def about(request):
    return render(request, 'about.html')

def userList(request):
    return render(request, 'user_list.html')
>>>>>>> ffc18c8 (Refactored pages to use base template and added Users/About pages)
