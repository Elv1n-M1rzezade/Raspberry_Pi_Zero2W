import cv2

import time



# Initialize camera (may need to change '0' if you have multiple cameras)

cap = cv2.VideoCapture(0)



# Set resolution (adjust as needed, lower resolutions can help with FPS)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)



# Optimization: Set camera backend (V4L2 may be faster)

cap.set(cv2.CAP_PROP_BACKEND, cv2.CAP_V4L2) 



# Variables for FPS calculation

start_time = time.time()

frame_count = 0



while True:

  ret, frame = cap.read()



  if not ret:

    print("Error reading frame")

    break



  # FPS calculation

  frame_count += 1

  current_time = time.time()

  elapsed_time = current_time - start_time

  if elapsed_time >= 1: # Calculate FPS every second

    fps = frame_count / elapsed_time

    print("FPS:", fps)

    start_time = current_time

    frame_count = 0



  cv2.imshow('Camera', frame)



  if cv2.waitKey(1) == ord('q'):

    break



cap.release()

cv2.destroyAllWindows()

