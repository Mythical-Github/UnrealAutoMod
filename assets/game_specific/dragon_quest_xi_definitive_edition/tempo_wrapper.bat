@echo off

set "mod_dir_to_pack=%1"

set "output_pak=%2"

set "script_dir=%~dp0%"

set "script=%script_dir%u4pak_dq11_v2.py"

set "mod_dir=%mod_dir_to_pack:/=\%"

cd /d "%mod_dir%"

python %script% pack %output_pak% JackGame

exit /b
