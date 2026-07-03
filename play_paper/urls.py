from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns =[
    path('', RedirectView.as_view(url='select/', permanent=False), name='home'),
    path('paper',views.paper_generator,name='paper'),    
    path('reset/', views.reset_paper, name='reset_paper'),    
    path('select/',views.select_class_subject,name='select'),
    path('urdu/',views.urdu_paper,name='urdu'),
    path('reset_urdu/', views.reset_urdu_paper, name='reset_urdu_paper'),
    path('math/', views.math_paper, name='math'),
    path('reset_math/', views.reset_math_paper, name='reset_math_paper'),
]

