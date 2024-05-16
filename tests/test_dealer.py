import unittest
import sys
sys.path.insert(0, '../')
from dealer import Dealer
from deck import Deck, Card


class TestDealer(unittest.TestCase):
    def test_initial_score(self):
        dealer = Dealer()
        self.assertEqual(dealer.score, 0)

    def test_hit(self):
        dealer = Dealer()
        dealer.hit(Deck())
        self.assertGreater(dealer.score, 0)

    def test_stand(self):
        dealer = Dealer()
        dealer.stand()
        self.assertEqual(dealer.score, 0)

    def test_calculate_score(self):
        dealer = Dealer()
        dealer.hand = [Card("Ace", "Hearts"), Card("10", "Diamonds")]
        dealer.calculate_score()
        self.assertEqual(dealer.score, 21)

    def test_reveal_upcard(self):
        dealer = Dealer()
        dealer.hand = [Card("Ace", "Hearts"), Card("10", "Diamonds")]
        dealer.reveal_upcard()
        self.assertEqual(dealer.upcard, dealer.hand[0])

    def test_multiple_aces(self):
        dealer = Dealer()
        dealer.hand = [Card("Ace", "Hearts"), Card("Ace", "Diamonds")]
        dealer.calculate_score()
        self.assertEqual(dealer.score, 12)

    def test_bust(self):
        dealer = Dealer()
        dealer.hand = [Card("10", "Hearts"), Card("10", "Diamonds"), Card("10", "Clubs")]
        dealer.calculate_score()
        self.assertGreater(dealer.score, 21)

    def test_empty_hand(self):
        dealer = Dealer()
        dealer.calculate_score()
        self.assertEqual(dealer.score, 0)

    def test_non_numeric_ranks(self):
        dealer = Dealer()
        dealer.hand = [Card("Jack", "Hearts"), Card("Queen", "Diamonds")]
        dealer.calculate_score()
        self.assertEqual(dealer.score, 20)


if __name__ == "__main__":
    unittest.main()
