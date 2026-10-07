"""Practical 4: Edge detection using Sobel and Canny operators."""
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
gray = cv2.imread(str(BASE / "assets" / "astronaut.jpg"), cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise SystemExit("Image not found")

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.convertScaleAbs(cv2.magnitude(sobel_x.astype("float32"), sobel_y.astype("float32")))
canny = cv2.Canny(gray, 100, 200)

cv2.imwrite(str(BASE / "output_sobel.jpg"), sobel)
cv2.imwrite(str(BASE / "output_canny.jpg"), canny)

plt.figure(figsize=(10, 4))
for i, (image, title) in enumerate([(gray, "Original"), (sobel, "Sobel"), (canny, "Canny")], 1):
    plt.subplot(1, 3, i)
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_edge_comparison.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Sobel and Canny edge detection completed.")
