"""Practical 14: Read text from an image using Tesseract OCR."""
from pathlib import Path
import os
import shutil
import cv2
import pytesseract
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
img = cv2.imread(str(BASE / "assets" / "ocr_document_photo.png"))

if img is None:
    raise SystemExit("Image not found")

# Step 1: Convert the original image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)

# Step 2: Remove a little noise and make text black on a white background
blur = cv2.GaussianBlur(gray, (3, 3), 0)
preprocessed = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 31, 12
)

cv2.imwrite(str(BASE / "output_ocr_preprocessed.png"), preprocessed)

# Check whether the Tesseract application is installed
exe = shutil.which("tesseract")
if exe is None:
    default_path = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    if default_path.exists():
        exe = str(default_path)

if exe:
    pytesseract.pytesseract.tesseract_cmd = exe
    text = pytesseract.image_to_string(preprocessed).strip()
    print("Detected text:")
    print(text if text else "No text detected")
else:
    print("Tesseract application is not installed on this PC.")

print("Original = normal document image with uneven background.")
print("Preprocessed = cleaner black text on white background for easier OCR.")

# Display each stage so the difference is easy to understand
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("1. Original Document")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("2. Grayscale")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(preprocessed, cmap="gray")
plt.title("3. Preprocessed for OCR")
plt.axis("off")

plt.tight_layout()
plt.savefig(BASE / "output_ocr_result.png", dpi=130)
if os.environ.get("DIP_TEST_MODE") != "1":
    plt.show()
plt.close()
