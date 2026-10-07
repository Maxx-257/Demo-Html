"""Practical 13: Capture and process webcam video using OpenCV."""
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt

BASE = Path(__file__).parent

if os.environ.get("DIP_TEST_MODE") == "1":
    cap = None
else:
    cap = cv2.VideoCapture(0)

if cap is not None and cap.isOpened():
    print("Webcam started. Press Q to stop.")
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 80, 160)
        cv2.imshow("Original", frame)
        cv2.imshow("Edges", edges)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Webcam unavailable, using sample image.")
    frame = cv2.imread(str(BASE / "assets" / "astronaut.jpg"))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 160)

    plt.figure(figsize=(9, 3))
    plt.subplot(1, 3, 1); plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)); plt.title("Original"); plt.axis("off")
    plt.subplot(1, 3, 2); plt.imshow(gray, cmap="gray"); plt.title("Gray"); plt.axis("off")
    plt.subplot(1, 3, 3); plt.imshow(edges, cmap="gray"); plt.title("Edges"); plt.axis("off")
    plt.tight_layout()
    plt.savefig(BASE / "output_webcam_fallback.png")
    if os.environ.get("DIP_TEST_MODE") != "1":
        plt.show()
    plt.close()
