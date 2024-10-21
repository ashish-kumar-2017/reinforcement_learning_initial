import gym
import numpy as np

cliffEnv = gym.make("CliffWalking-v0")

done = False
state = cliffEnv.reset()

while not done:
    print(cliffEnv.render(mode="ansi"))
    action=int(np.random.randint(low=0, high=4, size=1))
    print(state,"-->",["UP","RIGHT","DOWN","LEFT"][action])
    state, reward, done, _ = cliffEnv.step(action)
cliffEnv.close()

# import gym
#
# # Create the environment (assuming you are using 'CliffWalking-v0')
# cliffEnv = gym.make('CliffWalking-v0')
#
# # Reset the environment to the initial state
# cliffEnv.reset()
#
# # Render the environment (compatible with newer gym versions)
# # Instead of render(mode='ansi'), we print the current state directly
# for _ in range(5):  # You can adjust the number of steps as needed
#     cliffEnv.render()  # Render the environment (no 'mode' argument)
#     action = cliffEnv.action_space.sample()  # Random action
#     state, reward, done, info = cliffEnv.step(action)  # Take the action
#
#     if done:
#         print("Episode finished")
#         break
#
# import gym
# import numpy as np  # Ensure numpy is imported
#
# # Create the environment (assuming you are using 'CliffWalking-v0')
# cliffEnv = gym.make('CliffWalking-v0')
#
# # Reset the environment to the initial state
# cliffEnv.reset()
#
# # Render the environment (compatible with newer gym versions)
# # Instead of render(mode='ansi'), we print the current state directly
# for _ in range(5):  # You can adjust the number of steps as needed
#     cliffEnv.render()  # Render the environment (no 'mode' argument)
#
#     # Generate a random action (assuming there are 4 possible actions: 0, 1, 2, 3)
#     action = int(np.random.randint(low=0, high=4, size=1))
#
#     # Take the action
#     state, reward, done, info = cliffEnv.step(action)
#
#     # Print the results
#     print(f"Action: {action}, State: {state}, Reward: {reward}, Done: {done}")
#
#     # If the episode is finished, stop the loop
#     if done:
#         print("Episode finished")
#         break
