@echo off

cd %~dp0

cd ..

taskkill /f /im "unreal_auto_mod.exe" > nul 2>&1

set exe_file="%CD%\unreal_auto_mod.exe"
set settings_json="%CD%\presets\default\settings.json"
set arg=generate_game_file_list_json
set command=%exe_file% %arg% %settings_json%

rem echo %command%
%command%

rem pause

exit /b