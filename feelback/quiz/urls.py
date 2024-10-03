from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitfeedback/', views.submitfeedback, name='submitfeedback'),
    path('dashboard/', views.dashboard, name='dashboard'),
]