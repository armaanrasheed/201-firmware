#include <WiFi.h>
#include <ESPAsyncWebServer.h>

const char* ssid = "yourSSID";
const char* password = "yourPASSWORD";


AsyncWebServer server(80);
int received_value = 0;


void setup() {
  Serial.begin(9600);
  delay(1000);

  Serial.print("Setting AP (Access Point)…");
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  server.on("/endpoint", HTTP_POST, [](AsyncWebServerRequest *request){
    if (request->hasParam("value", true)) {
      received_value = request->getParam("value", true)->value().toInt();
    }
    request->send(200);
  });

  server.begin();
}

void loop() {
  // Your code here
  Serial.print("Received value: ");
  Serial.println(received_value);
  delay(1000);
}