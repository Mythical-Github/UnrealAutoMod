@echo off

cd /d "%~dp0"

set "base_dir=%~dp0UnrealAutoMod"

if not exist  "%~dp0/UnrealAutoMod" (
     "%~dp0/UnrealAutoModDevSetup.bat"
)

cd "%base_dir%"

set "c_one=uv pip install git+https://github.com/Mythical-Github/ue_dev_py_utils.git"
set "c_two=uv pip install git+https://github.com/Mythical-Github/log_py.git"
set "c_three=uv pip install git+https://github.com/Mythical-Github/cli_py.git"
set "c_four=uv pip install git+https://github.com/Mythical-Github/ue_dev_py_utils.git"
set "c_five=uv pip install git+https://github.com/Mythical-Github/win_man_py.git"
set "c_six=uv pip install alive_progress"
set "c_seven=uv pip install requests"
set "c_eight=uv pip freeze | uv pip compile - -o requirements.txt"

uv venv
.venv\Scripts\activate && %c_one% && %c_two% && %c_three% && %c_four% && %c_five% && %c_six% && %c_seven% && %c_eight%

pause

exit /b 0
