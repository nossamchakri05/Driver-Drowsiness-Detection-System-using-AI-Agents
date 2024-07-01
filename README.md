# Driver-Drowsiness-Detection-System-using-AI-Agents
This project is a real-time driver drowsiness detection system using MESA and OpenCV. It monitors eye blinks to assess alertness and triggers an audible alert if drowsiness is detected. Using dlib for facial landmarks and Pygame for audio alerts, it enhances driver safety by preventing fatigue-related accidents.

# Requirements
To run this project, you'll need to have the following software and libraries installed:
Python 3.6+
MESA
OpenCV
dlib
imutils
numpy
Pygame

# File Strucutre 
alert_agent.py: Defines the AlertAgent class responsible for playing and stopping alerts.
driver_agent.py: Defines the DriverAgent class responsible for detecting eye blinks and assessing alertness.
driver_alert_model.py: Defines the DriverAlertModel class that integrates the agents and handles the video capture and processing.
main.py: The entry point of the application that initializes and runs the model.

This project aims to enhance road safety by providing an effective solution for detecting driver drowsiness in real-time. Your contributions and feedback are highly appreciated!
