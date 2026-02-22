# Women Safety Device Using IoT, GPS & GSM Tracker

## 📌 Project Overview

The Women Safety Device Using IoT, GPS & GSM Tracker is a smart wearable safety system developed using Raspberry Pi.  
This project provides real-time emergency alerts, GPS tracking, image capture, GSM-based SMS alerts, email notifications, and health monitoring.

The system ensures quick emergency response using:

- Panic Button Trigger
- Voice Command Activation
- GPS Location Sharing
- Image Capture Evidence
- GSM SMS Alert System
- Cloud Monitoring using ThingSpeak
- Remote Monitoring using RealVNC

---


## 🚨 Problem Statement

Women safety is a major concern due to increasing crime rates.  
Most safety apps depend on smartphones, which may not be accessible during emergencies.

This project provides a wearable IoT-based safety system that works independently and sends real-time emergency alerts with location and image evidence.

---

## 🎯 Objectives

- Design a wearable IoT-based women safety device
- Enable dual emergency activation (panic button + voice command)
- Send SMS and email alerts with GPS location
- Capture image during emergency
- Monitor health parameters (heart rate, temperature)
- Upload real-time data to ThingSpeak cloud
- Ensure low-cost and real-time safety solution

---

## 🔥 Key Features

- Real-time emergency alert system
- Panic button activation
- Voice-based emergency detection
- GPS-based location tracking
- GSM SMS alert system
- Automatic image capture
- Email alert with image and location
- Health monitoring (Heart Rate, Temperature, SpO₂)
- Cloud data logging
- Remote access using RealVNC

---

## 🏗 System Architecture

Main Components:

- Raspberry Pi 4 Model B (Main Controller)
- GSM Module (SIM800L / SIM900A)
- GPS Module (Neo-6M)
- Pi Camera Module
- Panic Button
- Bluetooth Module
- Heart Rate Sensor
- Temperature Sensor
- ThingSpeak Cloud
- Gemini AI Voice Assistant

---

## 🧰 Hardware Requirements

- Raspberry Pi 4 Model B
- GSM Module (SIM800L / SIM900A)
- GPS Module (Neo-6M)
- Pi Camera Module
- Bluetooth Module (HC-05 / BLE)
- Panic Button Switch
- Heart Rate Sensor
- Temperature Sensor
- Battery Pack / Power Supply

---

## 💻 Software Requirements

- Raspberry Pi OS (Raspbian OS)
- Python 3.x
- OpenCV
- pySerial
- SpeechRecognition
- ThingSpeak API
- Google Gemini AI API
- RealVNC Viewer
- SMTP Email Service

---

## ⚙ Working Principle

The system continuously monitors emergency triggers.

When activated by:

- Panic Button  
OR  
- Voice Command ("Emergency")

The system will:

1. Capture image using Pi Camera
2. Fetch GPS location
3. Send SMS alert via GSM
4. Send Email alert with image and location
5. Upload data to ThingSpeak cloud
6. Store emergency logs

---

## 📷 Hardware Setup

![Hardware Setup](images/hardware_setup.jpg)

---

## 🔧 Installation Guide

### Step 1: Install Raspberry Pi OS

Install Raspberry Pi OS using Raspberry Pi Imager.

Enable:

- Camera
- Serial Port
- SSH
- Bluetooth

---

### Step 2: Connect Raspberry Pi using RealVNC

1. Connect Raspberry Pi to hotspot
2. Find IP address of your Raspberry Pi [hostname -I]
3. 3. Open RealVNC Viewer
4. Enter IP address
5. Login to Raspberry Pi

---

### Step 3: Install Required Libraries

pip install -r requirements.txt

---

### Step 4: Run the Project

python3 main.py

---

## 🌐 Cloud Integration

ThingSpeak cloud is used for:

- Health monitoring
- Emergency data storage
- Real-time visualization

---

## 🧪 Testing Results

The system was successfully tested for:

- Panic button emergency activation
- Voice command activation
- SMS alert delivery
- Email alert delivery
- GPS location accuracy
- Image capture
- ThingSpeak cloud upload

---

## 📱 Applications

- Women personal safety
- Elderly monitoring
- Child safety system
- Healthcare monitoring
- Smart wearable safety device
- Emergency response support

---

## 🔮 Future Scope

- Mobile application integration
- 4G / 5G communication
- Live video streaming
- Fall detection system
- AI-based automatic threat detection
- Improved battery optimization

---

## 🛠 Technologies Used

- IoT (Internet of Things)
- Raspberry Pi
- Python
- GSM Communication
- GPS Tracking
- ThingSpeak Cloud
- Gemini AI
- OpenCV

---

## 👩‍💻 Authors

Bhoomika S Shetty  
USN: 4SU22IS012  

D P Thanmayi  
USN: 4SU22IS014  

Sinchana K A  
USN: 4SU22IS046  

Yashaswini  
USN: 4SU22IS063  

Department of Information Science and Engineering  
SDM Institute of Technology, Ujire  
Affiliated to Visvesvaraya Technological University, Belagavi  

---

## 👩‍🏫 Project Guide

Ms. Shobha  
Assistant Professor  
Department of Information Science and Engineering  
SDM Institute of Technology, Ujire  

---

## 📜 License

This project is licensed under the MIT License.

---

## ✅ Conclusion

This project demonstrates a real-time IoT-based women safety system integrating Raspberry Pi, GPS, GSM, AI, and cloud technology.  
It provides reliable emergency alerts, evidence capture, and health monitoring, making it an effective wearable safety solution.

---

## 🔑 Keywords

Women Safety, IoT, Raspberry Pi, GPS, GSM, Emergency Alert, ThingSpeak, Gemini AI, Health Monitoring, Smart Wearable
