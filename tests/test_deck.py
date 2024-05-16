import unittest

import sys
sys.path.insert(0, '../')

from deck import Deck, Card

class TestDeck(unittest.TestCase):
    def test_reset(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_draw(self):
        deck = Deck()
        card = deck.draw()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck), 51)

    def test_shuffle(self):
        deck = Deck()
        original_order = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)

    def test_empty_draw(self):
        deck = Deck()
        for _ in range(52):
            deck.draw()
        with self.assertRaises(ValueError):
            deck.draw()

if __name__ == "__main__":
    unittest.main()
