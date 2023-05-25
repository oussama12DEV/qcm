from django.urls import path
from . import views

urlpatterns = [
 path('my_qcm/<int:quiz_id>/', views. start_quiz, name='start_quiz'),
 path('my_qcm/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
 path('my_qcm/<int:quiz_id>/result/', views.quiz_result, name='quiz_result'),
]