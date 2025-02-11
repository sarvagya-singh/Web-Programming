from django.urls import path
from . import views

urlpatterns = [
    path('promotion/', views.promotion_view, name='promotion_view'),  #Keep this line if you want /promotion/ to work
    path('', views.promotion_view, name='home'),  # Define a view for the empty path
]
