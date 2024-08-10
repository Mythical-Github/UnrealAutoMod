@echo off

if not exist  "%~dp0/UnrealAutoMod" (
     "%~dp0/UnrealAutoModDevSetup.bat"
)

cd /d "%~dp0/UnrealAutoMod"

set "json=%CD%\assets\base\default\settings.json"

.venv\Scripts\activate && uv run "%CD%/src/unreal_auto_mod/__main__.py" %json% test_mods_all

exit /b 0
