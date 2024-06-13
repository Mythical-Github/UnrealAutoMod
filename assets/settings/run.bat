@echo off


cd %~dp0


set exe_file="%CD%\UnrealAutoModCLI.exe"
set settings_json="%CD%\settings.json"
set arg=test_mods_all
set command=%exe_file% %arg% %settings_json%


echo %command%
%command%


pause


exit /b