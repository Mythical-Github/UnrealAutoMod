@echo off
setlocal

set "script_dir=%~dp0"
set "backup_dir=%script_dir%backup"
set "backup_bak_dir=%backup_dir%.bak"
set "zip_url=https://github.com/Mythical-Github/UnrealAutoMod/releases/latest/download/UnrealAutoMod.zip"
set "zip_file=%script_dir%UnrealAutoMod.zip"
set "temp_dir=%script_dir%temp_extraction"

if exist "%backup_dir%" (
    ren "%backup_dir%" "backup.bak"
)

mkdir "%backup_dir%"

for %%F in ("%script_dir*") do (
    if /I not "%%~nxF"=="%~nx0" if /I not "%%~nxF"=="backup.bak" (
        move "%%F" "%backup_dir%"
    )
)

powershell -Command "(New-Object Net.WebClient).DownloadFile('%zip_url%', '%zip_file%')"
powershell -Command "Expand-Archive -Path '%zip_file%' -DestinationPath '%temp_dir%' -Force"
move "%temp_dir%\*" "%script_dir%"
rmdir /s /q "%temp_dir%"
del "%zip_file%"

endlocal
exit
