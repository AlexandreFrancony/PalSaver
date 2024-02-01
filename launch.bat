@echo off

REM Get the current directory
set "CURRENT_DIR=%~dp0"

REM Navigate to the src directory
cd /d "%CURRENT_DIR%src"

REM Execute the Setup.py file
python main.py

REM Return to the original directory
cd /d "%CURRENT_DIR%"

REM Pause the script to see the output
pause
