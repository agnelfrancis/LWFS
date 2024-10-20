@echo off
cls
echo Starting Automation Process...

:: Navigate to laptop_code folder
cd /d "%~dp0Codes\laptop_code" || (
    echo Error: Could not navigate to "LWFS\Codes\laptop_code".
    pause
    exit /b 1
)

:: Check if the Python server file exists
if not exist "server.py" (
    echo Error: server.py not found in "LWFS\Codes\laptop_code".
    pause
    exit /b 1
)

:: Check if requirements.txt exists
if not exist "requirements.txt" (
    echo Error: requirements.txt not found in "LWFS\Codes\laptop_code".
    pause
    exit /b 1
)

:: Install Python dependencies
echo Installing Python dependencies...
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Error installing Python dependencies!
    pause
    exit /b 1
)
echo Python dependencies installed successfully!

:: Start Python server and check for Arduino connection
echo Starting Python server...
python server.py
if %ERRORLEVEL% neq 0 (
    echo Error starting Python server or Arduino not connected!
    echo Python server did not start successfully, stopping the process.
    pause
    exit /b 1
)
echo Python server started successfully!

:: Navigate back to Codes folder
cd /d "%~dp0Codes\Website" || (
    echo Error: Could not navigate to "LWFS\Codes\Website".
    pause
    exit /b 1
)

:: Check if the Node.js server file exists
if not exist "server.js" (
    echo Error: server.js not found in "LWFS\Codes\Website".
    pause
    exit /b 1
)

:: Check if package.json exists
if not exist "package.json" (
    echo Error: package.json not found in "LWFS\Codes\Website".
    pause
    exit /b 1
)

:: Install Node.js dependencies
echo Installing Node.js dependencies...
npm install
if %ERRORLEVEL% neq 0 (
    echo Error installing Node.js dependencies!
    pause
    exit /b 1
)
echo Node.js dependencies installed successfully!

:: Start Node.js server
echo Starting Node.js server...
node server.js
if %ERRORLEVEL% neq 0 (
    echo Error starting Node.js server!
    pause
    exit /b 1
)
echo Node.js server started successfully!

:: All done
echo All tasks completed successfully!
pause
