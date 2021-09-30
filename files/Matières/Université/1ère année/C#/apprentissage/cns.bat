color 0A
echo off
cls
echo Entrez le nom complet du fichier … compiler:
set /p filename=
echo Entrez le nom du fichier de destination (sans l'extension):
set /p destination=
echo Compilation.
gcc -o %destination% %filename%
echo Fichier compil‚ avec succŠs sous le nom de %destination%.
echo (c) Cr‚‚ par Henry Letellier
pause
pause
echo Tentative de lancement du fichier %destination%.
%destination%.exe
echo '%destination%' a ‚t‚ lanc‚ avec succŠs.