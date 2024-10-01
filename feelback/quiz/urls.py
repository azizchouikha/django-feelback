from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('feedbackform/', views.feedbackform, name='feedbackform'),
    path('submitfeedback/', views.submitfeedback, name='submitfeedback'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
