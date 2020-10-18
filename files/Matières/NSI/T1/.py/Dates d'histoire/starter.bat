color 0A
echo off
cls
:start
echo Quel Fichier voulez-vous exécuter?
REM dir
echo Dates d'histoires (DT)
echo.
echo Quitter (q)
set /p start=
if %start%==dt goto dt
if %start%==Dt goto dt
if %start%==dT goto dt
if %start%==DT goto dt
if %start%==q goto quit
if %start%==Q goto quit
echo assurez-vous de n'avoir entré que dt ou Dt ou dT ou DT ou q ou Q
echo vous avez entré: %start%
goto start

:dt
echo executer le programe (e), voir les statistiques (v), sortir de cette section (q)
set /p DT=
if %DT%==e goto dte
if %DT%==E goto dte
if %DT%==v goto dtv
if %DT%==V goto dtv
if %DT%==q goto dtq
if %DT%==Q goto dtq
echo assurez-vous de n'avoir entré que e ou E ou v ou V ou q ou Q
echo vous avez entré: %DT%
goto dt
:dte
cmd /C ""C:\Program Files (x86)\Python37-32\python.exe" "c:\Program Files (x86)\Programmes de Henry Letellier\dates d'histoires\prog\dates d'histoire graphique.py" "
goto dt
:dtv
start "C:\Program Files (x86)\Programmes de Henry Letellier\dates d'histoires\see your stats.txt" "
goto dt
:dtq
goto start
:quit