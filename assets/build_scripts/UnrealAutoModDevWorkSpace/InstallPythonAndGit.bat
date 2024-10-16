@echo off
setlocal

set CURL_OPTIONS=-L --retry 3 --retry-delay 5

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found, downloading the latest version...
    
    curl %CURL_OPTIONS% https://www.python.org/ftp/python/ | findstr /r "[0-9]\.[0-9]\.[0-9]" > python_versions.txt
    for /f "tokens=*" %%A in (python_versions.txt) do set latestPythonVersion=%%A
    set latestPythonVersion=%latestPythonVersion:~0,5%

    echo Latest Python version found: %latestPythonVersion%
    
    curl %CURL_OPTIONS% -o python_installer.exe https://www.python.org/ftp/python/%latestPythonVersion%/python-%latestPythonVersion%-amd64.exe
    
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1

    timeout /t 30 >nul

    echo Python installed successfully.
) else (
    echo Python is already installed.
)

pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip not found. Installing pip...
    python -m ensurepip --upgrade
    echo Pip installed successfully.
) else (
    echo Pip is already installed.
)

echo Updating pip to the latest version...
python -m pip install --upgrade Pip

git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git not found, downloading and installing the latest version...

    curl %CURL_OPTIONS% -o git_installer.exe https://github.com/git-for-windows/git/releases/latest/download/Git-2.42.0-64-bit.exe

    git_installer.exe /VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP- /NOICONS

    timeout /t 30 >nul

    echo Git installed successfully.
) else (
    echo Git is already installed.
)

echo Python, pip, and Git installation check complete.

exit /b
