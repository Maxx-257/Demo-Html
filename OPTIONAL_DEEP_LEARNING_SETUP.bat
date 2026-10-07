@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run SETUP_ONCE.bat first.
  pause
  exit /b 1
)
echo Installing optional deep-learning packages. This can take a long time.
".venv\Scripts\python.exe" -m pip install -r requirements_optional_deep_learning.txt
if errorlevel 1 (
  echo Optional installation failed. The practicals will still use their safe fallbacks.
) else (
  echo Optional deep-learning packages installed.
)
pause
