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

# Send SMS
try:
    ser.write(b'AT+CMGF=1\r\n')  # Set SMS mode to text mode
    time.sleep(1)
    ser.write(b'AT+CMGS="6385663699"\r\n')  # Replace <RecipientPhoneNumber> with the recipient's phone number
    time.sleep(1)
    ser.write(b'This is a test SMS from SIM900A module.\r\n')  # SMS content
    time.sleep(1)
    ser.write(bytes([26]))  # Send Ctrl+Z to indicate the end of message
    time.sleep(1)
    print("SMS sent successfully.")
except SerialException as e:
    print("Failed to send SMS:", e)

# Close the serial connection
ser.close()
