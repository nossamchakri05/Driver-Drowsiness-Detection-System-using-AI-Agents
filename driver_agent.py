
from mesa import Agent
import cv2
import dlib
import numpy as np
from imutils import face_utils
import pygame


pygame.mixer.init()

class DriverAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.sleep = 0
        self.drowsy = 0
        self.active = 0
        self.status = ""
        self.color = (0, 0, 0)
        self.alert_playing = False

    def compute(self, ptA, ptB):
        dist = np.linalg.norm(ptA - ptB)
        return dist

    def blinked(self, a, b, c, d, e, f):
        up = self.compute(b, d) + self.compute(c, e)
        down = self.compute(a, f)
        ratio = up / (2.0 * down)

        if ratio > 0.25:
            return 2
        elif 0.21 < ratio <= 0.25:
            return 1
        else:
            return 0

    def step(self):
        frame = self.model.get_frame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.model.detector(gray)

        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            face_frame = frame.copy()
            cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            landmarks = self.model.predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            left_blink = self.blinked(landmarks[36], landmarks[37],
                                      landmarks[38], landmarks[41], landmarks[40], landmarks[39])
            right_blink = self.blinked(landmarks[42], landmarks[43],
                                       landmarks[44], landmarks[47], landmarks[46], landmarks[45])

            if (left_blink == 0 or right_blink == 0):
                self.sleep += 1
                self.drowsy = 0
                self.active = 0
                if (self.sleep > 6):
                    self.status = "SLEEPING !!!"
                    self.color = (255, 0, 0)
                    if not self.alert_playing:
                        self.model.alert_agent.play_alert()
                        self.alert_playing = True
            elif (left_blink == 1 or right_blink == 1):
                self.sleep = 0
                self.active = 0
                self.drowsy += 1
                if (self.drowsy > 6):
                    self.status = "Drowsy !"
                    self.color = (0, 0, 255)
                    if not self.alert_playing:
                        self.model.alert_agent.play_alert()
                        self.alert_playing = True
            else:
                self.drowsy = 0
                self.sleep = 0
                self.active += 1
                if (self.active > 6):
                    self.status = "Active :)"
                    self.color = (0, 255, 0)
                    if self.alert_playing:
                        self.model.alert_agent.stop_alert()
                        self.alert_playing = False

            cv2.putText(frame, self.status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, self.color, 3)

            for n in range(0, 68):
                (x, y) = landmarks[n]
                cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

            cv2.imshow("Result of detector", face_frame)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            self.model.running = False
