import os
from time import sleep
from tkinter import *
from tkinter.filedialog import *
import shutil
def pause():pause=input("Press enter to continue...")
def trim_path(path):
    main=word=""
    for i in path:
        if i=="/":
            word+="/"
            main+=word
            word=""
        else:
            word+=i
    print(f"main={main},word={word}")
    return [main,word]
def folder_exists(folder):
    run_command="yes"
    if os.path.exists(folder)==True:
        cont=True
        while cont==True:
            overwrite=input("a folder named {} aleready exists in this directory. Do you wish to overwrite it? [(y)es/(n)o]".format(folder)).lower()
            if overwrite=="y":
                os.system("del /q {}".format(folder))
                os.mkdir(folder)
                shutil.copyfile(file, f"{folder}/{file}")
                os.chdir(folder)
                cont=False
            elif overwrite=="n":
                orint("aborting....")
                pause()
                folder=file=path=To_write=""
                run_command="no"
                cont=False
            else:
                print(f"Please ensure you have either entred y for yes or n for no\nYou have entered: {overwrite}")
    else:
        os.mkdir(folder)
        shutil.copyfile(file, f"{folder}/{file}")
        os.chdir(folder)
    return run_command
def run_command(command,run_command):
    if run_command=="yes":
        os.system("python setup.py py2exe")
class additionnal:
    def set_icon():
        icon_path = askopenfilename(title="Ouvrir le fichier",filetypes=[('all files','.*')])
def start_up():
    filepath = askopenfilename(title="Ouvrir le fichier",filetypes=[('all files','.*')])
    print(os.getcwd())
    print(filepath)
    options=trim_path(filepath)
    file=options[1]
    path=options[0]
    os.chdir(path)
    folder=f"processing_file_{file}"
    run_command=folder_exists(folder)
    print(os.getcwd())
    run_command(command,run_command)
start_up()
pause()
