@echo off
setlocal

set "script_dir=%~dp0"
set "backup_dir=%script_dir%backup"
set "zip_url=https://github.com/Mythical-Github/unreal_auto_mod/releases/latest/download/unreal_auto_mod.zip"
set "zip_file=%script_dir%unreal_auto_mod.zip"

if exist "%backup_dir%" (
    echo Renaming existing backup directory to backup.bak
    ren "%backup_dir%" "backup.bak"
)

echo Creating new backup directory
mkdir "%backup_dir%"

echo Backing up files and directories to backup directory...
for /f "delims=" %%F in ('dir /b /a-d "%script_dir%"') do (
    if /I not "%%~nxF"=="%~nx0" (
        move "%%F" "%backup_dir%"
    )
)
for /d %%D in ("%script_dir%*") do (
    if /I not "%%~nxD"=="backup" (
        move "%%D" "%backup_dir%"
    )
)

echo Downloading update from %zip_url%
powershell -Command "(New-Object Net.WebClient).DownloadFile('%zip_url%', '%zip_file%')"

echo Extracting files...
powershell -Command "Expand-Archive -Path '%zip_file%' -DestinationPath '%script_dir%' -Force"

echo Deleting downloaded zip file...
del "%zip_file%"

echo Update complete.
endlocal
exit
