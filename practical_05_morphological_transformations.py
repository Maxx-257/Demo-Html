"""Practical 5: Morphological transformations."""
from pathlib import Path
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
img = cv2.imread(str(BASE / "assets" / "morphology_text_photo.png"), cv2.IMREAD_GRAYSCALE)

if img is None:
    raise SystemExit("Image not found")

# Convert the text image into a binary image
binary = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV, 31, 11
)

kernel = np.ones((3, 3), np.uint8)

erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

images = [img, binary, erosion, dilation, opening, closing]
titles = [
    "Original Photo", "Binary",
    "Erosion - thinner text", "Dilation - thicker text",
    "Opening - removes small noise", "Closing - fills small gaps"
]

plt.figure(figsize=(12, 7))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i], fontsize=10)
    plt.axis("off")

plt.tight_layout()
plt.savefig(BASE / "output_morphology.png", dpi=130)
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Morphological transformations completed.")
