from django.urls import path
from .import views


urlpatterns = [
    path("",views.home,name="home"),
    path("help/",views.help,name="help"),
    path("send/",views.send,name="send"),
    path("about/",views.about,name="about"),
]

