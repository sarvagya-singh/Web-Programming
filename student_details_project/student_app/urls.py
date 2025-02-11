from django.urls import path
from . import views

urlpatterns = [
    path('student_form/', views.student_form_view, name='student_form'), #This is now accessed via /student_form/
    path('', views.student_form_view, name='home'), # Add this line, now the empty path will render the form
]
