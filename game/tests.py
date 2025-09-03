"""
Tests for the Rock Paper Scissors game.

Contains unit tests for game logic, views, and functionality.
"""

import json
from django.test import TestCase, Client
from django.urls import reverse
from .views import determine_winner


class GameLogicTests(TestCase):
    """Test the core game logic."""

    def test_determine_winner_rock_vs_scissors(self):
        """Test rock beats scissors."""
        result = determine_winner('rock', 'scissors')
        self.assertEqual(result, 'win')

    def test_determine_winner_paper_vs_rock(self):
        """Test paper beats rock."""
        result = determine_winner('paper', 'rock')
        self.assertEqual(result, 'win')

    def test_determine_winner_scissors_vs_paper(self):
        """Test scissors beats paper."""
        result = determine_winner('scissors', 'paper')
        self.assertEqual(result, 'win')

    def test_determine_winner_draw(self):
        """Test same choices result in draw."""
        result = determine_winner('rock', 'rock')
        self.assertEqual(result, 'draw')

        result = determine_winner('paper', 'paper')
        self.assertEqual(result, 'draw')

        result = determine_winner('scissors', 'scissors')
        self.assertEqual(result, 'draw')

    def test_determine_winner_lose_scenarios(self):
        """Test losing scenarios."""
        result = determine_winner('rock', 'paper')
        self.assertEqual(result, 'lose')

        result = determine_winner('paper', 'scissors')
        self.assertEqual(result, 'lose')

        result = determine_winner('scissors', 'rock')
        self.assertEqual(result, 'lose')


class GameViewTests(TestCase):
    """Test the game views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_home_view(self):
        """Test home page loads correctly."""
        response = self.client.get(reverse('game:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rock Paper Scissors')

    def test_play_move_valid_choice(self):
        """Test playing a valid move."""
        data = {'choice': 'rock'}
        response = self.client.post(
            reverse('game:play_move'),
            json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertIn('player_choice', response_data)
        self.assertIn('computer_choice', response_data)
        self.assertIn('result', response_data)
        self.assertEqual(response_data['player_choice'], 'rock')

    def test_play_move_invalid_choice(self):
        """Test playing an invalid move."""
        data = {'choice': 'invalid'}
        response = self.client.post(
            reverse('game:play_move'),
            json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_reset_game(self):
        """Test game reset functionality."""
        # Play a move first
        data = {'choice': 'rock'}
        self.client.post(
            reverse('game:play_move'),
            json.dumps(data),
            content_type='application/json'
        )

        # Reset the game
        response = self.client.post(reverse('game:reset_game'))
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['player_score'], 0)
        self.assertEqual(response_data['computer_score'], 0)
        self.assertEqual(response_data['draw_score'], 0)
