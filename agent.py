import numpy as np
import random

class BlackjackAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, states, actions):
        chosen_actions = []
        for state in states:
            if random.random() < self.epsilon:
                # Explore: choose a random action
                chosen_action = random.choice(actions)
            else:
                # Exploit: choose the action with the highest Q-value
                q_values = [self.q_table.get((state, action), 0) for action in actions]
                chosen_action = actions[np.argmax(q_values)]
            chosen_actions.append(chosen_action)
        return chosen_actions

    def learn(self, states, actions, next_states, rewards):
        for i in range(len(states)):
            state = states[i]
            action = actions[i]
            next_state = next_states[i]
            reward = rewards[i]

            q_value = self.q_table.get((state, action), 0)
            next_q_values = [self.q_table.get((next_state, next_action), 0) for next_action in range(4)]
            next_q_value = max(next_q_values)
            td_error = reward + self.gamma * next_q_value - q_value
            self.q_table[(state, action)] = q_value + self.alpha * td_error

    def train(self, env, episodes=1000):
        for episode in range(episodes):
            if episode % (episodes // 20) == 0:
                print(f"Iteration {episode}")
            state = env.reset()
            done = False
            while not done:
                actions = env.get_actions()
                action = self.choose_action(state, actions)
                next_state, reward, done = env.step(action)
                self.learn(state, action, next_state, reward)
                state = next_state

    def play(self, env):
        state = env.reset()
        done = False
        while not done:
            actions = env.get_actions()
            action = self.choose_action(state, actions)
            next_state, reward, done = env.step(action)
            state = next_state
