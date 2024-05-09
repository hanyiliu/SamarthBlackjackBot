class Player:
    def __init__(self):
        self.hands = [[]]
        self.scores = [0]
        self.bet = 0

    def hit(self, deck, hand_index=0):
        self.hands[hand_index].append(deck.draw())
        self.calculate_score(hand_index)

    def stand(self):
        pass

    def double_down(self, deck, hand_index=0):
        self.bet *= 2
        self.hit(deck, hand_index)
        self.stand()

    def split(self, deck):
        self.hands = [[self.hands[0][0]], [self.hands[0][1]]]
        self.scores = [0, 0]
        if self.hands[0][0].rank == "Ace":
            self.hit(deck, 0)
            self.stand()
            self.hit(deck, 1)
            self.stand()
        else:
            self.hit(deck, 0)
            self.hit(deck, 1)

    def calculate_score(self, hand_index=0):
        self.scores[hand_index] = 0
        num_aces = 0
        for card in self.hands[hand_index]:
            if card.rank == "Ace":
                num_aces += 1
                self.scores[hand_index] += 11
            elif card.rank in ["Jack", "Queen", "King"]:
                self.scores[hand_index] += 10
            else:
                self.scores[hand_index] += int(card.rank)
        while self.scores[hand_index] > 21 and num_aces:
            self.scores[hand_index] -= 10
            num_aces -= 1

    def get_state(self):
        return tuple(tuple(hand) for hand in self.hands), tuple(self.scores), self.bet

    def __repr__(self):
        return f"Player(hands={self.hands}, scores={self.scores}, bet={self.bet})"
