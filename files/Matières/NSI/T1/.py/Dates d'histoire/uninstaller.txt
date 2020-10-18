color 0A
echo off
cls
:start
echo Welcome to the uninstaller wizard
echo To uninstall the program enter (u), to cancel the uninstallation enter (c)
set /p uninstall=
if %uninstall%==u goto u
if %uninstall%==U goto u
if %uninstall%==c goto c
if %uninstall%==C goto c
echo Please make sure that you have only entered u or U or c or C.
echo You have entered %uninstall%.
pause
goto start

:u
REM programfiles
echo deleted the file dates d'histoire graphique.py
echo deleted the folder prog
echo deleted the file py.ico
echo deleted the file README.txt
echo deleted the file see your stats.txt
echo deleted the file starterdate.bat
echo deleted the file Stats_dates_d_histoire_Graphic_py.txt
echo deleted the file dates d'histoires
REM C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Programmes de Henry Letellier\stats
echo deleted the shortcut README.lnk
echo deleted the file See your stats.txt
echo deleted the folder stats
echo deleted the shortcut download Python.lnk
echo deleted the file startersoft.bat
echo deleted the shortcut uninstall00.bat.lnk
REM Desktop
echo deleted the file startersoft.bat-Raccourci.lnk
echo The software has been uninstalled, Hope you enjoyed using it.
pause
REM del uninstall00.bat.lnk
REM del uninstall00.bat
:c
echo Installation cancelled
echo Goodbye, see you next time.
pause