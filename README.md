# 🤖 Robotic System for Automatic Dimensioning and Alignment

## 📝 Project Overview
This repository contains the implementation of a robotic system designed for automatic dimensioning of mechanical parts during the assembly process. The system can measure part dimensions, rotate the platform, and align parts for seamless integration. By automating this process, the system eliminates manual measurements and significantly improves efficiency and precision.

## ⚙️ System Components
The robotic system uses the following key components:
- **ESP32 Development Board:** Provides real-time control and manages Wi-Fi communication.
- **OpenCV:** Performs image processing to detect part boundaries and calculate key dimensions.
- **Python:** Facilitates communication between the host machine and the ESP32 through HTTP requests.

### **Component Images**
**Rotating Plate Close-Up**
![rotating plate close up](https://drive.google.com/uc?export=view&id=1RiuAv-psCIWjgl-IF6OugsDXSOn8GrVk)
- **Description:** The rotating platform ensures precise alignment and placement of parts during the assembly process, driven by a stepper motor for accurate rotational control.

**Webcam Top View**
![web cam top view](https://drive.google.com/uc?export=view&id=1jasVUBIwGUUQAcynUYVpZrb-sE6_ws1O)
- **Description:** The top-down view captured by the webcam assists the OpenCV module in detecting part boundaries and computing key dimensions.

## 📂 Project Structure
The project is organized into directories that group related files for rotation tracking and web server communication.

```
/project-root
|-- rotation-tracking-py/   # Python scripts for rotation tracking and communication
|   |-- rotation-tracking.py
|   |-- result.txt
|   |-- server.py
|
|-- src/                    # ESP32 firmware source code
    |-- main.cpp
```

### **Directory Details**

#### **📁 rotation-tracking-py/**
This directory contains Python scripts that manage the tracking and communication processes.

- **`rotation-tracking.py`**:
  - **Purpose:** Detects and tracks the rotation angle of a mechanical part based on user-defined points.
  - **Key Features:**
    - Displays the image and captures mouse click points to define angles.
    - Calculates the angle between three points and writes the result to `result.txt`.

- **`result.txt`**:
  - **Purpose:** Stores the computed angle values for the corresponding part.

- **`server.py`**:
  - **Purpose:** Sends the computed angles to the ESP32 web server using HTTP POST requests.
  - **Endpoint:** Sends requests to `http://192.168.4.1/endpoint` (default soft AP IP address of the ESP32).

#### **📁 src/**
Contains the ESP32 firmware source code for handling incoming HTTP requests.

- **`main.cpp`**:
  - **Purpose:** Implements an asynchronous web server on the ESP32.
  - **Key Functions:**
    - **`setup()`**: Configures the ESP32 as a Wi-Fi Access Point and initializes the async web server.
    - **`loop()`**: Continuously monitors and prints received angle values for real-time observation.

## 🚀 How to Run the System
1. **Setup the ESP32:**
   - Flash the ESP32 with `src/main.cpp` using PlatformIO.
   - Set the desired Wi-Fi SSID and password in the source code.
2. **Run the Python Script:**
   - Install dependencies: `pip install opencv-python requests`.
   - Run `rotation-tracking.py` to capture angles.
   - Run `server.py` to send the angle to the ESP32.
3. **Operation:**
   - Interact with the displayed image to mark key points.
   - The computed angle is sent to the ESP32, which logs the value.

## 🛠️ Purpose and Applications
This system enhances accuracy and reliability during the assembly process, making it ideal for:
- **Manufacturing Lines:** Where part orientation and sizing are critical.
- **Quality Control:** Automates and standardizes measurement tasks.

## 📚 References
- [ESPAsyncWebServer Documentation](https://github.com/me-no-dev/ESPAsyncWebServer)

---
Let me know if you need any additional information or modifications!

