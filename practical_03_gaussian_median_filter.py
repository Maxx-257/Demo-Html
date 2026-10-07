"""Practical 3: Gaussian and Median filtering to remove noise."""
from pathlib import Path
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
img = cv2.imread(str(BASE / "assets" / "astronaut.jpg"))
if img is None:
    raise SystemExit("Image not found")

# Add salt-and-pepper noise for demonstration
noisy = img.copy()
rng = np.random.default_rng(10)
for _ in range(5000):
    y = rng.integers(0, img.shape[0])
    x = rng.integers(0, img.shape[1])
    noisy[y, x] = 0 if rng.random() < 0.5 else 255

gaussian = cv2.GaussianBlur(noisy, (5, 5), 0)
median = cv2.medianBlur(noisy, 5)

cv2.imwrite(str(BASE / "output_noisy.jpg"), noisy)
cv2.imwrite(str(BASE / "output_gaussian.jpg"), gaussian)
cv2.imwrite(str(BASE / "output_median.jpg"), median)

plt.figure(figsize=(10, 4))
for i, (image, title) in enumerate([(noisy, "Noisy"), (gaussian, "Gaussian"), (median, "Median")], 1):
    plt.subplot(1, 3, i)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_denoising_comparison.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Gaussian and Median filtering completed.")
