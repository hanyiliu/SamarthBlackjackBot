import numpy as np
import random

class BlackjackAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        """
        Initialize the agent with Q-learning parameters.

        Args:
            alpha (float): Learning rate (default=0.1)
            gamma (float): Discount factor (default=0.9)
            epsilon (float): Exploration rate (default=0.1)

        Initializes:
            self.q_table: A dictionary to store state-action values
            self.alpha: Learning rate
            self.gamma: Discount factor
            self.epsilon: Exploration rate
        """
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, state, actions):
        """
        Choose an action using epsilon-greedy policy.

        Args:
            state (tuple): Current state of the game
            actions (list): List of possible actions

        Returns:
            action (int): Chosen action
        """
        if random.random() < self.epsilon:
            # Explore: choose a random action
            return random.choice(actions)
        else:
            # Exploit: choose the action with the highest Q-value
            q_values = [self.q_table.get((state, action), 0) for action in actions]
            return actions[np.argmax(q_values)]

    def learn(self, state, action, next_state, reward, actions):
        """
        Update the Q-table based on the experience.

        Args:
            state (tuple): Current state of the game
            action (int): Action taken
            next_state (tuple): Next state of the game
            reward (float): Reward received

        Updates:
            self.q_table: Q-value for the given state-action pair
        """
        q_value = self.q_table.get((state, action), 0)
        next_q_values = [self.q_table.get((next_state, next_action), 0) for next_action in range(4)]
        next_q_value = max(next_q_values)
        td_error = reward + self.gamma * next_q_value - q_value
        self.q_table[(state, action)] = q_value + self.alpha * td_error

    def train(self, env, episodes=1000):
        """
        Train the agent by interacting with the environment.

        Args:
            env (BlackjackEnvironment): Environment to interact with
            episodes (int): Number of episodes to train (default=1000)

        Trains:
            self.q_table: Q-values for all state-action pairs
        """
        for episode in range(episodes):
            state = env.reset()
            done = False
            while not done:
                actions = env.get_actions()
                action = self.choose_action(state, actions)
                next_state, reward, done = env.step(action)
                self.learn(state, action, next_state, reward, actions)
                state = next_state

    def play(self, env):
        """
        Play a game using the learned policy.

        Args:
            env (BlackjackEnvironment): Environment to interact with

        Plays:
            A game of Blackjack using the greedy policy
        """
        state = env.reset()
        done = False
        while not done:
            actions = env.get_actions()
            action = self.choose_action(state, actions)
            next_state, reward, done = env.step(action)
            state = next_state
