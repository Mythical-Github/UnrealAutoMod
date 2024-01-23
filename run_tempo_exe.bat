@echo off
setlocal enabledelayedexpansion

cd "%~dp0\src"

set "game_name=the_baby_in_yellow_steam"
set "preset_name=biy_mythical"
set "script_arg_index=7"

set _=set "script_args

%_%[0]=run_ide"
%_%[1]=run_fmodel"
%_%[2]=run_blender"
%_%[3]=open_game_dir"
%_%[4]=open_uproject_dir"
%_%[5]=open_downloads_dir"
%_%[6]=test_mods_cooked"
%_%[7]=test_mods_paks"
%_%[8]=test_mods_both"
%_%[9]=run_game"

set script_arg=!script_args[%script_arg_index%]!

set "command=Tempo.exe %game_name% %preset_name% %script_arg%"

%command%

rem pause

exit /b