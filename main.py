# main.py

import cv2
from driver_alert_model import DriverAlertModel

cap = cv2.VideoCapture(0)
model = DriverAlertModel(video_capture=cap)

while model.running:
    model.step()

cap.release()
cv2.destroyAllWindows()
