@echo off

cd %~dp0

%CD%/cleanup.py
%CD%/build.py
%CD%/make_release.py
%CD%/zip_release.py
%CD%/cleanup.py

exit /b