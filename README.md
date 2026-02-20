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



