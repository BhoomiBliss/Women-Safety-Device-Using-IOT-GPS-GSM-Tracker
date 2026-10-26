# Raspberry Pi Emergency Alert Prototype

An academic group project exploring an IoT alert workflow with Raspberry Pi, GPS, GSM, a panic-button trigger, and a voice trigger. The documented flow captures a location and sends an alert when a trigger is activated.

> **Safety note:** This is an educational prototype. It is not a tested or guaranteed personal-safety service. Do not rely on it as an emergency response system. Hardware, network coverage, power, and delivery services can fail.

## Project scope

The repository documents these prototype components:

- Raspberry Pi controller and camera
- GPS and GSM modules for location and SMS workflows
- Panic button and voice-trigger input
- Python application with serial, camera, speech, and cloud-related dependencies

The README also describes email and cloud logging. Confirm which integrations work with the current hardware and configuration before presenting them as completed.

## Hardware

The documented build uses a Raspberry Pi, compatible GPS/GSM modules, camera, panic button, power source, and optional sensors. Module compatibility and wiring depend on the actual hardware revision.

## Setup on the Raspberry Pi

The repository includes a Python dependency file and documents `main.py` as its entry point. On the configured Raspberry Pi OS installation:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

Several dependencies require Raspberry Pi hardware or system packages. Review the source and configure local service credentials before running; never commit credentials or real location data. These commands have not been run as part of this README update.

## Project type

Collaborative academic prototype. The previous README listed student registration numbers; those identifiers are removed from the current README. Confirm team attribution with collaborators before publishing names or claiming individual ownership.
