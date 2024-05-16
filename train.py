from agent import BlackjackAgent
from blackjack_env.environment import BlackjackEnvironment
import numpy as np
import os
from test import test_agent
import pandas as pd

# Create an instance of the BlackjackEnvironment
env = BlackjackEnvironment()

# Define hyperparameter combinations to test
hyperparameters = [
    {'alpha': 0.1, 'gamma': 0.9, 'epsilon': 0.1}
    # Add more combinations here...
]

# Create a subfolder to store the trained agents
trained_agents_folder = 'trained_agents'
if not os.path.exists(trained_agents_folder):
    os.makedirs(trained_agents_folder)

# Train and test each agent
for i, params in enumerate(hyperparameters):
    print(f'Training agent {i+1} with hyperparameters: {params}')

    # Create an instance of the BlackjackAgent with the current hyperparameters
    agent = BlackjackAgent(**params)

    # Train the agent
    agent.train(env, episodes=100000)

    # Print out the Q-table
    print(f"Agent {i+1} Q-table:")
    q_table_list = [(state, action, q_value) for (state, action), q_value in agent.q_table.items()]
    q_table_df = pd.DataFrame(q_table_list, columns=['State', 'Action', 'Q-value'])
    print(q_table_df)

    # Save the trained Q-table to a file in the subfolder
    filename = f'q_table_{i+1}.npy'
    filepath = os.path.join(trained_agents_folder, filename)
    with open(filepath, 'wb') as f:
        np.save(f, agent.q_table)

    print(f'Saved Q-table to {filepath}')

    # Test the agent and print the win percentage
    n_games = 10000
    win_percentage = test_agent(n_games, agent.q_table)
    print(f'Agent {i+1} won {win_percentage:.2f}% of games.')
