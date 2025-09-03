"""
URL configuration for rock_paper_scissors_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game.urls')),  # Include game app URLs
]
