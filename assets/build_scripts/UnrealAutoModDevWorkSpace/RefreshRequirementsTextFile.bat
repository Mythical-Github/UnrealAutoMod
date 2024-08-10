@echo off

cd /d "%~dp0"

set "base_dir=%~dp0UnrealAutoMod"

pip install uv

if not exist "%base_dir%" (
    git clone https://github.com/Mythical-Github/UnrealAutoMod.git "%base_dir%"
)

cd "%base_dir%"

set "c_one=uv pip install git+https://github.com/Mythical-Github/ue_dev_py_utils.git"
set "c_two=uv pip install git+https://github.com/Mythical-Github/log_py.git"
set "c_three=uv pip install git+https://github.com/Mythical-Github/cli_py.git"
set "c_four=uv pip install git+https://github.com/Mythical-Github/ue_dev_py_utils.git"
set "c_five=uv pip install git+https://github.com/Mythical-Github/win_man_py.git"
set "c_six=uv pip freeze | uv pip compile - -o requirements.txt"

uv venv
.venv\Scripts\activate && %c_one% && %c_two% && %c_three% && %c_four% && %c_five% && %c_six% && pause

pause

exit /b 0
