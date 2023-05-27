from . import views
from django.urls import path
urlpatterns = [
path('inscription/',views.index,name='inscription'),   
path('acces/',views.acces,name='acces'), 
]

