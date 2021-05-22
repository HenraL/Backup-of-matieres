import os
def echo(word):
    print(word)
os.system("color 0A")
os.system("echo off")
os.system("cls")
def func(FUNC):
    os.system("{}".format(FUNC))
echo("This programm is intended for the people who already have some experience with the following programms")
echo("I do not suggest you continue unless you know what you are doing.")
echo()
echo("Use this program at your own risk.")
echo("The author of this program cannot be held responsible for any damage that happens on you're personal objects.")
echo()
echo("The following commands will be used in the order they apear:")
echo("- diskpart : used to enter the program")
echo("- list disk : used to show the display the names of the different disks that are connected or in you're computer")
echo("- a small question to get the name of the disk you whant to put back on foot")
echo("Please enter the index number of you're disk, (disk 0 is your primary disk, it cannot be formated so there is no point in selecting it)")
echo("- select disk %diskchoice% : used to enter the desired disk")
echo("- clean : to make sure the disk is clean")
echo("- create partition primary : creates a folder containing the necessary elements for the usb to function correctly")
echo("- a question will be asked to know if you wish to rename the device during the process (please answer by y for yes or n for no)")
echo("if n(no) is answered:")
echo("- a question will be asked to get the desired format")
echo("- format fs=%format% : the device is set to one of the specific formats below (defined by %format%)")
echo("  (1) ~ ntfs (recommended)")
echo("  (2) ~ fat")
echo("  (3) ~ fat32")
echo("  (4) ~ exfat")
echo("if y(yes) is answered:")
echo("- a question will be asked to get the desired format")
echo("- a second question will be asked to get the name you will give it")
echo("- format fs=%format% label=%nameOfDisk%: the device is set to one of the specific formats below (defined by %format%)")
echo("  (1) ~ ntfs (recommended)")
echo("  (2) ~ fat")
echo("  (3) ~ fat32")
echo("  (4) ~ exfat")
echo("- at the end of one or the other choice, the following command will done")
echo("- assign : alows the computer to acces it by giving it a label (cannot be chosen)")
print()
diskpart
list disk
echo "Please enter the index number of you're disk, (disk 0 is your primary disk, it cannot be formated so there is no point in selecting it)"
set /p diskchoice=
select disk %diskchoice%
clean
create partition primary
:importantQuestion
echo "Would you like to rename your disk (please answer by y for yes or n for no):"
set /p renamedisk=
if %renamedisk%==y (
    :wrongformaty
    echo "(1) ~ ntfs (recommended), (2) ~ fat, (3) ~ fat32, (4) ~ exfat"
    echo "Please enter the desired format (1, 2, 3 or 4):"
    set /p format=

    if %format%==1 (
        echo "ntfs"
        set /a finalformat="ntfs"
    )
    if %format%==2 (
        echo "fat"
        set /a finalformat="fat"
    )
    if %format%==3 (
        echo "fat32" 
        set /a finalformat="fat32"   
    )
    if %format%==4 (
        echo "exfat"
        set /a finalformat="exfat"
    )
    echo "Please make sure you have entered a whole number between 1 and 4."
    echo "You have entered: %format%"
    goto wrongformaty
    echo.
    :namingDisky
    echo "Please enter the desired name of the disk: (maximum letters: 11)"
    echo "wordcount guide"
    echo "1 3 5 7 9 11 (max)"
    set /p nameOfDisk=
    set lenNameOfDisk=nameOfDisk
    set length=0
    :loopy
    if "%lenNameOfDisk%"=="" goto endloopy
    set lenNameOfDisk=%lenNameOfDisk:~0,-1%
    set /a length=%length%+1
    goto loopy
    :endloopy
    if length leq 11 (
        echo "format fs=%finalformat% label=%nameOfDisk%"
        format fs=%finalformat% label="%nameOfDisk%"
    )
    else (
        echo "Please enter no more than 11 characters."
        echo "You have entered %length% characters"
        goto namingDisky
    )
)
if %renamedisk%==Y (
    :wrongformatY
    echo "(1) ~ ntfs (recommended), (2) ~ fat, (3) ~ fat32, (4) ~ exfat"
    echo "Please enter the desired format (1, 2, 3 or 4):"
    set /p format=

    if %format%==1 (
        echo "ntfs"
        set /a finalformat="ntfs"
    )
    if %format%==2 (
        echo "fat"
        set /a finalformat="fat"
    )
    if %format%==3 (
        echo "fat32" 
        set /a finalformat="fat32"   
    )
    if %format%==4 (
        echo "exfat"
        set /a finalformat="exfat"
    )
    echo "Please make sure you have entered a whole number between 1 and 4."
    echo "You have entered: %format%"
    goto wrongformatY
    echo.
    :namingDiskY
    echo "Please enter the desired name of the disk: (maximum letters: 11)"
    echo "wordcount guide"
    echo "1 3 5 7 9 11 (max)"
    set /p nameOfDisk=
    set lenNameOfDisk=nameOfDisk
    set length=0
    :loopY
    if "%lenNameOfDisk%"=="" goto endloopY
    set lenNameOfDisk=%lenNameOfDisk:~0,-1%
    set /a length=%length%+1
    goto loopY
    :endloopy
    if length leq 11 (
        echo "format fs=%finalformat% label=%nameOfDisk%"
        format fs=%finalformat% label="%nameOfDisk%"
    )
    else (
        echo "Please enter no more than 11 characters."
        echo "You have entered %length% characters"
        goto namingDiskY
    )
)
if %renamedisk%==n (
    echo "(1) ~ ntfs (recommended), (2) ~ fat, (3) ~ fat32, (4) ~ exfat"
    echo "Please enter the desired format (1, 2, 3 or 4):"
    set /p format=

    if %format%==1 (
        echo "ntfs"
        set /a finalformat="ntfs"
    )
    if %format%==2 (
        echo "fat"
        set /a finalformat="fat"
    )
    if %format%==3 (
        echo "fat32" 
        set /a finalformat="fat32"   
    )
    if %format%==4 (
        echo "exfat"
        set /a finalformat="exfat"
    )
    format fs=%finalformat%
)
if %renamedisk%==N (
    echo "(1) ~ ntfs (recommended), (2) ~ fat, (3) ~ fat32, (4) ~ exfat"
    echo "Please enter the desired format (1, 2, 3 or 4):"
    set /p format=

    if %format%==1 (
        echo "ntfs"
        set /a finalformat="ntfs"
    )
    if %format%==2 (
        echo "fat"
        set /a finalformat="fat"
    )
    if %format%==3 (
        echo "fat32" 
        set /a finalformat="fat32"   
    )
    if %format%==4 (
        echo "exfat"
        set /a finalformat="exfat"
    )
    format fs=%finalformat%
)
echo "please enter either n or N for no or y or Y for yes, you have entered: %renamedisk%"
goto importantQuestion
assign
pause
echo "Progam created by Henry Letellier"
echo "My instagram @hen9341_henry"
pause
pause
