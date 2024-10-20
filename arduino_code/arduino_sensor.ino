#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <Adafruit_BMP085_U.h>

// DHT11 Configuration
#define DHTPIN 2        // Pin where the DHT11 data pin is connected
#define DHTTYPE DHT11   // DHT 11 sensor type
DHT dht(DHTPIN, DHTTYPE);  // Initialize DHT11 sensor

// BMP180 Configuration (I2C sensor)
Adafruit_BMP085_Unified bmp = Adafruit_BMP085_Unified();

void setup() {
  // Start serial communication for debugging and sending data
  Serial.begin(9600);
  
  // Initialize the DHT11 sensor
  dht.begin();

  // Initialize the BMP180 sensor and check if it's connected
  if (!bmp.begin()) {
    Serial.println("Could not find a valid BMP180 sensor, check wiring!");
    while (1); // Halt if BMP180 is not found
  }
}

void loop() {
  // Reading DHT11 sensor (Temperature in Celsius and Humidity)
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Reading BMP180 sensor (Pressure in hPa)
  sensors_event_t event;
  bmp.getEvent(&event);
  float pressure = event.pressure; // Pressure in hPa

  // Check if any reads failed and print an error if so
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT11 sensor!");
  }
  
  if (isnan(pressure)) {
    Serial.println("Failed to read from BMP180 sensor!");
  }

  // Only send data if both sensors provide valid readings
  if (!isnan(humidity) && !isnan(temperature) && !isnan(pressure)) {
    // Prepare the data for sending over serial to the laptop
    String data = "Temperature: " + String(temperature) + " C, ";
    data += "Humidity: " + String(humidity) + " %, ";
    data += "Pressure: " + String(pressure) + " hPa";
    
    // Send the data over serial
    Serial.println(data);
  }

  // Wait for 2 seconds before the next loop (sensor reading)
  delay(2000);
}
