#Le jeux du passager clandestin
#paracode
#groupe de x personnes (ex:autour de table)
#Mise bet=[0,10]
#1Mise=1personne
#révéler mise de chaque personne
#récuperer mise de chaque personne
#Tot_tour= Additionner *mises
#Tot_tour*=banque (banque=2)
#rendu=diviser Tot_tour par nbpersonne
#donner à chaque personne la var rendu

#default defs
def pause():pause=input("Press enter to continue...")
import random,os
i=bet=result=current_type_of_play=next_turn_type=0
default_turn_track={"round(i)":i,"bet":bet,"result":result,"c_t_o_p":current_type_of_play,"n_t_t":next_turn_type}



class root:
    def __init__(self):
        self.i=0
        self.nb_players_list=[]
        self.GType=["C","T"]
        self.StrategyType=["Nice","Mean","Uncertain","Cautius","Lunatic"]
    def CNumber(question):
        given=False
        while given==False:
            a=input(question)
            try:
                a=int(a)
                given=True
                return a
            except:
                print("Please only enter a whole number.\nYou have entered: '{}'".format(a))
                pause()
    def CNNZero():
        """Check Number Not Zero"""
        given=False
        while given==False:
            a=root.CNumber("Enter the amount of players")
            if a>0:
                given=True
                return a
            else:
                print("Please only enter a whole positive number above Zero.\nYou have entered: '{}'".format(a))
                pause()
    def YNo(question):
        given=False
        while given==False:
            a=input(question).lower()
            if a=="y" or a=="n":
                given=True
                return a
            except:
                print("Please only enter y for yes or n for no.\nYou have entered: '{}'".format(a))
                pause()
    def CText(question):
        given=False
        while given==False:
            a=input(question)
            try:
                a=int(a)
                print("Please only enter a name, not numbers.\nPS:You're name can contain numbers.\nYou have entered: '{}'".format(a))
                pause()
            except:
                if len(a)>0:
                    given=True
                    return a
                else:
                    print("Please only enter a name.\nPS:You're name can contain numbers.\nYou have entered: '{}'".format(a))
                    pause()
class Initialise(root):
    def GVars(self):
        """Get Vars"""
        self.nb_players=root.CNNZero()
        Initialise.NPlayers(self)
        #self.StrategyType=["Nice (ccccc)","Mean (TTTT)","Uncertain (ctctctct)","Cautious (TCTCTCTC)","Lunatic (random.randint(ct))"]
        self.MainStrategy=Initialise.CMStrategy(self.StrategyType,self.nb_players)
        for i in range(1,self.nb_players+1):
            self.nb_players_list.append(
                {"player_nb":i,
                 "player_name":self.player_names[i],
                 "total_earned_points":{"bef_bank":0,"af_bank":0},
                 "chosen_Technic":self.StrategyType[self.MainStrategy[i]],
                 "tot_techniques":{"C":0,"T":0,"R":{"Times":0,"C":0,"T":0}},
                 "rounds":{}}
                )
        .
    def NPlayers(self):
        """Name Players"""
        self.player_names=[]
        NameThem=root.YNo("Do you whish to name all the players? [(y)es/(n)o]")
        if NameThem=="y":
            for i in range(self.nb_players):
                self.player_names.append(root.CText("Please enter the name of player n°{}:".format(i)))
        else:
            for i in range(self.nb_players):
                self.player_names.append(" ")
    def CMStrategy(options,people):
        Temp={}
        MainStrategy=[]
        for i in range(len(options)):
            Temp[i]=options[i]
        Temp[len(options)]="Randomly choose from one of the above"
        Possibilities="index Strategy"
        line=0
        for i in Temp:
            if line==3:
                Possibilities+="\n"
                line=0
            Possibilities+="{}     {} ".format(i,Temp[i])
            line+=1
        RandomAll=root.YNo("Do you wish to apply one specific strategy (including: randomly choosing a different strategy for each player) to all the players? [(y)es/(n)o]")
        if RandomAll=="y":
            MS=Initialise.GMS(Possibilities,"Enter the index of strategy you wish to apply to all the players",options,0)
            if 
        else:
            auto=-1
        for i in range(people):
            if auto==-1:
                MS=Initialise.GMS(Possibilities,"Enter the index of strategy you wish to apply to player n°{}".format(i),options,1)
            else:
                if .
        return MainStrategy
    def GMS(Possibilities,message,options,status):
        """ Get Main Strategy """
        given=False
        while given==False:
            MS=root.CNumber("{}\n{}:".format(Possibilities,message))
            if MS in Temp:
                given=True
                if Temp[MS]=="Randomly choose from one of the above":
                    if status==1:
                        MS=random.randint(0,len(options)-1)
                    else:
                        MS=len(options)
                else:
                    MS
            else:
                print("Please enter a whole number present from the list above.\nYou have entered: '{}'".format(MS))
                pause()
        return MS
    




class TypeOfPlay(root):
    def C():"""cooperation""";print("C")
    def T():"""Trahison""";print("T")
    def R():"""random""";print("R");"if random.randint()==C:return C(); else: return T()"
    def DecideType():
        """Choose Type of Play"""
        print("Decide Type")

class CreateReport(root):
    def CFFdata():"""Check For Folder data""";print("CFFdata")
    def CReport():"""Create Report""";print("CReport")
    def WRTFile():"""Write Report To File""";print("WRTFile")

class PlayRound(root):
    def PR():"""Play Round""";print("PR")
    def UList():"""Update List""":print("UList")

RI=root()
II=Initialise()
TOPI=TypeOfPlay()
CRI=CreateReport()
PRI=PlayRound()
