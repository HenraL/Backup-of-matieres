from math import sqrt
class pourcent:
    def substract(to_deal,percentage,Base):
        result_from_percentage = to_deal*(percentage/Base)
        e=to_deal-result_from_percentage
        return f"{e}={to_deal}-({to_deal}*({percentage}/{Base}))"
    def add(to_deal,percentage,Base):
        result_from_percentage = to_deal*(percentage/Base)
        e=to_deal+result_from_percentage
        return f"{e}={to_deal}-({to_deal}*({percentage}/{Base}))"
    def make(total_val_from_perc,total_val_perc,Base):
        if total_val_from_perc>total_val_perc:
            print("Value over 100")
            e=(Base*total_val_from_perc)/total_val_perc
            return f"({Base}*{total_val_from_perc})/{total_val_perc}={e}"
        else:
            print("Value below 100")
            e=(Base*total_val_from_perc)/total_val_perc
            return f"({Base}*{total_val_from_perc})/{total_val_perc}={e}"
    def undo(total_value,perc,Base):
        e=total_value*(perc/Base)
        return f"{total_value}*({perc}/{Base})={e}"
    def add_inners(lst):
        unpercentad=0
        for i in range(len(lst)):
            unpercentade+=int(lst[i])/100
        return unpercentade*100
    def substract_inners(lst,to_take_from):#to_take_from must be given as a percentage
        unpercentad=to_take_from/100
        for i in range(len(lst)):
            unpercentade-=int(lst[i])/100
        return unpercentade*100

class Puissance:
    def UI(U,I): #primaire
        return U*I
    def PI(P,I):
        return P/I
    def PU(P,U):
        return P/U
class Puissance_par_effet_Joule:
    def RI2(R,I=""): #primaire
        if I=="":return ["Can't calculate, missing I",R]
        else:return ["PEJ",R*I**2]
    def PR(P,R): #I is ²
        I=P/R
        return I
    def PI2(P,I):
        return P/(I**2)
    def PEJ_if_percent(R,I,Percent):
        PEJ=(R*I)/Percent
        return PEJ
    def GetI(PEJ,R):
        return sqrt(PEJ/R)
    def totale(PJ1,PJ2,PJ3,PJ4):
        #PJ1 or 2 or 3 or 4 = Puissance_par_effet_Joule.RI2(R,I)
        missing=[]
        if PJ1[0]=="Can't calculate, missing I":
            PJ1[0]=False
            missing.append(1)
        if PJ2[0]=="Can't calculate, missing I":
            PJ2[0]=False
            missing.append(2)
        if PJ3[0]=="Can't calculate, missing I":
            PJ3[0]=False
            missing.append(3)
        if PJ4[0]=="Can't calculate, missing I":
            PJ4[0]=False
            missing.append(4)
        if len(missing)==4:PJtot="Error, values cannot all be NULL (None in python)"
        elif PJ1[0]==False and PJ2[0]==False:PJtot=f"{PJ1[1]}*I1²+{PJ2[1]}*I2²+{PJ3[1]+PJ4[1]}"
        elif PJ2[0]==False and PJ3[0]==False:PJtot=f"{PJ2[1]}*I2²+{PJ3[1]}*I3²+{PJ1[1]+PJ4[1]}"#uncommon
        elif PJ3[0]==False and PJ4[0]==False:PJtot=f"{PJ1[1]+PJ2[1]}+{PJ3[1]}*I3²+{PJ4[1]}*I4²"
        elif PJ4[0]==False and PJ1[0]==False:PJtot=f"{PJ1[1]}*I1²+{PJ2[1]+PJ3[1]}+{PJ4[1]}*I4²"#uncommon
        elif PJ1[0]==False:PJtot=f"{PJ1[1]}*I1²+{PJ2[1]+PJ3[1]+PJ4[1]}"#uncommon
        elif PJ2[0]==False:PJtot=f"{PJ2[1]}*I2²+{PJ1[1]+PJ3[1]+PJ4[1]}"#uncommon
        elif PJ3[0]==False:PJtot=f"{PJ3[1]}*I3²+{PJ1[1]+PJ2[1]+PJ4[1]}"#uncommon
        elif PJ4[0]==False:PJtot=f"{PJ4[1]}*I4²+{PJ1[1]+PJ3[1]+PJ2[1]}"#uncommon
        else:PJtot=PJ1[1]+PJ2[1]+PJ3[1]+PJ4[1]
        return PJtot,missing
#class advanced:
    #.

f=1
default_base=100

while f==1:
    g=int(input("0=quit\nchoix: 1 à 4 : "))
    if g==1:
        to_deal=int(input("To deal (ex:original sum to take from)"))
        percentage=int(input("persentage to take (ex: 5):"))
        Base=int(input("Base (default 100):"))
        if len(Base)==0:
            Base=default_base
        e=pourcent.substract(to_deal,percentage,Base)
        print(f"pourcent.substract({to_deal},{percentage},{Base})={e}")
    elif g==2:
        pourcent.add()
    elif g==3:
        pourcent.make()
    elif g==4:
        pourcent.undo()
    elif g==0:
        f=g
    else:
        print(f"Not found.\nEntered {g}.")
