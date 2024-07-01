
import pygame
import dlib

# driver_alert_model.py

from mesa import Model
import cv2
from driver_agent import DriverAgent
from alert_agent import AlertAgent

class DriverAlertModel(Model):
    def __init__(self, video_capture):
        self.alert_sound = pygame.mixer.Sound("C:/Users/nossa/Downloads/police-siren-44068.mp3")
        self.alert_channel = pygame.mixer.Channel(0)
        self.running = True
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.cap = video_capture  # Pass the video capture object to the model

        self.driver_agent = DriverAgent(1, self)
        self.alert_agent = AlertAgent(2, self)

    def get_frame(self):
        _, frame = self.cap.read()
        return frame

    def step(self):
        self.driver_agent.step()
