import cv2 as cv
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import time

# Load the falling detection model
falling_model = load_model('model.h5')

# Define body parts and pose pairs
BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
              "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
              ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
              ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
              ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]

# Define thresholds and model paths
args = {
    'input': 'samp.mp4',
    'thr': 0.2,
    'width': 368,
    'height': 368
}

inWidth = args['width']
inHeight = args['height']

# Initialize variables for pose estimation
prev_points = None
prev_time = time.time()

# Load the pose estimation model
net = cv.dnn.readNetFromTensorflow("graph.pb")

# Process the video
cap = cv.VideoCapture(args['input'])
while cv.waitKey(1) < 0:
    hasFrame, frame = cap.read()
    if not hasFrame:
        cv.waitKey()
        break

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        heatMap = out[0, i, :, :]
        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        points.append((int(x), int(y)) if conf > args['thr'] else None)

    if prev_points is not None:
        idRWrist = BODY_PARTS["RWrist"]
        current_rwrist = points[idRWrist]
        prev_rwrist = prev_points[idRWrist]

        if current_rwrist is not None and prev_rwrist is not None:
            displacement = np.sqrt((current_rwrist[0] - prev_rwrist[0])**2 + (current_rwrist[1] - prev_rwrist[1])**2)
            time_elapsed = time.time() - prev_time
            velocity = displacement / time_elapsed
            print("Velocity of right wrist:", velocity)

            # Load and preprocess the image for falling prediction
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # OpenCV uses BGR format
            img = cv.resize(img, (150, 150))
            img_array = img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Make prediction for falling
            prediction = falling_model.predict(img_array)

            # Check if both conditions are met
            if velocity > 1000 and prediction[0][0] > 0.5:
                print("Falling")

    prev_points = points
    prev_time = time.time()

    cv.imshow('OpenPose using OpenCV', frame)
    cv.waitKey(1)  # Add this line to wait for a key event and update the display

cap.release()
cv.destroyAllWindows()

