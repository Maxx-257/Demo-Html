"""Practical 15: Simple Streamlit face-mask detection demo."""
from pathlib import Path
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).parent

# This is a lightweight demo: Haar Cascade detects the face and
# the lower-half color is used only to demonstrate mask/no-mask output.
def detect_mask(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(gray, 1.1, 5)

    for x, y, w, h in faces:
        face = frame[y:y+h, x:x+w]
        lower = face[h//2:, :]
        saturation = cv2.cvtColor(lower, cv2.COLOR_BGR2HSV)[:, :, 1].mean()
        label = "Mask" if saturation > 70 else "No Mask"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y-8), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    return frame, len(faces)

try:
    import streamlit as st
    running_streamlit = st.runtime.exists()
except Exception:
    running_streamlit = False

if running_streamlit:
    st.title("Face Mask Detector")
    photo = st.camera_input("Take a photo")
    if photo:
        data = np.frombuffer(photo.getvalue(), np.uint8)
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
        result, count = detect_mask(frame)
        st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption=f"Faces: {count}")
else:
    frame = cv2.imread(str(BASE / "assets" / "astronaut.jpg"))
    result, count = detect_mask(frame)
    cv2.imwrite(str(BASE / "output_face_mask_demo.jpg"), result)
    print("Faces detected:", count)
    print("For Streamlit run: streamlit run practical_15_streamlit_face_mask.py")

    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("Face Mask Demo")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(BASE / "output_face_mask_demo_plot.png")
    if os.environ.get("DIP_TEST_MODE") != "1":
        plt.show()
    plt.close()
