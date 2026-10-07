"""Practical 2: Histogram equalization on grayscale and color images."""
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
img = cv2.imread(str(BASE / "assets" / "astronaut.jpg"))
if img is None:
    raise SystemExit("Image not found")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_eq = cv2.equalizeHist(gray)

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
color_eq = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imwrite(str(BASE / "output_gray_equalized.jpg"), gray_eq)
cv2.imwrite(str(BASE / "output_color_equalized.jpg"), color_eq)

plt.figure(figsize=(10, 4))
for i, (image, title, cmap) in enumerate([
    (gray, "Original Gray", "gray"),
    (gray_eq, "Equalized Gray", "gray"),
    (cv2.cvtColor(color_eq, cv2.COLOR_BGR2RGB), "Equalized Color", None)
], 1):
    plt.subplot(1, 3, i)
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.savefig(BASE / "output_histogram_equalization.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Histogram equalization completed.")
