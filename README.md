# 🌱 Greenhouse Monitor & Control System  
**ESP32 + Raspberry Pi + MQTT + AWS IoT**

A complete automation platform for hydroponic greenhouse environments, enabling environmental sensing, device control, remote monitoring, and data analytics.

## ✅ Overview

This project provides a full greenhouse monitoring and automation solution using **ESP32 microcontrollers**, a **Raspberry Pi–based Linux MQTT server**, and optional **AWS IoT integration**.  
The system enables real-time sensing, bidirectional control, and remote access via an Android application.

## 👤 My Role
- Hardware Architecture & Design  
- ESP32 Firmware Development  
- Linux MQTT Server Development  
- System Integration & Testing  


## 🔍 Problem Statement
A customer operating a hydroponic greenhouse required:
- Automated environmental regulation  
- Watering and nutrient dosing control  
- Remote monitoring  
- Integration of multiple sensors & actuators  
- Scalable IoT platform  


## ✅ Solution
Developed an end-to-end greenhouse automation platform integrating:

### 🌡️ Sensors
- Temperature
- Humidity
- Soil Moisture
- pH 
- EC 

### ⚙️ Actuators
- Irrigation Valves
- Pumps
- Ventilation Motors
- High-Pressure Fogging System

Each sensor/actuator node is controlled via **ESP32** devices that communicate with the central **Raspberry Pi MQTT server**.

Configuration, command publishing, and remote monitoring are supported via MQTT topics, with optional AWS IoT data streaming.

An Android mobile app was developed for real-time monitoring and control.


## 🔧 Key Technologies

| Category | Tech |
|----------|------|
| MCU | ESP32 |
| Gateway | Raspberry Pi |
| Protocols | MQTT / HTTPS |
| Cloud | AWS IoT |
| Mobile | Android App |
| Firmware | Arduino C / FreeRTOS |
| Language | C/C++, Python |
