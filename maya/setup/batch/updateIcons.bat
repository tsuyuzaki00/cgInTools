@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

rem set maya2020_icons=%HOMEPATH%\Documents\maya\2020\prefs\icons
set current_dir=%~dp0

cd ../icons
set source_icons=%cd%

cd ../../../../../icons
set paste_icons=%cd%

echo %source_icons%
echo %paste_icons%

rem copy %source_path% %paste_icons%

ENDLOCAL