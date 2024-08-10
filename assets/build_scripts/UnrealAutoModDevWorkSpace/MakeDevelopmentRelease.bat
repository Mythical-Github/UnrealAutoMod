@echo off

set "UnrealAutoModDir=%~dp0UnrealAutoMod"
set "DevelopmentDirToZip=%UnrealAutoModDir%\assets\build_scripts\UnrealAutoModDevWorkSpace"
set "FinalZipLocation=%~dp0Development.zip"

cd /d "%UnrealAutoModDir%"

echo Creating zip file from %DevelopmentDirToZip% to %FinalZipLocation%
powershell -Command "Compress-Archive -Path '%DevelopmentDirToZip%' -DestinationPath '%FinalZipLocation%' -Force"

exit /b 0