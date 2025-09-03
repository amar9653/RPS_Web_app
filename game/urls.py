"""
URL patterns for the game app.

Defines the URL routes for:
1. Home page (game interface)
2. AJAX endpoint for playing moves
3. AJAX endpoint for resetting the game
"""

from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    # Home page - displays the game interface
    path('', views.home, name='home'),

    # AJAX endpoint for playing a move
    path('play/', views.play_move, name='play_move'),

    # AJAX endpoint for resetting the game
    path('reset/', views.reset_game, name='reset_game'),
]
