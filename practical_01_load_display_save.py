"""Practical 1: Load, display and save an image using OpenCV and Pillow."""
from pathlib import Path
import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
path = BASE / "assets" / "astronaut.jpg"

img = cv2.imread(str(path))
if img is None:
    raise SystemExit("Image not found")

cv2.imwrite(str(BASE / "output_opencv.jpg"), img)
Image.open(path).save(BASE / "output_pillow.png")

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Loaded Image")
plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_display.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Image loaded and saved successfully.")
