import unittest

import sys
sys.path.insert(0, '../')

from game import Game
from unittest.mock import patch


class TestGame(unittest.TestCase):
    def test_deal_initial_cards(self):
        game = Game()
        game.deal_initial_cards()
        self.assertEqual(len(game.player.hand), 2)
        self.assertEqual(len(game.dealer.hand), 2)

    def test_determine_winner_player_busts(self):
        game = Game()
        game.player.score = 22
        self.assertEqual(game.determine_winner(), "Dealer")

    def test_determine_winner_dealer_busts(self):
        game = Game()
        game.dealer.score = 22
        self.assertEqual(game.determine_winner(), "Player")

    def test_determine_winner_player_wins(self):
        game = Game()
        game.player.score = 20
        game.dealer.score = 19
        self.assertEqual(game.determine_winner(), "Player")

    def test_determine_winner_dealer_wins(self):
        game = Game()
        game.player.score = 19
        game.dealer.score = 20
        self.assertEqual(game.determine_winner(), "Dealer")

    def test_determine_winner_push(self):
        game = Game()
        game.player.score = 20
        game.dealer.score = 20
        self.assertEqual(game.determine_winner(), "Push")

    def test_play_round_invalid_action(self):
        game = Game()
        with patch('builtins.input', side_effect=['invalid', 'stand']):
            with patch('builtins.print') as mock_print:
                game.play_round()
                mock_print.assert_any_call("Invalid action. Please try again.")

    def test_dealer_print_statements(self):
        game = Game()
        with patch('builtins.input', side_effect=['stand']):
            with patch('builtins.print') as mock_print:
                game.play_round()
                mock_print.assert_any_call(f"Dealer: [{game.dealer.upcard}, ?], score: ?")
                mock_print.assert_any_call(f"Dealer: {game.dealer.hand}, score: {game.dealer.score}")

if __name__ == "__main__":
    unittest.main()
