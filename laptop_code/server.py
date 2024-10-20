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

def find_arduino_port():
    """Automatically find the Arduino port by scanning available ports."""
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'Arduino' in port.description:
            return port.device
    return None

# Try to find the Arduino port automatically
arduino_port = find_arduino_port()

if arduino_port is None:
    print("Arduino not connected. Please check the connection.")
    sys.exit()
else:
    try:
        ser = serial.Serial(arduino_port, 9600, timeout=1)
        print(f"Connected to Arduino on {arduino_port}")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        sys.exit()

@app.route('/data', methods=['GET'])
def get_data():
    with data_lock:  # Ensure thread safety
        return jsonify(sensor_data)

def read_serial_data():
    global sensor_data
    while True:
        if ser and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(line)
            if "Temperature" in line:
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
    thread = Thread(target=read_serial_data)
    thread.daemon = True
    thread.start()

    try:
        app.run(host='0.0.0.0', port=500)
    finally:
        ser.close()  # Ensure the serial connection is closed
