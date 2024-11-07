# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Example route to a 'home' view in portfolio
]

