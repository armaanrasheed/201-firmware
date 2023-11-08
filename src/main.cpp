#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <WiFiClientSecure.h>

// Replace with your network credentials
const char* ssid = "aru";
const char* password = "123456789";

// Create an instance of the server
// Specify the port (default is 80)
AsyncWebServer server(80);

void setup() {
  // Start the Serial communication to send messages to the computer
  Serial.begin(9600);
  delay(10);

  // Set the ESP32 as an access point
  WiFi.softAP(ssid, password);

  // Print the IP address
  Serial.println(WiFi.softAPIP());

  // Start the server
  server.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
}