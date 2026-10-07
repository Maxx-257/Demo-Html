"""Practical 9: Template matching using a real photograph."""
from pathlib import Path
import os
import cv2
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
image = cv2.imread(str(BASE / "assets" / "real_coffee.png"))
template = cv2.imread(str(BASE / "assets" / "real_coffee_template.png"))

if image is None or template is None:
    raise SystemExit("Image or template not found")

# Find the template inside the main image
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
_, max_value, _, max_location = cv2.minMaxLoc(result)

h, w = template.shape[:2]
x, y = max_location

matched = image.copy()
cv2.rectangle(matched, (x, y), (x + w, y + h), (0, 255, 0), 4)

cv2.imwrite(str(BASE / "output_template_match.png"), matched)

# Show the main image, template and final result together
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("Template to Find")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(matched, cv2.COLOR_BGR2RGB))
plt.title("Matched Result")
plt.axis("off")

plt.tight_layout()
plt.savefig(BASE / "output_template_match_plot.png", dpi=130)
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()

print("Best match confidence:", round(float(max_value), 3))
print("Best match location:", max_location)
