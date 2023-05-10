import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
im_name = 'uttt.mp4'
curdir = os.path.dirname(os.path.realpath(__file__))
stru = '\yy'
curdir = curdir.replace(stru[0], '/') + '/'
path = curdir + im_name
cap = cv2.VideoCapture(path)

# Define parameters for optical flow calculation
params = dict(pyr_scale=0.5, levels=3, winsize=15,
              iterations=3, poly_n=5, poly_sigma=1.2, flags=0)

# Initialize variables for optical flow calculation
prev_frame = None
speeds = []

while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    if not ret:
        # End of video
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_frame is not None:
        # Calculate the optical flow between the current and previous frames
        flow = cv2.calcOpticalFlowFarneback(prev_frame, gray, None, **params)

        # Convert the flow vectors to magnitude and angle values
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

        # Threshold the magnitude values to remove noise
        mag[mag < 5] = 0

        # Calculate the average magnitude of the remaining flow vectors
        speed = np.mean(mag)

        # Store the speed value in the list
        speeds.append(speed)

    # Update the previous frame variable
    prev_frame = gray

cap.release()

# Plot the speed values over time
plt.plot(speeds)
plt.xlabel('Frame number')
plt.ylabel('Speed (pixels/frame)')
plt.show()
