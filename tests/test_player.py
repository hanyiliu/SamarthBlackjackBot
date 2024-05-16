import unittest


import sys
sys.path.insert(0, '../')

from player import Player
from deck import Deck, Card

class TestPlayer(unittest.TestCase):
    def test_initial_score(self):
        player = Player()
        self.assertEqual(player.score, 0)

    def test_hit(self):
        player = Player()
        deck = Deck()
        player.hit(deck)
        self.assertGreater(player.score, 0)

    def test_stand(self):
        player = Player()
        player.stand()
        self.assertEqual(player.score, 0)

    def test_double_down(self):
        player = Player()
        player.bet = 10
        deck = Deck()
        player.double_down(deck)
        self.assertEqual(player.bet, 20)

    def test_split(self):
        player = Player()
        deck = Deck()
        player.hand = [Card("Ace", "Hearts"), Card("Ace", "Diamonds")]
        player.split(deck)
        self.assertEqual(len(player.hand), 1)

    def test_calculate_score(self):
        player = Player()
        player.hand = [Card("Ace", "Hearts"), Card("10", "Diamonds")]
        player.calculate_score()
        self.assertEqual(player.score, 21)

if __name__ == "__main__":
    unittest.main()
