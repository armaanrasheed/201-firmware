# 🛠️ Project Overview
This project consists of several components implemented for rotation tracking using an ESP32 development board, OpenCV for image processing, and Python for communication between the host machine and the ESP32 device. Below is a detailed explanation of each relevant directory and its contents.

## 📂 Directory Structure
```
/project-root
|-- rotation-tracking-py/
|-- src/
```

---

## 📁 `rotation-tracking-py/` Directory
Contains Python scripts for rotation tracking using OpenCV and communication with the ESP32 server.

### 📝 `rotation-tracking.py`
- **Dependencies:** OpenCV (`cv2`) and `math`.
- **Functionality:**
  - Reads and resizes the image.
  - Detects points via mouse clicks and calculates angles based on gradients.
  - Displays the angle on the image and writes the result to `result.txt`.

### 🔧 Key Functions:
- `mousePoints(event, x, y, flags, params)`: Captures mouse clicks and draws points.
- `gradient(pt1, pt2)`: Calculates the gradient between two points.
- `getAngle(pointsList)`: Computes the angle between three points and writes it to `result.txt`.

---

### 📄 `result.txt`
Stores the computed angle as a text value.

---

### 🌐 `server.py`
- **Dependencies:** `requests`.
- **Functionality:** Reads `result.txt` and sends the angle value to the ESP32 device using HTTP POST requests.
- **ESP32 IP:** `192.168.4.1` (default soft AP IP).

---

## 📁 `src/` Directory
Contains the main source file for the ESP32.

### 📝 `main.cpp`
- **Dependencies:** `WiFi.h`, `ESPAsyncWebServer.h`.
- **Functionality:**
  - Sets up ESP32 as a Wi-Fi Access Point (AP).
  - Listens for HTTP POST requests at `/endpoint` and reads the value.
  - Prints received values to the serial monitor.

### 🔧 Key Sections:
- **`setup()` Function:**
  - Initializes the serial communication.
  - Configures Wi-Fi Access Point.
  - Starts the Async Web Server.
- **`loop()` Function:**
  - Continuously prints the received values.

---

## 🚀 Future Improvements
- **Error Handling:** Implement exception handling in Python scripts and the ESP32 code.
- **Dynamic IP Configuration:** Avoid hardcoding the IP address.
- **Optimization:** Implement an optimized event loop in the ESP32 code.

---

## 📚 References
- [ESPAsyncWebServer Documentation](https://github.com/me-no-dev/ESPAsyncWebServer)

