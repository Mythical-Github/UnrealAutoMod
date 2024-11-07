@echo off

cd /d %~dp0

set "py_project_dev_tools_exe=%CD%/py_project_dev_tools.exe"

set "project_info_ini=%CD%/project_info.ini"

set "repo_url="
set "repo_name="

for /f "usebackq tokens=1,* delims==" %%A in ("%project_info_ini%") do (
    if "%%A"=="repo_url" set "repo_url=%%B"
)

if not defined repo_url echo Missing repo_url in config file && exit /b 1

for %%A in (%repo_url%) do set "repo_name=%%~nA"

if not defined repo_name echo Missing repo_name in config file && exit /b 1

set "toml=%CD%/%repo_name%/pyproject.toml"

"%py_project_dev_tools_exe%" refresh_deps "%toml%"

exit /b 0


