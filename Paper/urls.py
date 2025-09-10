from django.urls import path
from .import views


urlpatterns = [
    path("",views.home,name="home"),
    path("help/",views.help,name="help"),
    path("send/",views.send,name="send"),
    path("about/",views.about,name="about"),
    path("user/",views.userList,name="userList"),
    path('contact/',views.contact_page,name='contact_page'),
    path("term/",views.term_page,name='term_page'),
    path("login/",views.login_page,name='login_page'),
    
    
    
]

