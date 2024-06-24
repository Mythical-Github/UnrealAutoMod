@echo off

cd %~dp0

%CD%/cleanup.py
%CD%/build.py
%CD%/cleanup.py

exit /b