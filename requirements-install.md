# Installation and Setup Guide

This guide explains how to install and run the Women Safety Device Using IoT, GPS & GSM Tracker on Raspberry Pi.

---

## 1. Hardware Setup

Connect the following components to Raspberry Pi:

- GSM Module (SIM800L / SIM900A)
- GPS Module (Neo-6M)
- Pi Camera Module
- Panic Button Switch
- Bluetooth Module (HC-05 / BLE)
- Heart Rate and Temperature Sensors (optional)
- Power Supply / Battery

Ensure all connections are correct and secure.

---

## 2. Install Raspberry Pi OS

Install Raspberry Pi OS using Raspberry Pi Imager.

Enable:

- SSH
- Camera
- Serial Port
- Bluetooth

---

## 3. Install RealVNC Viewer

RealVNC is used to remotely control Raspberry Pi.

Steps:

1. Install RealVNC Viewer on your laptop
2. Connect Raspberry Pi to hotspot or WiFi
3. Open RealVNC Viewer
4. Enter Raspberry Pi IP address
5. Login using username and password

Now Raspberry Pi desktop will open remotely.

---

## 4. Connect Raspberry Pi to Hotspot

Steps:

1. Turn ON mobile hotspot
2. Connect Raspberry Pi to hotspot
3. Check IP address using:

```bash
hostname -I
