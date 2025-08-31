from django.shortcuts import render,HttpResponse

# Create your views here.


def app(request):
    return render(request, "home.html")  