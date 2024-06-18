@echo off


cd %~dp0


set exe_file="%CD%\UnrealAutoModCLI.exe"
set settings_json="%CD%\escape_the_backrooms.json"
set arg=test_mods_all
set command=%exe_file% %arg% %settings_json%


echo %command%
%command%


rem pause


exit /b