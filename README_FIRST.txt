DIGITAL IMAGE PROCESSING - ALL 15 PRACTICALS
Course: Digital Image Processing (26UBCA507)
WINDOWS / VS CODE - QUICK PRACTICAL SETUP

============================================================
FASTEST FIRST-TIME SETUP
============================================================
1. Extract the ZIP completely.
2. Open the ENTIRE extracted folder in VS Code.
3. Open Terminal -> New Terminal.
4. Run:

      SETUP_ONCE.bat

5. Wait until SETUP COMPLETE appears.
6. Close the terminal and open a new terminal once.
7. The terminal should show (.venv).

VS Code is already configured to use the project virtual environment.
You normally do NOT need to select the interpreter manually.

Optional check before the exam:

      TEST_ALL.bat

This safely checks all 15 practical files.

============================================================
HOW TO RUN A PRACTICAL
============================================================
Example:

      python practical_05_morphological_transformations.py

You can also open the file and choose:
Run Python File in Terminal

Avoid the Code Runner extension's "Run Code" option because it may use
the wrong Python interpreter.

For Practical 15 Streamlit interface:

      streamlit run practical_15_streamlit_face_mask.py

============================================================
ABOUT THE CODE
============================================================
- The code is intentionally kept at a normal TYBCA practical level.
- It uses simple variables, loops and OpenCV functions so it is easier
  to understand and explain in viva.
- It is not reduced so much that the practical concept is lost.
- Output images are saved automatically and a result window opens when
  the practical is run normally.

============================================================
REAL-LIFE IMAGES USED
============================================================
Practical 5:
  Uses a real handwritten-text photograph. This makes Erosion,
  Dilation, Opening and Closing easier to distinguish visually.

Practical 6:
  Uses a real coins photograph for contour detection.

Practical 7:
  Uses a real photograph for affine and perspective transformation.

Practical 9:
  Uses a real coffee photograph with a cropped real template.

============================================================
IMPORTANT FOR PRACTICALS 10, 11 AND 12
============================================================
These are heavy deep-learning practicals:

10 - YOLOv5 Object Detection
11 - CNN using TensorFlow/Keras on MNIST
12 - ResNet Flower Classification

The files contain the actual deep-learning code, but Torch/TensorFlow can
be large and may not be installed on every college PC.

If the required package is unavailable, the program automatically runs a
simple visual fallback instead of giving a traceback.

For the FULL versions, when you have enough time and internet, run:

      OPTIONAL_DEEP_LEARNING_SETUP.bat

This is optional. It is not required for TEST_ALL.bat.

============================================================
OTHER IMPORTANT PRACTICALS
============================================================
Practical 13:
  Uses the webcam when available. If a webcam is unavailable, it uses
  the included sample image instead.

Practical 14:
  Uses Tesseract OCR when the Tesseract desktop program is installed.
  If it is not installed, image preprocessing and visual output still run.

Practical 15:
  Can be run directly with Python for a simple demonstration or with
  Streamlit for the camera interface.

============================================================
PRACTICAL FILES
============================================================
01  Load, display and save images using OpenCV and Pillow
02  Histogram equalization on grayscale and color images
03  Gaussian and Median filtering
04  Sobel and Canny edge detection
05  Morphological transformations
06  Contour detection and analysis
07  Affine and perspective transformations
08  Haar Cascade face detection
09  Template matching
10  YOLOv5 object detection
11  CNN using TensorFlow/Keras for MNIST
12  ResNet flower classification
13  Real-time webcam processing
14  Tesseract OCR
15  Streamlit face-mask detector

============================================================
QUICK VENV CHECK
============================================================
A correct terminal normally begins with:

      (.venv)

To verify Python:

      python -c "import sys; print(sys.executable)"

The path should end with:

      .venv\Scripts\python.exe

If an old terminal does not show (.venv), close it and open
Terminal -> New Terminal.

UPDATED DEMONSTRATIONS
----------------------
Practical 5  : Clear text image shows erosion, dilation, opening and closing differences.
Practical 9  : Shows Original Image + Template to Find + Matched Result together.
Practical 11 : Shows both Actual digit and Predicted digit.
Practical 14 : Shows Original Document -> Grayscale -> Preprocessed OCR image.
