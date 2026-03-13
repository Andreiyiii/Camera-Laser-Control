# 🖐️ Finger-Tracking Laser 

This project combines Artificial Intelligence and Computer Vision to control a laser turret through hand gestures. The system detects the position of your finger via webcam and physically moves a laser to track it in real-time.

## Hardware Requirements

* **Microcontroller:** Arduino Uno
* **Actuators:** 2x SG90 Servo Motors (X-axis and Y-axis)
* **Laser Source:** KY-008 Laser Module (3-pin)
* **Video Source:** Webcam 
* **Misc:** Pan-Tilt bracket, jumper wires, USB cable.

## 🔌 Wiring Diagram

| Component | Arduino Pin | Description |
| :--- | :--- | :--- |
| **Servo Pan** | Pin 9 | Left - Right movement |
| **Servo Tilt** | Pin 10 | Up - Down movement |
| **Laser Module (S)** | Pin 13 | Control Signal (On/Off) |
| **VCC / +** | 5V 
| **GND / -** | GND 

## 💻 Software & Dependencies

### 1. Arduino (The Executor)
The Arduino code acts as the "muscles" of the project. It listens for commands sent via Serial (USB) and maps the received angles to the servo motors.

### 2. Python (The AI Brain)
Image processing is handled in Python using:
* `OpenCV`: For video capture and display.
* `MediaPipe`: For hand landmark detection.
* `pySerial`: For communicating with the Arduino.

## Installation & Setup

1.  **Upload Arduino Code:** Use the Arduino IDE or the VS Code Arduino extension to upload the `.ino` sketch to your board.
2.  **Python Configuration:**
    * Install the required libraries:
    ```bash
    pip install opencv-python mediapipe==0.10.21 pyserial
    ```
3.  **Launch:**
    * Check your COM port in the Arduino IDE (e.g., `COM5`).
    * Update the `PORT_ARDUINO` variable in the Python script.
    * Run the script:
    ```bash
    python src/tracker.py
    ```

