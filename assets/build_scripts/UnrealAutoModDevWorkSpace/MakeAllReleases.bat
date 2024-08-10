@echo off

cd /d %~dp0

call MakeUnrealAutoModRelease.bat

cd /d %~dp0

call MakeDevelopmentRelease.bat
