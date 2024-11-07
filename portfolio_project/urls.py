# portfolio_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Include is for including app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Include the portfolio app URLs only
]
