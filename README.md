User Manual for LWFS Station Setup
Made By Agnel, Fahad and Adhithyan
Local Weather Forecast System
Table of Contents
User Manual for LWFS Station Setup .......................................................................................... 1
1. Introduction................................................................................................................................. 3
2. Safety Information .................................................................................................................... 3
3. Required Components ............................................................................................................ 3
4. Hardware Connections ........................................................................................................... 3
Connecting DHT11 Sensor ....................................................................................................... 3
Connecting BMP180 Sensor ................................................................................................... 3
Connecting to PC ...................................................................................................................... 4
5. Software Setup .......................................................................................................................... 4
Setting Up Arduino Code ........................................................................................................ 4
Setting Up Laptop Code .......................................................................................................... 4
Setting Up the Website ........................................................................................................... 4
6. Running the System ................................................................................................................. 5
7. Troubleshooting ........................................................................................................................ 5
8. Support and Contact Information ....................................................................................... 5
9. Appendix ..................................................................................................................................... 5
Component Specifications .................................................................................................... 5
Local Weather Forecast System
1. Introduction
This manual provides step-by-step instructions for connecting the DHT11 and BMP180 sensors to the LWFS Station, as well as how to set up and run the associated software components. Follow these instructions carefully to ensure a successful setup. This is made by Agnel Francis Olakkengil, Fahad, Adhithyan and is made for Skill Day Project and is innovative project
2. Safety Information
• Ensure that the LWFS Station is powered off before making any connections.
• Handle all electronic components with care to avoid damage from static electricity.
• Confirm that the power supply is compatible with the components being used.
3. Required Components
• LWFS Station
• DHT11 Sensor (Temperature and Humidity)
• BMP180 Sensor (Pressure and Temperature)
• Blue Wire (USB connection to PC)
• Jumper Wires (Female-to-female or male-to-female as required)
• Breadboard (optional)
• PC or Laptop
4. Hardware Connections
Connecting DHT11 Sensor
1. Pin Configuration for DHT11:
o VCC (Pin 1): Connect to the 5V pin on the LWFS Station.
o DATA (Pin 2): Connect to a digital GPIO pin (e.g., D2).
o GND (Pin 4): Connect to the GND pin on the LWFS Station.
2. Connection Diagram:
o Use jumper wires to connect the DHT11 sensor to the LWFS Station according to the pin configuration.
Connecting BMP180 Sensor
1. Pin Configuration for BMP180:
o VCC (Pin 1): Connect to the 3.3V pin on the LWFS Station.
Local Weather Forecast System
o SDA (Pin 2): Connect to the SDA pin (e.g., A4 on Arduino).
o SCL (Pin 3): Connect to the SCL pin (e.g., A5 on Arduino).
o GND (Pin 4): Connect to the GND pin on the LWFS Station.
2. Connection Diagram:
o Use jumper wires to connect the BMP180 sensor to the LWFS Station according to the pin configuration.
Connecting to PC
1. Connect the Blue Wire:
o Plug one end of the blue wire into the USB port on the LWFS Station.
o Connect the other end to an available USB port on your PC.
5. Software Setup
The software components are organized into three main folders within the LWFS directory: arduino_code, laptop_code, and Website.
Setting Up Arduino Code
1. Navigate to the arduino_code folder.
2. Open the arduino_sensor.ino file using the Arduino IDE.
3. Verify the connections of the DHT11 and BMP180 sensors in the code.
4. Upload the code to the LWFS Station by connecting it to your PC and selecting the appropriate board and port in the Arduino IDE.
Setting Up Laptop Code
1. Navigate to the laptop_code folder.
2. Install the required dependencies:
o Open a terminal and run the command pip install -r requirements.txt to install all necessary Python libraries listed in the requirements file.
3. Run the server:
o Open a terminal in the laptop_code folder.
o Execute the command python server.py to start the server.
Setting Up the Website
1. Navigate to the Website folder.
2. Install Node.js dependencies:
o Open a terminal in the Website folder.
o Run the command npm install to install all the required packages listed in package.json.
3. Run the website:
Local Weather Forecast System
o Execute the command node server.js in the terminal to start the web server.
6. Running the System
1. Ensure all hardware connections are secure and the LWFS Station is powered on.
2. Upload the Arduino code to the LWFS Station and ensure it is running correctly.
3. Start the laptop server by executing python server.py.
4. Launch the website by executing node server.js.
5. Open a web browser and navigate to the specified URL (typically http://localhost:3000 or as indicated in your server setup) to access the website interface.
7. Troubleshooting
• No readings from sensors:
o Check that all connections are secure and correctly configured.
o Ensure the LWFS Station is powered on and that the correct ports are selected in the Arduino IDE.
• Server not running:
o Verify that all required Python libraries are installed.
o Check for any error messages in the terminal and resolve them accordingly.
• Website not loading:
o Ensure that the Node.js server is running without errors.
o Double-check the URL being used to access the website.
8. Support and Contact Information
For further assistance, please contact our support team:
• Email: support@example.com
• Phone: 1-800-555-0199
9. Appendix
Component Specifications
• DHT11 Sensor:
o Operating Voltage: 3-5V
o Temperature Range: 0-50 °C
Local Weather Forecast System
o Humidity Range: 20-90% RH
• BMP180 Sensor:
o Operating Voltage: 1.8-3.6V
o Pressure Range: 300-1100 hPa
o Temperature Range: -40 to +85 °C
Made By Agnel Francis Olakkengil For Skill Day 2024
----------------- Other Mentions Fahad, Adhithyan
