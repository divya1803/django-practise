from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='Blog Home'),
    path('about/', views.about, name='Blog about'),
]