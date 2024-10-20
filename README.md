# Local Weather Forecast System (LWFS) Station Setup

**Made By:** Agnel, Fahad, and Adhithyan  
**Skill Day Project**  

---

## Table of Contents
1. [Introduction](#introduction)  
2. [Safety Information](#safety-information)  
3. [Required Components](#required-components)  
4. [Hardware Connections](#hardware-connections)  
   - [Connecting DHT11 Sensor](#connecting-dht11-sensor)  
   - [Connecting BMP180 Sensor](#connecting-bmp180-sensor)  
   - [Connecting to PC](#connecting-to-pc)  
5. [Software Setup](#software-setup)  
   - [Setting Up Arduino Code](#setting-up-arduino-code)  
   - [Setting Up Laptop Code](#setting-up-laptop-code)  
   - [Setting Up the Website](#setting-up-the-website)  
6. [Running the System](#running-the-system)  
7. [Troubleshooting](#troubleshooting)  
8. [Support and Contact Information](#support-and-contact-information)  
9. [Appendix](#appendix)  

---

## Introduction
This manual provides step-by-step instructions for connecting the DHT11 and BMP180 sensors to the LWFS Station, as well as how to set up and run the associated software components. Follow these instructions carefully to ensure a successful setup.

## Safety Information
- Ensure that the LWFS Station is powered off before making any connections.
- Handle all electronic components with care to avoid damage from static electricity.
- Confirm that the power supply is compatible with the components being used.

## Required Components
- LWFS Station
- DHT11 Sensor (Temperature and Humidity)
- BMP180 Sensor (Pressure and Temperature)
- Blue Wire (USB connection to PC)
- Jumper Wires (Female-to-female or male-to-female as required)
- Breadboard (optional)
- PC or Laptop

## Hardware Connections

### Connecting DHT11 Sensor
1. **Pin Configuration for DHT11:**
   - VCC (Pin 1): Connect to the 5V pin on the LWFS Station.
   - DATA (Pin 2): Connect to a A0 (e.g., A0 on Arduino).
   - GND (Pin 4): Connect to the GND pin on the LWFS Station.
2. **Connection Diagram:**
   - Use jumper wires to connect the DHT11 sensor to the LWFS Station according to the pin configuration.

### Connecting BMP180 Sensor
1. **Pin Configuration for BMP180:**
   - VIN (Pin 1): Connect to the 3.3V pin on the LWFS Station.
   - SDA (Pin 2): Connect to the SDA pin (e.g., A4 on Arduino).
   - SCL (Pin 3): Connect to the SCL pin (e.g., A5 on Arduino).
   - GND (Pin 4): Connect to the GND pin on the LWFS Station.
2. **Connection Diagram:**
   - Use jumper wires to connect the BMP180 sensor to the LWFS Station according to the pin configuration.

### Connecting to PC
1. **Connect the Blue Wire:**
   - Plug one end of the blue wire into the USB port on the LWFS Station.
   - Connect the other end to an available USB port on your PC.

## Software Setup
The software components are organized into three main folders within the LWFS directory: **arduino_code**, **laptop_code**, and **Website**.

### Setting Up Arduino Code
1. Navigate to the **arduino_code** folder.
2. Open the `arduino_sensor.ino` file using the Arduino IDE.
3. Verify the connections of the DHT11 and BMP180 sensors in the code.
4. Upload the code to the LWFS Station by connecting it to your PC and selecting the appropriate board and port in the Arduino IDE.

### Setting Up Laptop Code
1. Navigate to the **laptop_code** folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
### Run the server:
1. Open a terminal in the laptop_code folder.
2. Execute the command:
   ```bash
   python server.py
### Setting Up the Website
1. Navigate to the Website folder.
2. Install Node.js dependencies:
3. Open a terminal in the Website folder.
4. Run the command:
   ```bash
   npm install
### Run the website:
1. Execute the command:
   ```bash
   node server.js
### Running the System
1. Ensure all hardware connections are secure and the LWFS Station is powered on.
2. Upload the Arduino code to the LWFS Station and ensure it is running correctly.
3. Start the laptop server by executing:
   ```bash
   python server.py
4. Launch the website by executing:
   ```bash
   node server.js
5. Open a web browser and navigate to the specified URL always 0.0.0.0:9000 ) to access the website interface.
### To Access From Other Devices
1. Open cmd by typing it in Search
2. There Type
   ```bash
   ipconfig
3. After that You will get some numbers, Specifically look for **IPv4** Number like this
   ```bash
   IPv4 Address. . . . . . . . . . . : 192.168.x.x
4. Then Type 192.168.x.x:9000 ( use it in another device Make Sure both is connected to same WiFi Router )
5. If everything is done properly you will get a website with readings
### No readings from sensors:
1. Check that all connections are secure and correctly configured.
2. Ensure the LWFS Station is powered on and that the correct ports are selected in the Arduino IDE.
###Server not running:
1. Verify that all required Python libraries are installed.
2. Check for any error messages in the terminal and resolve them accordingly.
### Website not loading:
1. Ensure that the Node.js server is running without errors.
2. Double-check the URL being used to access the website.
### Support and Contact Information

For further assistance, please contact our support team:
Email: agnelfrancis2007@gmail.com

## Appendix
### Component Specifications
#### DHT11 Sensor:
Operating Voltage: 3-5V
Temperature Range: 0-50 °C
Humidity Range: 20-90% RH
#### BMP180 Sensor:
Operating Voltage: 1.8-3.6V
Pressure Range: 300-1100 hPa
Temperature Range: -40 to +85 °C

### Made By Agnel Francis Olakkengil For Skill Day 2024
#### Other Mentions: Fahad, Adhithyan