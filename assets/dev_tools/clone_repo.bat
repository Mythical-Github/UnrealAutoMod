@echo off
setlocal

cd /d %~dp0

set "project_info_ini=%CD%/project_info.ini"

set "repo_url="
set "repo_branch="
set "clone_recursively="

for /f "usebackq tokens=1,* delims==" %%A in ("%project_info_ini%") do (
    if "%%A"=="repo_url" set "repo_url=%%B"
    if "%%A"=="repo_branch" set "repo_branch=%%B"
    if "%%A"=="clone_recursively" set "clone_recursively=%%B"
)

if not defined repo_url echo Missing repo_url in config file && exit /b 1
if not defined repo_branch echo Missing repo_branch in config file && exit /b 1
if not defined clone_recursively echo Missing clone_recursively in config file && exit /b 1

set "py_project_dev_tools_exe=%CD%/py_project_dev_tools.exe"

"%py_project_dev_tools_exe%" clone_repo "%repo_url%" %repo_branch% %clone_recursively% "%CD%"

endlocal
exit /b 0
