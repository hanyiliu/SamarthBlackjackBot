from blackjack_env.deck import Deck, Card
from blackjack_env.player import Player
from blackjack_env.dealer import Dealer
import random

class Game:
    def __init__(self, always_double=False):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
        self.always_double = always_double

    def deal_initial_cards(self):
        if self.always_double:
            self.player.hit(self.deck)
            self.player.hands[0].append(Card(self.player.hands[0][0].rank, random.choice(["Diamonds", "Clubs", "Hearts", "Spades"])))
            self.player.calculate_score()
        else:
            for _ in range(2):
                self.player.hit(self.deck)

        for _ in range(2):
            self.dealer.hit(self.deck)
        self.dealer.reveal_upcard()

    def display_player_hand(self, hand_index):
        print(f"Player's hand {hand_index+1}: {', '.join(str(card) for card in self.player.hands[hand_index])}, score: {self.player.scores[hand_index]}")

    def play_round(self):
        self.deal_initial_cards()
        print("Initial cards:")

        print(f"Dealer: [{self.dealer.upcard}, ?], score: ?")

        hand_index = 0
        while hand_index < len(self.player.hands):
            while True:
                self.display_player_hand(hand_index)
                if self.player.scores[hand_index] > 21:
                    print(f"Hand {hand_index+1} busts!")
                    break
                action = input(f"What would you like to do with hand {hand_index+1}? (hit, stand, double down, split): ")
                if action.lower() == "hit":
                    self.player.hit(self.deck, hand_index)
                elif action.lower() == "stand":
                    break
                elif action.lower() == "double down":
                    self.player.double_down(self.deck, hand_index)
                    self.display_player_hand(hand_index)
                    break
                elif action.lower() == "split":
                    if len(self.player.hands) > 1:
                        print("You can't split again.")
                    elif self.player.hands[hand_index][0].rank != self.player.hands[hand_index][1].rank:
                        print("You can't split these cards.")
                    else:
                        self.player.split(self.deck)
                else:
                    print("Invalid action. Please try again.")

            hand_index += 1

        print(f"Dealer: {', '.join(str(card) for card in self.dealer.hand)}, score: {self.dealer.score}")

        for i, score in enumerate(self.player.scores):
            winner = self.determine_winner(score)
            print(f"The winner of hand {i+1} is: {winner}!")
    def determine_winner(self, player_score):
        if player_score > 21:
            return "Dealer"
        elif self.dealer.score > 21:
            return "Player"
        elif player_score > self.dealer.score:
            return "Player"
        elif player_score < self.dealer.score:
            return "Dealer"
        else:
            return "Push"

    def play_game(self):
        while True:
            winner = self.play_round()
            play_again = input("Would you like to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
            self.deck.reset()
            self.player = Player()
            self.dealer = Dealer()

if __name__ == "__main__":
    game = Game(always_double=True)

    game.play_game()
