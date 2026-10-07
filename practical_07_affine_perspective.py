"""Practical 7: Affine and Perspective transformations on a real photo."""
from pathlib import Path
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
img = cv2.imread(str(BASE / "assets" / "real_astronaut.jpg"))
if img is None:
    raise SystemExit("Image not found")

h, w = img.shape[:2]

src1 = np.float32([[40, 40], [w - 40, 40], [40, h - 40]])
dst1 = np.float32([[70, 80], [w - 70, 50], [100, h - 50]])
M1 = cv2.getAffineTransform(src1, dst1)
affine = cv2.warpAffine(img, M1, (w, h))

src2 = np.float32([[30, 30], [w - 30, 30], [30, h - 30], [w - 30, h - 30]])
dst2 = np.float32([[80, 20], [w - 50, 70], [40, h - 20], [w - 100, h - 60]])
M2 = cv2.getPerspectiveTransform(src2, dst2)
perspective = cv2.warpPerspective(img, M2, (w, h))

plt.figure(figsize=(11, 4))
for i, (image, title) in enumerate([(img, "Original"), (affine, "Affine"), (perspective, "Perspective")], 1):
    plt.subplot(1, 3, i)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_transformations.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Affine and Perspective transformations completed.")
