"""Practical 6: Detect and analyze contours in a real image."""
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
img = cv2.imread(str(BASE / "assets" / "real_coins.png"))
if img is None:
    raise SystemExit("Image not found")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = img.copy()
count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500:
        x, y, w, h = cv2.boundingRect(contour)
        if x > 2 and y > 2 and x + w < img.shape[1] - 2 and y + h < img.shape[0] - 2:
            count += 1
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(output, str(count), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            print("Contour", count, "Area =", round(area, 2))

cv2.imwrite(str(BASE / "output_contours.png"), output)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Contour Detection")
plt.axis("off")
plt.tight_layout()
plt.savefig(BASE / "output_contour_plot.png")
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Contours detected:", count)
