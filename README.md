# Touchless Human–Computer Interaction System using NVIDIA Jetson Orin Nano

## Project Overview

This project presents a real-time touchless Human–Computer Interaction (HCI) system implemented on the NVIDIA Jetson Orin Nano Developer Kit. The system detects hand gestures from a live webcam feed using MediaPipe’s pre-trained hand landmark detection model and translates them into media control commands for applications such as VLC Media Player and Spotify.

The primary objective of this work is to demonstrate an edge-based gesture recognition system capable of replacing conventional keyboard-based media interaction with intuitive hand gestures, while maintaining low latency and real-time performance on embedded hardware.

---

## Objectives

- Implement real-time hand detection and tracking using MediaPipe.
- Extract and analyze 21 hand landmark keypoints.
- Classify gestures using rule-based geometric logic.
- Map recognized gestures to media control commands.
- Deploy and optimize the system for the NVIDIA Jetson Orin Nano platform.

---

## Hardware Components

- NVIDIA Jetson Orin Nano Developer Kit  
- USB Webcam  
- HDMI Monitor  
- Keyboard and Mouse  
- Ubuntu 22.04 (JetPack Environment)

---

## Software Stack

- Python 3.10  
- OpenCV  
- MediaPipe  
- TensorFlow Lite (backend used by MediaPipe)  
- pynput (keyboard emulation)  
- VLC Media Player / Spotify  

---

## System Architecture

The system follows a modular architecture to ensure clarity and maintainability:

Webcam  
→ MediaPipe Palm Detection  
→ Hand Landmark Extraction (21 Keypoints)  
→ Finger State Analysis  
→ Rule-Based Gesture Classification  
→ Keyboard Emulation  
→ Media Player Control  

Each module is implemented independently to improve scalability and debugging efficiency.

---

## Supported Gestures and Actions

| Gesture        | Description                          | Media Action     |
|---------------|--------------------------------------|------------------|
| Fist          | All fingers folded                   | Play / Pause     |
| Thumb Up      | Only thumb extended                  | Volume Up        |
| Pinky         | Only pinky extended                  | Volume Down      |
| Two Fingers   | Index and middle extended            | Next Track       |
| Palm          | All fingers extended                 | Stop             |

---

## Project Structure

```
Touchless-HCI-Jetson-Orin-Nano/
│
├── main.py
│   Integrates all modules and runs the complete gesture-controlled system.
│
├── camera_module.py
│   Handles webcam input and extracts 21 hand landmarks using MediaPipe.
│
├── gesture_logic.py
│   Implements rule-based gesture classification using finger state analysis.
│
├── media_control.py
│   Sends keyboard commands to control VLC / Spotify.
│
├── gesture_debug.py
│   Standalone script for testing gesture detection and visualization.
│
├── requirements.txt
│   Lists all Python dependencies required to run the project.
│
├── .gitignore
│   Specifies files and directories ignored by Git.
│
└── README.md
    Project documentation.
```

## Optimization Techniques

To ensure stable real-time performance on embedded hardware, the following optimization strategies were implemented:

- Reduced frame resolution (640 × 480) to improve processing speed.
- Limited detection to a single hand to reduce computational overhead.
- Implemented a cooldown mechanism to prevent repeated command triggering.
- Adopted lightweight rule-based gesture classification instead of training a custom deep learning model.
- Utilized TensorFlow Lite optimized inference backend for efficient execution on Jetson hardware.

---

## Results

The system successfully achieves real-time gesture recognition on the NVIDIA Jetson Orin Nano with minimal latency. Hand landmark detection remains stable under adequate lighting conditions, and gesture-to-media response time is nearly instantaneous. The modular design ensures maintainability, scalability, and ease of debugging.

---

## Challenges Encountered

- Dependency conflicts between NumPy and OpenCV versions.
- Compatibility issues between MediaPipe and updated Python libraries.
- Display limitations when running GUI applications over remote SSH sessions.
- Sensitivity of gesture recognition under varying lighting conditions.

---

## Future Scope

- Integration of a machine learning-based gesture classifier.
- Support for multi-hand gesture recognition.
- Background media control using system-level APIs.
- Integration with IoT-enabled smart environments.
- Development of customizable gesture training for personalized interaction.

---

## Authors

Ayush Hegde  
Department of Electronics and Communication Engineering  
RV College of Engineering  

Nishaanth KS  
Department of Electronics and Communication Engineering  
RV College of Engineering  

Peta Sai Sri Harshith  
Department of Electronics and Telecommunication Engineering  
RV College of Engineering  

---

## License

This project is developed for academic and educational purposes.


