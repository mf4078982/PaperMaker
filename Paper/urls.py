from django.urls import path
from .import views


urlpatterns = [
    path("",views.home,name="home"),
    path("help/",views.help,name="help"),
    path("send/",views.send,name="send"),
<<<<<<< HEAD
=======
    path("about/",views.about,name="about"),
    path("user/",views.userList,name="userList"),
    
    
>>>>>>> ffc18c8 (Refactored pages to use base template and added Users/About pages)
]

