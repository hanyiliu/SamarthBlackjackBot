import numpy as np
from agent import BlackjackAgent
from blackjack_env.environment import BlackjackEnvironment
import os

# Create an instance of the BlackjackEnvironment
env = BlackjackEnvironment()

def test_agent(n_games, q_table):
    wins = 0
    agent = BlackjackAgent()
    agent.q_table = q_table

    for _ in range(n_games):
        state = env.reset()
        done = False
        while not done:
            actions = env.get_actions()
            action = agent.choose_action(state, actions)
            next_state, reward, done = env.step(action)

            if done and reward == 1:
                wins += 1
            state = next_state
    win_percentage = (wins / n_games) * 100
    return win_percentage

# Load the trained Q-tables from the subfolder
trained_agents_folder = 'trained_agents'
q_tables = []
for filename in os.listdir(trained_agents_folder):
    if filename.startswith('q_table_') and filename.endswith('.npy'):
        filepath = os.path.join(trained_agents_folder, filename)
        q_table = np.load(filepath, allow_pickle=True).item()
        q_tables.append(q_table)

# Test each agent
n_games = 10000
for i, q_table in enumerate(q_tables):
    win_percentage = test_agent(n_games, q_table)
    print(f'Agent {i+1} won {win_percentage:.2f}% of games.')
