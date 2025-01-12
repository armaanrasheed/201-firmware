# 🤖 Robotic System for Automatic Dimensioning and Alignment

## 📝 Project Description
This project centers around a robotic system designed to automatically dimension mechanical parts as part of an assembly process machine. The robot can measure the size of a part, rotate its platform, and align the part correctly for seamless integration into the assembly process. This capability eliminates the need for manual measurements and adjustments, significantly improving precision and efficiency.

## ⚙️ System Components
The system leverages an ESP32 development board for real-time control, OpenCV for image processing to accurately detect part boundaries and dimensions, and Python for communication between the host machine and the ESP32 device.

### **Rotating Plate Close-Up**
![rotating plate close up](https://drive.google.com/uc?export=view&id=1RiuAv-psCIWjgl-IF6OugsDXSOn8GrVk)
**Description:** This image shows a close-up view of the rotating platform used for mechanical alignment. The platform is fitted with a stepper motor that ensures precise rotation. The setup enables accurate placement of parts in various orientations to achieve optimal alignment during the assembly process.

### **Webcam Top View**
![web cam top view](https://drive.google.com/uc?export=view&id=1jasVUBIwGUUQAcynUYVpZrb-sE6_ws1O)
**Description:** This image provides a top-down view of the workspace as captured by the webcam used in the system. The camera plays a crucial role in the dimensioning module, where OpenCV algorithms process the captured images to detect part boundaries and calculate key dimensions such as width, height, and depth.

## 📂 Project Structure
Below is a breakdown of the key directories and their relevant files for the rotation tracking and async web server components:

### **Directory Structure:**
```
/project-root
|-- rotation-tracking-py/
|   |-- rotation-tracking.py
|   |-- result.txt
|   |-- server.py
|
|-- src/
    |-- main.cpp
```

### **📁 rotation-tracking-py/**
This directory contains Python scripts used for image-based rotation tracking and communication with the ESP32 device.

- **`rotation-tracking.py`**: 
  - **Purpose:** Tracks rotation angles based on user-defined points in an image.
  - **Key Features:** 
    - Displays points clicked by the user and computes angles.
    - Writes the computed angles to `result.txt`.
- **`result.txt`**: Stores the computed angle values.
- **`server.py`**: 
  - **Purpose:** Reads angle values from `result.txt` and sends them to the ESP32 device using HTTP POST requests.
  - **Endpoint:** The ESP32 device listens for POST requests at `http://192.168.4.1/endpoint`.

### **📁 src/**
This directory contains the ESP32 source code.

- **`main.cpp`**:
  - **Purpose:** Handles communication by setting up the ESP32 as a Wi-Fi Access Point (AP) and an async web server.
  - **Key Functions:**
    - **`setup()`**: Initializes serial communication, configures the AP, and starts the web server.
    - **`loop()`**: Continuously prints the received rotation values.

## 🛠️ Purpose and Applications
This robotic system was designed to enhance accuracy and reliability in the assembly process, making it ideal for applications where part orientation and sizing are crucial.

---
Let me know if you need further details or edits!

