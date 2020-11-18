# from Tableau import*
import tkinter as tk
import datetime, os
date=datetime.datetime.now()

class Main:
    def __init__(self,data,chosenFile,date,g,t,M,m,ma,LN,FN):
        self.gender=g
        self.time=t
        self.markTime=M
        self.markGap=m
        self.markRecovery=ma
        self.mT=self.markTime
        self.mG=self.markGap
        self.mR=self.markRecovery
        self.file=data
        self.LN=LN #Last Name
        self.FN=FN #First Name
        self.chosen={"Last name":"","First name":"","mark":"","gender":"","gap":"","Recovery main":""}
        self.chosen["T{}".format(self.chosen["gender"])]=""
        for i in range(2):
            for k in range(3):
                self.chosen["T{}_R{}".format(i,k)]=""
        self.Date="{}/{}/{}".format(date.day,date.month,date.year)
        self.DateFile="{} {} {}".format(date.day,date.month,date.year)
        self.filepath=""
        self.fileList=os.listdir("data")
        self.chosenFile=chosenFile
        self.path="data/{}".format(self.chosenFile)
        Main.show(self)
    def show(self):
        print(self.gender)
        print(self.time)
        print(self.markTime)
        print(self.markGap)
        print(self.markRecovery)
        print(self.mT)
        print(self.mG)
        print(self.mR)
        print(self.file)
        print(self.LN)
        print(self.FN)
        print(self.chosen)
        print(self.Date)
        print(self.DateFile)
        print(self.filepath)
        print(self.fileList)
        print(self.chosenFile)
        print(self.path)
gender,data,chosenFile="ee","ee",None
time="ee"
markTime="ee"
markGap="ee"
markRecovery="ee"
g="e"
t="e"
M="e"
m="e"
ma="e"
LN="e"
FN="e"
Project_Gap_main_corresponds=["0","2","4"]
Init=Main.__init__(gender,data,chosenFile,date,g,t,M,m,ma,LN,FN)


OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

app = tk.Tk()

app.geometry('100x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))
    global a
    a=variable.get()
    print(a)
    return a

variable.trace("w", callback)

app.mainloop()

print(a)

