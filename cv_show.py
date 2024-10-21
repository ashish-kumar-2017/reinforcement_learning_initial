import gym, cv2
import numpy as np

# Creating the Environment
cliffEnv = gym.make("CliffWalking-v0")


# Handy functions for Visuals
def initialize_frame():
    width, height = 600, 200
    img = np.ones(shape=(height, width, 3)) * 255.0
    margin_horizontal = 6
    margin_vertical = 2

    # Vertical Lines
    for i in range(13):
        img = cv2.line(img, (49 * i + margin_horizontal, margin_vertical),
                       (49 * i + margin_horizontal, 200 - margin_vertical), color=(0, 0, 0), thickness=1)

    # Horizontal Lines
    for i in range(5):
        img = cv2.line(img, (margin_horizontal, 49 * i + margin_vertical),
                       (600 - margin_horizontal, 49 * i + margin_vertical), color=(0, 0, 0), thickness=1)

    # Cliff Box
    img = cv2.rectangle(img, (49 * 1 + margin_horizontal + 2, 49 * 3 + margin_vertical + 2),
                        (49 * 11 + margin_horizontal - 2, 49 * 4 + margin_vertical - 2), color=(255, 0, 255),
                        thickness=-1)
    img = cv2.putText(img, text="Cliff", org=(49 * 5 + margin_horizontal, 49 * 4 + margin_vertical - 10),
                      fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

    # Goal
    frame = cv2.putText(img, text="G", org=(49 * 11 + margin_horizontal + 10, 49 * 4 + margin_vertical - 10),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0), thickness=2)
    # Start
    # frame = cv2.putText(img, text="S", org=(49 * 0 + margin_horizontal + 10, 49 * 4 + margin_vertical - 10),
    #                     fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0), thickness=2)
    return frame


def put_agent(img, state):
    margin_horizontal = 6
    margin_vertical = 2
    row, column = np.unravel_index(indices=state, shape=(4, 12))
    cv2.putText(img, text="A", org=(49 * column + margin_horizontal + 10, 49 * (row + 1) + margin_vertical - 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0), thickness=2)
    return img


# Initializing our environment
done = False
frame = initialize_frame()
state = cliffEnv.reset()

# For each step of the episode
while not done:
    # Show the current state of the environment
    frame2 = put_agent(frame.copy(), state)
    cv2.imshow("Cliff Walking", frame2)
    cv2.waitKey(250)

    # Select an action
    action = int(np.random.randint(low=0, high=4, size=1))

    # Take the action in the environment
    state, reward, done, _ = cliffEnv.step(action)
cliffEnv.close()



#
# import cv2
# import numpy as np
# import gym
#
# # Create the environment
# cliffEnv = gym.make('CliffWalking-v0')
#
#
# # Handy functions for Visuals
# def initialize_frame():
#     width, height = 600, 200
#     img = np.ones(shape=(height, width, 3)) * 255.0  # Initialize a white image
#     margin_horizontal = 6
#     margin_vertical = 2
#
#     # Debug print to check if img is initialized correctly
#     if img is None:
#         print("Error: Image initialization failed!")
#         return None
#
#     # Vertical Lines
#     for i in range(13):
#         img = cv2.line(img, (49 * i + margin_horizontal, margin_vertical),
#                        (49 * i + margin_horizontal, 200 - margin_vertical), color=(0, 0, 0), thickness=1)
#
#     # Horizontal Lines
#     for i in range(5):
#         img = cv2.line(img, (margin_horizontal, 49 * i + margin_vertical),
#                        (600 - margin_horizontal, 49 * i + margin_vertical), color=(0, 0, 0), thickness=1)
#
#     # Cliff Box
#     img = cv2.rectangle(img, (49 * 1 + margin_horizontal + 2, 49 * 3 + margin_vertical + 2),
#                         (49 * 11 + margin_horizontal - 2, 49 * 4 + margin_vertical - 2), color=(255, 0, 255),
#                         thickness=-1)
#
#     # Put "Cliff" Text
#     img = cv2.putText(img, text="Cliff", org=(49 * 5 + margin_horizontal, 49 * 4 + margin_vertical - 10),
#                       fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
#
#     # Goal
#     img = cv2.putText(img, text="G", org=(49 * 11 + margin_horizontal + 10, 49 * 4 + margin_vertical - 10),
#                       fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0), thickness=2)
#
#     # Debug print to check if img is still valid
#     if img is None:
#         print("Error: Image creation failed after drawing!")
#         return None
#
#     return img  # Return the frame if successful
#
#
# def put_agent(img, state):
#     margin_horizontal = 6
#     margin_vertical = 2
#     row, column = np.unravel_index(indices=state, shape=(4, 12))
#     cv2.putText(img, text="A", org=(49 * column + margin_horizontal + 10, 49 * (row + 1) + margin_vertical - 10),
#                 fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0), thickness=2)
#     return img
#
#
# # Initializing our environment
# done = False
# frame = initialize_frame()
#
# # Check if frame creation was successful
# if frame is None:
#     print("Error: Frame initialization failed. Exiting.")
#     exit(1)
#
# state = cliffEnv.reset()[0]  # Ensure proper reset handling in newer Gym versions
#
# # For each step of the episode
# while not done:
#     # Show the current state of the environment
#     frame2 = put_agent(frame.copy(), state)  # Ensure we're copying the frame correctly
#     cv2.imshow("Cliff Walking", frame2)
#     cv2.waitKey(250)
#
#     # Select an action
#     action = int(np.random.randint(low=0, high=4, size=1))
#
#     # Take the action in the environment
#     state, reward, done, _ = cliffEnv.step(action)
#
# # Close the OpenCV window
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# # Handy functions for Visuals
# def initialize_frame():
#     width, height = 600, 200
#     img = np.ones(shape=(height, width, 3)) * 255.0  # Initialize a white image
#
#     # Debugging step: Check if the image is created correctly
#     if img is None:
#         print("Error: Image initialization failed!")
#         return None
#
#     # Return the simple blank image
#     return img
#
# # Initializing our environment
# frame = initialize_frame()
#
# # Check if frame creation was successful
# if frame is None:
#     print("Error: Frame initialization failed. Exiting.")
#     exit(1)
#
# # Show the blank frame to confirm OpenCV is working
# cv2.imshow("Blank Frame", frame)
# cv2.waitKey(2500)  # Display the frame for 2.5 seconds
#
# # Close the OpenCV window
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# # Handy functions for Visuals
# def initialize_frame():
#     width, height = 600, 200
#     img = np.ones(shape=(height, width, 3)) * 255.0  # Initialize a white image
#
#     # Check if the image is created correctly
#     if img is None:
#         print("Error: Image initialization failed!")
#         return None
#
#     # Return the simple blank image
#     return img
#
# # Initializing our environment
# frame = initialize_frame()
#
# # Check if frame creation was successful
# if frame is None:
#     print("Error: Frame initialization failed. Exiting.")
#     exit(1)
#
# # Show the blank frame to confirm OpenCV is working
# cv2.imshow("Blank Frame", frame)
#
# # Wait until the user presses a key to close the window
# cv2.waitKey(0)
#
# # Close the OpenCV window
# cv2.destroyAllWindows()

#
# import cv2
# import numpy as np
#
# # Create a blank image
# img = np.ones((300, 300, 3)) * 255  # White image
#
# # Draw a simple rectangle
# cv2.rectangle(img, (50, 50), (250, 250), (0, 0, 255), 2)
#
# # Show the image
# cv2.imshow('Test Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# # Create a simple image
# img = np.ones((300, 300, 3), dtype=np.uint8) * 255  # White image
# cv2.putText(img, "Hello OpenCV", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#
# # Display the image
# cv2.imshow("Test Image", img)
# cv2.waitKey(0)  # Wait until a key is pressed
# cv2.destroyAllWindows()  # Close the window
