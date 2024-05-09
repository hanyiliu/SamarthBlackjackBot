from blackjack_env.game import Game

class BlackjackEnvironment:
    def __init__(self):
        self.game = Game()
        self.actions = ["hit", "stand", "double_down", "split"]

    def reset(self):
        self.game = Game()
        self.game.deal_initial_cards()
        return self.get_state()

    def step(self, action):
        if not (0 <= action < len(self.actions)):
            raise ValueError("Invalid action")

        if self.actions[action] == "hit":
            self.game.player.hit(self.game.deck)
        elif self.actions[action] == "stand":
            self.game.player.stand()
        elif self.actions[action] == "double_down":
            self.game.player.double_down(self.game.deck)
        elif self.actions[action] == "split":
            self.game.player.split(self.game.deck)

        state = self.get_state()
        reward = self.get_reward()
        done = self.is_done()
        return state, reward, done

    def get_state(self):
        player_hand, player_score, _ = self.game.player.get_state()
        dealer_upcard, _ = self.game.dealer.get_state()
        return (player_hand, player_score, dealer_upcard)

    def get_actions(self):
        return [i for i in range(len(self.actions))]

    def is_done(self):
        return self.game.player.scores[0] > 21 or self.game.dealer.score > 21 or self.game.player.stand

    def get_reward(self):
        if self.is_done():
            winner = self.game.determine_winner(self.game.player.scores[0])
            if winner == "Player":
                return 1
            elif winner == "Dealer":
                return -1
            else:
                return 0
        else:
            return 0
