from random import*
from tkinter import*
import os, platform, datetime
dateorevent=["date","event"]
qdateorevent=["Quand a été","Que s'est-il passé"]
fdateorevent=["La bonne date", "Le bon évènement"]
edateorevent=["e",""]
date=datetime.datetime.now()
DATE="{}/{}/{}".format(date.day,date.month,date.year)
TIME="{}:{}:{}".format(date.hour,date.minute,date.second)
# -------------------------------- Variables ----------------------------------------

#Font="Algerian"
Font="Times_New_Roman"
#Font=""
#Size=14
#Size=10
Size=8
WBG="Orange"
FBG="White"
LBG="grey"
WFG="black"
FFG="blue"
LFG="white"
F1=FLAT
F1T=GROOVE
F1b=GROOVE
F1q=FLAT
hfDE="blue"
hbDE="green"
hfEN="blue"
hbEN="green"
hfFR="blue"
hbFR="green"
hfES="blue"
hbES="green"
hfq="blue"
hbq="green"
def write(content):
    f=open("Stats_dates_d_histoire_text_py.txt","a")
    f.write(content)
    f.close
def pause():
    pause=input("Please press enter to continue...")
def random():
    DATEOREVENT=randint(0,1)
    button1=randint(0,len(dates)-1)
    button2=randint(0,len(dates)-1)
    button3=randint(0,len(dates)-1)
    button4=randint(0,len(dates)-1)
    if DATEOREVENT==1:
        DATEOREVENTT=0
    else:
        DATEOREVENTT=1
    answer=randint(1,3)
    if answer==1:
        button1=i
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
    elif answer==2:
        button2=i
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button1 or button2==button3 or button2==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
    elif answer==3:
        button3=i
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button1 or button2==button3 or button2==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
    else:
        button4=i
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
        button1=randint(0,len(dates))
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        while redo=="redo":
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button1 or button2==button3 or button2==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
    return DATEOREVENT, DATEOREVENTT, button1, button2, button3, button4
score,erreur=0,0
dates=[
    {"date":"de 1337-1453 J.-C.","event":"la Guerre de 100 ans"},
    {"date":"en 1492 J.-C.","event":"la Découverte de L'Amérique"},
    {"date":"le 29 mai 1453 J.-C.","event":"l'Imprimerie en Europe"},
    {"date":"en 1682 J.-C.","event":"Louis XIV à Versailles"},
    {"date":"de 1775-1782 J.-C.","event":"la Révolution Américaine"},
    {"date":"le 2 novembre 1789 - 9 novembre 1799","event":"la Révolution française"},
    {"date":"le 14 Juillet 1789 J.-C.","event":"la Prise de la bastille"},
    {"date":"le 2 Décembre 1804 J.-C.","event":"le Sacre de Napoléon"},
    {"date":"de 1811-1820 J.-C.","event":"l'Indépendance En Amérique du Sud"},
    {"date":"en 1815 J.-C.","event":"le Congrès de Vienne"},
    {"date":"de 1861-1865 J.-C.","event":"la Guerre de Sécession"},
    {"date":"en 1989 J.-C.","event":"la Chute du mur de Berlin"},
    {"date":"en 1917 J.-C.","event":"la Révolution Russe"},
    {"date":"au Milieu XIXe J.-C.","event":"la Révolution Industrielle"},
    {"date":"le 24 octobre 1929 J.-C.","event":"le Jeudi noir"},
    {"date":"de 1941-1945 J.-C.","event":"Extermination des juifs"},
    {"date":"le 1er Octobre 1949 J.-C.","event":"La République populaire de Chine"},
    {"date":"en 1954 J.-C.","event":"Guerre d’Algérie"},
    {"date":"en 1965 J.-C.","event":"Guerre du Vietnam"},
    {"date":"le 21 juillet 1969","event":"Le premier pas sur la lune"},
    {"date":"le 9 novembre 1989","event":"Chute du mur de Berlin"},
    {"date":"le 5 mai 1789","event":"l'Ouverture des états généraux"},
    {"date":"le 20 juin 1789","event":"le serment du jeux de paume"},
    {"date":"le 26 août 1789","event":"l'Adoption de la déclaration des droits de l'homme et du citoyen"},
    {"date":"le 21 juin 1791","event":"la Fuite de Varennes"},
    {"date":"le 17 juillet 1791","event":"la fusillade du Champ-de-Mars"},
    {"date":"le 14 septembre 1791","event":"Louis XVI prête serment à la Constitution"},
    {"date":"le 10 août 1792","event":"la prise des Tuileries avec l'aide des fédérés marseillais"},
    {"date":"le 10 août 1792 (bis)","event":"la Chute de la monarchie et suspension de Louis XVI"},
    {"date":"le 21 septembre 1792","event":"la Convention nationale abolit la royauté et fonde la Ire République au lendemain de la bataille de Valmy"},
    {"date":"le 21 janvier 1793","event":"l'Exécution de Louis XVI"},
    {"date":"le 9 thermidor an II","event":"la Fin de la Terreur et chute de Robespierre"},
    {"date":"le 1er prairial an III","event":"l'Insurrection populaire réclamant le pain et le retour à la Constitution de l'an I (Insurrection violement réprimée dans le sang)"},
    {"date":"le 9 brumaire an IV","event":"le début du Directoire"},
    {"date":"le 18 brumaire an VIII","event":"le Coup d'état établissant le Consulat, dominé par Bonaparte"},

]
write("\n-------------------------------- stats ----------------------------------------\nChemin d'accès:{}\nOS:{}\nDate:{}\ntime:{}\n-------------------------------- end stats ----------------------------------------\n\n-------------------------------- Game Stats ----------------------------------------\nFont:{}\nSize:{}\nWBG:{}\nFBG:{}\nLBG:{}\nWFG:{}\nFFG:{}\nLFG:{}\nF1:{}\nF1T:{}\nF1b:{}\nF1q:{}\nhfDE:{}\nhbDE:{}\nhfEN:{}\nhbEN:{}\nhfFR:{}\nhbFR:{}\nhfES:{}\nhbES:{}\nhfq:{}\nhbq:{}\nscore:{}\nerreur:{}\ndates:\n-------------------------------- End of Game Stats ----------------------------------------\n\n-------------------------------- InGameStats ----------------------------------------\n".format(os.getcwd(),platform.system(),DATE,TIME,Font,Size,WBG,FBG,LBG,WFG,FFG,LFG,F1,F1T,F1b,F1q,hfDE,hbDE,hfEN,hbEN,hfFR,hbFR,hfES,hbES,hfq,hbq,score,erreur,dates))
for i in range(len(dates)):
    #random()
    DATEOREVENT=randint(0,1)
    # print(DATEOREVENT)
    button1=randint(0,len(dates)-1)
    button2=randint(0,len(dates)-1)
    button3=randint(0,len(dates)-1)
    button4=randint(0,len(dates)-1)
    if DATEOREVENT==1:
        DATEOREVENTT=0
    else:
        DATEOREVENTT=1
    ansswer=randint(1,3)
    print("answer={}".format(ansswer))
    if ansswer==1:
        button1=i
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button3={}".format(button3))
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
                break
    elif ansswer==2:
        button2=i
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button1={}".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
                break
    elif ansswer==3:
        button3=i
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button1={}".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
                break
    #else:
    #   button4=i
    #   button2=randint(0,len(dates)-1)
        #if button2==i or button2==button1 or button2==button3 or button2==button4:
         #       redo="redo"
          #  else:
           #     redo="no"
            #while redo=="redo":
             #   if button2==i:
              #      button2=randint(0,len(dates)-1)
               # elif button2==button1 or button2==button3 or button2==button4:
                #    button2=randint(0,len(dates)-1)
                #else:
                 #   redo="no"
    #   button3=randint(0,len(dates)-1)
    #    if button3==i or button3==button1 or button3==button2 or button3==button4:
     #           redo="redo"
      #      else:
       #         redo="no"
        #    while redo=="redo":
         #       if button3==i:
          #          button3=randint(0,len(dates)-1)
           #     elif button3==button1 or button3==button2 or button3==button4:
            #        button3=randint(0,len(dates)-1)
             #   else:
              #      redo="no"
    #   button1=randint(0,len(dates))
    #    if button1==i or button1==button2 or button1==button3 or button1==button4:
     #           redo="redo"
      #      else:
       #         redo="no"
        #    while redo=="redo":
         #       if button1==i:
          #          button1=randint(0,len(dates)-1)
           #     elif button1==button1 or button2==button3 or button2==button4:
            #        button1=randint(0,len(dates)-1)
             #   else:
              #      redo="no"
    print("{}: {} ?\n".format(qdateorevent[DATEOREVENTT],dates[i][dateorevent[DATEOREVENT]]))
    answer=input("{}, {}, {} ?".format(dates[button1][dateorevent[DATEOREVENTT]],dates[button2][dateorevent[DATEOREVENTT]], dates[button3][dateorevent[DATEOREVENTT]]))
    if answer==dates[i][dateorevent[DATEOREVENTT]]:
        print("Correct\n {} correspond bien {}".format(dates[i][dateorevent[DATEOREVENTT]], dates[i][dateorevent[DATEOREVENT]]))
        pause()
        score+=1
        erreur+=0
    else:
        print("Faux\n {} ne correspond pas {}\n {} étai{} {}\n".format(answer, dates[i][dateorevent[DATEOREVENT]],fdateorevent[DATEOREVENT],edateorevent[DATEOREVENT],dates[i][dateorevent[DATEOREVENTT]]))
        pause()
        score+=0
        erreur+=1
    write("\n________________________________ Round {} Stats ________________________________________\nDATEOREVENT:{}\nbutton1:{}={}\nbutton2:{}={}\nbutton3:{}={}\nbutton4:{}={}\nDATEOREVENTT:{}\nansswer:{}\nredo:{}\n{}: {} ?\n{}, {}, {} ?\nanswer:{}\n________________________________ end Round {} Stats ________________________________________".format(i+1,DATEOREVENT,button1,dates[button1][dateorevent[DATEOREVENTT]],button2,dates[button2][dateorevent[DATEOREVENTT]],button3,dates[button3][dateorevent[DATEOREVENTT]],button4,dates[button4][dateorevent[DATEOREVENTT]],DATEOREVENTT,ansswer,redo,qdateorevent[DATEOREVENTT],dates[i][dateorevent[DATEOREVENT]],dates[button1][dateorevent[DATEOREVENTT]],dates[button2][dateorevent[DATEOREVENTT]], dates[button3][dateorevent[DATEOREVENTT]],answer,i+1))

write("\n-------------------------------- end of InGameStats ----------------------------------------\n")

print(" Vous avez {} points et fait {} fautes.".format(score,erreur))
