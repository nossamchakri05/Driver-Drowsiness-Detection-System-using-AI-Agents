
from mesa import Agent
import pygame

class AlertAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def play_alert(self):
        self.model.alert_channel.play(self.model.alert_sound)
        self.alert_playing = True

    def stop_alert(self):
        self.model.alert_channel.stop()
        self.alert_playing = False
