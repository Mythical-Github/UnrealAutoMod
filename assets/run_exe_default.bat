@echo off

cd /d "%~dp0"

"%~dp0\UnrealAutoModCLI.exe" "default" "default" "test_mods_all"

rem pause

exit /b
