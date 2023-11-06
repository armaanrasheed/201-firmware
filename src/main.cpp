#include <Arduino.h>
#include <ESP32Servo.h>
#include <WiFi.h>

const char* ssid = "tempNet";
const char* password = "armaan";

int pos =0;

Servo myservo;

int servoPin = 27;


void setup() {
  // put your setup code here, to run once:
  ESP32PWM::allocateTimer(0);
	ESP32PWM::allocateTimer(1);
	ESP32PWM::allocateTimer(2);
	ESP32PWM::allocateTimer(3);
	myservo.setPeriodHertz(50);  
  myservo.attach(servoPin, 500, 2400);
  Serial.begin(115200);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
		// in steps of 1 degree
		myservo.write(pos);    // tell servo to go to position in variable 'pos'
		delay(15);             // waits 15ms for the servo to reach the position
	}
	for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
		myservo.write(pos);    // tell servo to go to position in variable 'pos'
		delay(15);             // waits 15ms for the servo to reach the position
	}
}