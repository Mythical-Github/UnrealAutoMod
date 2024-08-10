@echo off

cd "%~dp0/UnrealAutoMod"

setlocal

set /p desc=Enter commit description: 

git status --porcelain >nul 2>&1
if %errorlevel% neq 0 (
    echo No changes detected or not in a Git repository.
    exit /b 1
)

git checkout dev
if %errorlevel% neq 0 (
    echo Failed to switch to the dev branch.
    exit /b 1
)

git add .

git commit -m "%desc%"
if %errorlevel% neq 0 (
    echo Commit failed.
    exit /b 1
)

git push origin dev
if %errorlevel% neq 0 (
    echo Push failed.
    exit /b 1
)

endlocal
