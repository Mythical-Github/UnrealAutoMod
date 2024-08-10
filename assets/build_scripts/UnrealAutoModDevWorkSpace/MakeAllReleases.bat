@echo off

cd /d %~dp0

call MakeUnrealAutoModRelease.bat
call MakeDevelopmentRelease.bat

pause

exit /b 0
