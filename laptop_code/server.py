import serial
import serial.tools.list_ports  # Import to list available serial ports
from flask import Flask, jsonify
import sys  # To exit the script if Arduino is not connected

# Flask app setup
app = Flask(__name__)

# Global variable to store sensor data
sensor_data = {"temperature": None, "humidity": None, "pressure": None}

def find_arduino_port():
    """Automatically find the Arduino port by scanning available ports."""
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'Arduino' in port.description:  # Description may vary based on the Arduino model
            return port.device
    return None

# Try to find the Arduino port automatically
arduino_port = find_arduino_port()

if arduino_port is None:
    print("Arduino not connected. Please check the connection.")
    sys.exit()  # Exit the script if Arduino is not connected
else:
    try:
        ser = serial.Serial(arduino_port, 9600, timeout=1)
        print(f"Connected to Arduino on {arduino_port}")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        sys.exit()  # Exit the script if there's an error opening the serial port

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sensor_data)

def read_serial_data():
    global sensor_data
    while True:
        if ser and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()  # Read data from serial
            print(line)
            # Parse data (assuming the format: "Temperature: 25.0 C, Humidity: 60.0 %, Pressure: 1013.25 hPa")
            if "Temperature" in line:
                parts = line.split(", ")
                temperature = parts[0].split(": ")[1].split(" ")[0]
                humidity = parts[1].split(": ")[1].split(" ")[0]
                pressure = parts[2].split(": ")[1].split(" ")[0]
                
                # Update the sensor_data dictionary
                sensor_data = {
                    "temperature": temperature,
                    "humidity": humidity,
                    "pressure": pressure
                }

if __name__ == '__main__':
    # Start reading data in the background if Arduino is connected
    from threading import Thread
    thread = Thread(target=read_serial_data)
    thread.daemon = True  # This ensures the thread will exit when the main program exits
    thread.start()

    # Start the Flask app to host data on localhost:500
    app.run(host='0.0.0.0', port=500)