@echo off

:: Change to the directory where the script is located
cd /d "%~dp0"

:: Define the base directory
set "base_dir=%~dp0UnrealAutoMod"

:: Install uv if not already installed
pip install uv

:: Remove the existing directory if it exists
if not exist "%base_dir%" (
    git clone https://github.com/Mythical-Github/UnrealAutoMod.git "%base_dir%"
)

:: Change to the base directory
cd "%base_dir%"

:: Set the run application command
set command=uv run "%base_dir%/src/unreal_auto_mod/__main__.py" test_mods_all -h

:: Create and activate the virtual environment, then install requirements, then run the application, then pause
uv venv
.venv\Scripts\activate && uv pip install -r requirements.txt && %command% && pause

pause

:: Exit the script
exit /b 0
