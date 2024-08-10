@echo off

set "UnrealAutoModDir=%~dp0/UnrealAutoMod"

cd /d %UnrealAutoModDir%

set "build_py=%CD%/assets/build_scripts/run_build_and_zip.py"
set "built_release_before=%CD%\assets\base\UnrealAutoMod.zip"
set "built_release_after=%~dp0UnrealAutoMod.zip"

%build_py%

if exist "%built_release_after%" (
    del /q "%built_release_after%"
)

copy /Y "%built_release_before%" "%built_release_after%"

exit /b 0
