import unittest

import sys
sys.path.insert(0, '../')

from blackjack_env.environment import BlackjackEnvironment
from blackjack_env.game import Game
from blackjack_env.player import Player
from blackjack_env.dealer import Dealer
from blackjack_env.deck import Deck
from blackjack_env.deck import Card

class TestEnvironment(unittest.TestCase):
    def test_states(self):
        # Create a new environment
        env = BlackjackEnvironment()
        env.game = Game()
        # Set up the game with a specific state
        env.game.player = Player()
        env.game.dealer = Dealer()
        env.game.deck = Deck()

        # Deal two cards to the player and one card to the dealer
        env.game.player.hands = [[Card(10, 'Hearts'), Card(5, 'Diamonds')]]
        env.game.player.scores = [15]
        env.game.dealer.upcard = Card(7, 'Clubs')

        # Get the state from the environment
        state = env.get_state()[0]

        # Check that the state is correct
        self.assertEqual(state[0], (10, 5))  # player's hand values
        self.assertEqual(state[1], 7)  # dealer's upcard value

    def test_states_after_split(self):
        # Create a new environment
        env = BlackjackEnvironment()
        env.game = Game()
        # Set up the game with a specific state
        env.game.player = Player()
        env.game.dealer = Dealer()
        env.game.deck = Deck()

        # Deal two cards to the player and one card to the dealer
        env.game.player.hands = [[Card(5, 'Hearts'), Card(5, 'Diamonds')]]
        env.game.player.scores = [10]
        env.game.dealer.upcard = Card(7, 'Clubs')

        # Split the hand
        env.game.player.split(env.game.deck)

        # Get the states from the environment
        states = env.get_state()

        # Check that the states are correct
        self.assertEqual(len(states), 2)  # There should be two hands after splitting
        self.assertEqual(len(states[0][0]), 2)  # First hand should have two cards
        self.assertEqual(states[0][0][0], 5)  # First card in first hand should be a 5
        self.assertEqual(states[0][1], 7)  # Dealer's upcard value
        self.assertEqual(len(states[1][0]), 2)  # Second hand should have two cards
        self.assertEqual(states[1][0][0], 5)  # First card in second hand should be a 5
        self.assertEqual(states[1][1], 7)  # Dealer's upcard value
if __name__ == '__main__':
    unittest.main()
