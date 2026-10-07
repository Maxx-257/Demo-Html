"""Practical 8: Face detection using Haar Cascade."""
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
img = cv2.imread(str(BASE / "assets" / "astronaut.jpg"))
if img is None:
    raise SystemExit("Image not found")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imwrite(str(BASE / "output_face_detection.jpg"), img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Haar Face Detection")
plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_face_detection_plot.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Faces detected:", len(faces))
