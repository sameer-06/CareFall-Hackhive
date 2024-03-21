import cv2
import numpy as np
## numpy importing 
from tensorflow.keras.models import load_model
from serial import Serial, SerialException
import time
from one.api import ONE
# Define the serial port and baud rate
serial_port = '/dev/ttyS0'  # Assuming the SIM900A module is connected to the GPIO serial port
baud_rate = 9600
# Initialize the serial connection
try:
    ser = Serial(serial_port, baud_rate, timeout=1)
    print("Serial port opened successfully.")
except SerialException as e:
    print("Failed to open serial port:", e)
    exit()
# Send AT command to check module response
ser.write(b'AT\r\n')
time.sleep(1)  # Wait for module to respond

# Read the response
response = ser.readlines()
for line in response:
    print(line.strip())


# Load the saved model
saved_model_path = 'model.h5'
model = load_model(saved_model_path)

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Check frame dimensions and format
    if frame is None or frame.shape[0] <= 0 or frame.shape[1] <= 0:
        print("Error: Invalid frame dimensions")
        continue

    # Preprocess the frame
    frame_preprocessed = cv2.resize(frame, (150, 150))  # Resize to match model input size
    frame_preprocessed = cv2.cvtColor(frame_preprocessed, cv2.COLOR_BGR2RGB)  # Convert to RGB
    frame_preprocessed = frame_preprocessed / 255.0  # Rescale pixel values to [0, 1]
    frame_preprocessed = np.expand_dims(frame_preprocessed, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(frame_preprocessed)

    # Display prediction
    if prediction[0][0] > 0.5:
        cv2.putText(frame, "Falling", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # Send SMS
        try:
            ser.write(b'AT+CMGF=1\r\n')  # Set SMS mode to text mode
            time.sleep(1)
            ser.write(b'AT+CMGS="6385663699"\r\n')  # Replace <RecipientPhoneNumber> with the recipient's phone number
            time.sleep(1)
            ser.write(b'patient is falling!!!!!!\r\n')  # SMS content
            time.sleep(1)
            ser.write(bytes([26]))  # Send Ctrl+Z to indicate the end of message
            time.sleep(1)
            print("SMS sent successfully.")
        except SerialException as e:
            print("Failed to send SMS:", e)
    else:
        cv2.putText(frame, "Not Falling", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Convert frame back to BGR for displaying
    frame_display = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Display the frame
    cv2.imshow('Live Detection', frame_display)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
ser.close()
# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
