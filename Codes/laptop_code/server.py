import serial
import serial.tools.list_ports
from flask import Flask, jsonify
import sys
from threading import Thread, Lock

# Flask app setup
app = Flask(__name__)

# Global variable to store sensor data and a lock for thread safety
sensor_data = {"temperature": None, "humidity": None, "pressure": None}
data_lock = Lock()

# Specify the Arduino port directly
arduino_port = 'COM6'

try:
    ser = serial.Serial(arduino_port, 9600, timeout=1)
    print(f"Connected to Arduino on {arduino_port}")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    sys.exit()

@app.route('/data', methods=['GET'])
def get_data():
    """Return the sensor data as JSON."""
    with data_lock:  # Ensure thread safety
        return jsonify(sensor_data)

def read_serial_data():
    """Continuously read data from the Arduino serial port."""
    global sensor_data
    while True:
        if ser and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(line)
            if "Temperature" in line:  # Check for valid temperature data
                parts = line.split(", ")
                try:
                    temperature = parts[0].split(": ")[1].split(" ")[0]
                    humidity = parts[1].split(": ")[1].split(" ")[0]
                    pressure = parts[2].split(": ")[1].split(" ")[0]
                    
                    # Update the sensor_data dictionary with a lock
                    with data_lock:
                        sensor_data = {
                            "temperature": temperature,
                            "humidity": humidity,
                            "pressure": pressure
                        }
                except IndexError:
                    print("Error parsing sensor data.")

if __name__ == '__main__':
    # Start a thread to read serial data
    thread = Thread(target=read_serial_data)
    thread.daemon = True
    thread.start()

    try:
        # Run the Flask app
        app.run(host='0.0.0.0', port=5000)  # Ensure the port is set to 5000
    finally:
        ser.close()  # Ensure the serial connection is closed
