@echo off


cd %~dp0

cd ..

taskkill /f /im "unreal_auto_mod.exe" > nul 2>&1

set exe_file="%CD%\unreal_auto_mod.exe"
set settings_json="%CD%\presets\default\settings.json"
set arg=resave_packages_and_fix_up_redirectors
set command=%exe_file% %arg% %settings_json%

rem echo %command%
%command%

rem pause


exit /b