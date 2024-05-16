from blackjack_env.game import Game

class BlackjackEnvironment:
    def __init__(self):
        self.game = Game()
        self.actions = ["hit", "stand", "double_down", "split"]

    def reset(self):
        self.game = Game()
        self.game.deal_initial_cards()
        return self.get_state()

    def step(self, actions):
        if not all(0 <= action < len(self.actions) for action in actions):
            raise ValueError("Invalid action")

        for i, action in enumerate(actions):
            if self.actions[action] == "hit":
                self.game.player.hit(self.game.deck, hand_index=i)
            elif self.actions[action] == "stand":
                self.game.player.stand_action(hand_index=i)
            elif self.actions[action] == "double_down":
                self.game.player.double_down(self.game.deck, hand_index=i)
            elif self.actions[action] == "split":
                self.game.player.split(self.game.deck)

        state = self.get_state()
        reward = self.get_reward()
        #print(f"Reward: {reward}")
        done = self.is_done()
        return state, reward, done

    def get_state(self):
        player_hands, _, _ = self.game.player.get_state()
        dealer_upcard_value, _ = self.game.dealer.get_state()

        states = []
        for i in range(len(player_hands)):
            state = (tuple(card for card in player_hands[i]), dealer_upcard_value)
            states.append(state)

        return states

    def get_actions(self):
        return [i for i in range(len(self.actions))]

    def is_done(self):
        return [score > 21 or stand for score, stand in zip(self.game.player.scores, self.game.player.stand)]

    def get_reward(self):
        rewards = []
        for i, score in enumerate(self.game.player.scores):
            if score > 21:
                rewards.append(-1)
            elif self.game.player.stand[i]:
                winner = self.game.determine_winner(score)
                if winner == "Player":
                    rewards.append(1)
                elif winner == "Dealer":
                    rewards.append(-1)
                else:
                    rewards.append(0)
            else:
                rewards.append(0)
        return rewards
