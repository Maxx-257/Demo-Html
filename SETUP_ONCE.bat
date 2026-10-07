@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title DIP Practical Setup

echo ============================================================
echo DIGITAL IMAGE PROCESSING - ONE TIME WINDOWS SETUP
echo ============================================================
echo.

set "PY="
for %%V in (3.12 3.11 3.10 3.13) do (
    if not defined PY (
        py -%%V --version >nul 2>&1
        if not errorlevel 1 set "PY=py -%%V"
    )
)
if not defined PY (
    python --version >nul 2>&1
    if not errorlevel 1 set "PY=python"
)

if not defined PY (
    echo [ERROR] Python was not found on this PC.
    echo Install Python 3.10, 3.11 or 3.12 and tick "Add Python to PATH".
    pause
    exit /b 1
)

echo [1/4] Python found:
%PY% --version

echo.
if not exist ".venv\Scripts\python.exe" (
    echo [2/4] Creating .venv ...
    %PY% -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Could not create .venv.
        pause
        exit /b 1
    )
) else (
    echo [2/4] Existing .venv found - keeping it.
)

set "VPY=%CD%\.venv\Scripts\python.exe"
echo.
echo [3/4] Upgrading pip ...
"%VPY%" -m pip install --upgrade pip
if errorlevel 1 echo [WARNING] pip upgrade failed; continuing with the installed pip.

echo.
echo [4/4] Installing the stable practical packages ...
"%VPY%" -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ERROR] Package installation did not finish successfully.
    echo Check the internet connection and run SETUP_ONCE.bat again.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo SETUP COMPLETE
echo ============================================================
echo VS Code is configured to use .venv automatically.
echo Close any OLD terminal and open Terminal ^> New Terminal.
echo You can now run: TEST_ALL.bat
echo.
pause
