# predictor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('diabetes/', views.diabetes_prediction, name='diabetes_prediction'),  # Diabetes prediction page
    path('heart/', views.heart_disease_prediction, name='heart_prediction'),  # Heart disease prediction page
]