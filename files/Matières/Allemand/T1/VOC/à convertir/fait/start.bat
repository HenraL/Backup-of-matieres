color F0 
REM 0A
echo off
cls
set file1="001 Cour d'Allemand du 02 09 2020.txt"
set file2="002 exercices d'Allemand du 02 09 2020.txt"
set file3="003 Cour d'Allemand du 09 09 2020.txt"
set file4="004 Exercice d'Allemand du 09 09 2020.txt"
set file5="005 Execice d'Allemand du 13 09 2020.txt"
set file6="006 Exercice d'Allemand du 14 09 2020.txt"
set file7="007 Cour d'Allemand du 16 09 2020.txt"
set file8="008 Expression d'Allemand du 19 09 2020.txt"
set file9="009 Cours d'Allemand du 23 09 2020.txt"
set file10="010 Execice d'Allemand sur Das Gap Jahr du 26 09 2020.txt"
set file11="011 Cours d'Allemand du 30 09 2020.txt"
set file12="012 Allemand Compréhension de L'oral du 30 09 2020.txt"
set file13="013 Exercice d'Allemand du 06 10 2020.txt"
set file14="014 Cours d'Allemand du 07 10 2020.txt"
set file15="015 Exrecice d'Allemand du 13 10 2020.txt"
set file16="016 Cour d'Allemand du 14 10 2020.txt"
set file17="017 Questions du DST d'Allemand du 07 10 2020, fait le 31 10 2020.txt"
set file18="018 Cours d'Allemand du 04 11 2020.txt"
set file19="019 Exercice d'Allemand du 07 11 2020.txt"
set file20="020 Exercices d'Allemand du 08 11 2020 Kunst und Politik.txt"
set file21="021 Cours d'Allemand du 18 11 2020.txt"
set file22="022 Exercice d'Allemand du 22 11 2020.txt"
set file23="023 Cours d'Allemand du 25 11 2020.txt"
set file24="024 Exercice d'Allemand du 29 11 2020.txt"
set file25="025 Cour d'Allemand du 02 12 2020.txt"
set file26="026 Cour d'Allemand du 07 12 2020.txt"
set file27="027 Cour d'Allemand du 09 12 2020.txt"
set file28="028 Exercice d'Allemand du 12 12 2020.txt"
set file29="029 Cours d'Allemand du 16 12 2020.txt"
set file30=""
@REM set file31="start.bat"
set files1to10=%file1%,%file2%,%file3%,%file4%,%file5%,%file6%,%file7%,%file8%,%file9%,%file10%
set files11to20=%file11%,%file12%,%file13%,%file14%,%file15%,%file16%,%file17%,%file18%,%file19%,%file20%
set files21to30=%file21%,%file22%,%file23%,%file24%,%file25%,%file26%,%file27%,%file28%,%file29%,%file30%
set files=(%files1to10%,%files11to20%,%files21to30%)
for %%i in %files% do (
    echo ouverture de %%i
    cmd/c %%i
    REM start %%i
    echo %%i ouvert
)
@REM pause