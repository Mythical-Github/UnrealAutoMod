@echo off

cd %~dp0

%CD%/build.py
%CD%/cleanup.py

exit /b