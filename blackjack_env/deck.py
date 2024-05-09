import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            raise ValueError("No more cards in the deck")
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)
