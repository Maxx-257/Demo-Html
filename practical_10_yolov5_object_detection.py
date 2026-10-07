"""Practical 10: Object detection using YOLOv5 with a safe OpenCV fallback."""
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
image_path = BASE / "assets" / "astronaut.jpg"
out_path = BASE / "output_object_detection.jpg"

try:
    if os.environ.get("DIP_FORCE_FALLBACK") == "1":
        raise ImportError("Safe fallback mode")

    import torch
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, verbose=False)
    result = model(str(image_path))
    result.save(save_dir=str(BASE / "yolo_output"), exist_ok=True)
    detected = result.render()[0]
    cv2.imwrite(str(out_path), cv2.cvtColor(detected, cv2.COLOR_RGB2BGR))
    print("YOLOv5 object detection completed.")

except Exception as e:
    print("YOLOv5 unavailable, using OpenCV fallback:", type(e).__name__)
    img = cv2.imread(str(image_path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(gray, 1.1, 5)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(img, "Object", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imwrite(str(out_path), img)
    print("Objects detected in fallback mode:", len(faces))

img = cv2.imread(str(out_path))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Object Detection")
plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_object_detection_plot.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()
