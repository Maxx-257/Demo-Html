@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "PY=.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"
set DIP_TEST_MODE=1
set DIP_FORCE_FALLBACK=1
set MPLBACKEND=Agg
set "FAIL=0"
echo ============================================================
echo TESTING ALL 15 DIP PRACTICALS IN SAFE TEST MODE
echo ============================================================
for %%F in (practical_01_load_display_save.py practical_02_histogram_equalization.py practical_03_gaussian_median_filter.py practical_04_sobel_canny.py practical_05_morphological_transformations.py practical_06_contour_analysis.py practical_07_affine_perspective.py practical_08_haar_face_detection.py practical_09_template_matching.py practical_10_yolov5_object_detection.py practical_11_cnn_mnist.py practical_12_resnet_flower_finetuning.py practical_13_webcam_processing.py practical_14_tesseract_ocr.py practical_15_streamlit_face_mask.py) do (
  echo.
  echo ---- %%F ----
  "%PY%" "%%F"
  if errorlevel 1 (
    echo [FAILED] %%F
    set "FAIL=1"
  ) else (
    echo [PASSED] %%F
  )
)
echo.
if "%FAIL%"=="0" (
  echo ALL 15 PRACTICALS PASSED SAFE TEST MODE.
) else (
  echo ONE OR MORE PRACTICALS FAILED. Scroll up to see which one.
)
pause
