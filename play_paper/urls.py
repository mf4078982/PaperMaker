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
    path('nursery_english/', views.nursery_english_paper, name='nursery_english'),
    path('reset_nursery_english/', views.reset_nursery_english_paper, name='reset_nursery_english'),
    path('nursery_gk/', views.nursery_gk_paper, name='nursery_gk'),
    path('reset_nursery_gk/', views.reset_nursery_gk_paper, name='reset_nursery_gk'),
    path('nursery_urdu/', views.nursery_urdu_paper, name='nursery_urdu'),
    path('reset_nursery_urdu/', views.reset_nursery_urdu_paper, name='reset_nursery_urdu'),
    path('nursery_math/', views.nursery_math_paper, name='nursery_math'),
    path('reset_nursery_math/', views.reset_nursery_math_paper, name='reset_nursery_math'),
    path('nursery_drawing/', views.nursery_drawing_paper, name='nursery_drawing'),
    path('reset_nursery_drawing/', views.reset_nursery_drawing_paper, name='reset_nursery_drawing'),
    path('prep_english/', views.prep_english_paper, name='prep_english'),
    path('reset_prep_english/', views.reset_prep_english_paper, name='reset_prep_english'),
    path('prep_math/', views.prep_math_paper, name='prep_math'),
    path('reset_prep_math/', views.reset_prep_math_paper, name='reset_prep_math'),
    path('prep_urdu/', views.prep_urdu_paper, name='prep_urdu'),
    path('reset_prep_urdu/', views.reset_prep_urdu_paper, name='reset_prep_urdu'),
    path('generate_find_circle_image/', views.generate_find_circle_image, name='generate_find_circle_image'),
]

