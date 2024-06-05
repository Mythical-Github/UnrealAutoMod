@echo off

cd /d "%~dp0"

"%~dp0\UnrealAutoModCLI.exe" "escape_the_backrooms" "character_mods" "test_mods_all"

pause

exit /b
