class Dealer:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.upcard = None

    def hit(self, deck):
        self.hand.append(deck.draw())
        self.calculate_score()

    def stand(self):
        pass

    def calculate_score(self):
        self.score = 0
        num_aces = 0
        for card in self.hand:
            if card.rank == "Ace":
                num_aces += 1
                self.score += 11
            elif card.rank in ["Jack", "Queen", "King"]:
                self.score += 10
            else:
                self.score += int(card.rank)
        while self.score > 21 and num_aces:
            self.score -= 10
            num_aces -= 1

    def reveal_upcard(self):
        self.upcard = self.hand[0]

    def get_state(self):
        upcard_value = self.upcard.rank
        if upcard_value in ["Jack", "Queen", "King"]:
            upcard_value = 10
        elif upcard_value == "Ace":
            upcard_value = "Ace"
        else:
            upcard_value = int(upcard_value)
        return upcard_value, self.score

    def __repr__(self):
        return f"Dealer(hand={self.hand}, score={self.score}, upcard={self.upcard})"
