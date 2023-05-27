from django.urls import path
from . import views 



urlpatterns = [
    
    path('', views.index_v, name='index'),
    path('about/',views.about_v, name='about'),
    path('contact/', views.contact_v, name='contact'),
    path('quiz/', views.quiz_v, name='quiz'),
    path('login/', views.login_v, name='login'),
   
   


]
