# 2,3,10,50,100 (ou 1€)

class loops:
    def euro(SomeInnitiale,euro):
        print(SomeInnitiale,euro)
        if SomeInnitiale>100:return (loops.euro(SomeInnitiale-100,euro+1))
        else:return (SomeInnitiale,euro)
    def middlecentime(SomeInnitiale,middlecentime):
        print(SomeInnitiale,middlecentime)
        if SomeInnitiale>50:return (loops.middlecentime(SomeInnitiale-50,middlecentime+1))
        else:return (SomeInnitiale,middlecentime)
    def tencentime(SomeInnitiale,tencentime):
        print(SomeInnitiale,tencentime)
        if SomeInnitiale>10:return (loops.tencentime(SomeInnitiale-10,tencentime+1))
        else:return (SomeInnitiale,tencentime)
    def fivecentime(SomeInnitiale,fivecentime):
        print(SomeInnitiale,fivecentime)
        if SomeInnitiale>5:return (loops.fivecentime(SomeInnitiale-5,fivecentime+1))
        else:return (SomeInnitiale, fivecentime)
    def threecentime(SomeInnitiale,threecentime):
        print(SomeInnitiale,threecentime)
        if SomeInnitiale>3:return (loops.threecentime(SomeInnitiale-3,threecentime+1))
        else:return (SomeInnitiale,threecentime)
    def twocentime(SomeInnitiale,twocentime):
        print(SomeInnitiale,twocentime)
        if SomeInnitiale>2:return (loops.twocentime(SomeInnitiale-2,twocentime+1))
        else:return (SomeInnitiale, twocentime)
    
euro=0
middlecentime=0
tencentime=0
threecentime=0
twocentime=0
fivecentime=0
SomeInnitiale=int(input("Entrez votre montant à rendre (en centimes):"))

if SomeInnitiale==0 or SomeInnitiale==1:
    print(SomeInnitiale)
else:
    while SomeInnitiale>0:
        if SomeInnitiale>2:
            if SomeInnitiale>3:
                if SomeInnitiale>10:
                    if SomeInnitiale>50:
                        if SomeInnitiale>100:
                            loops.euro(SomeInnitiale,euro)
                        else:
                            loops.middlecentime(SomeInnitiale,middlecentime)
                    else:
                        loops.tencentime(SomeInnitiale,tencentime)
                else:
                    loops.fivecentime(SomeInnitiale,fivecentime)
            else:
                loops.threecentime(SomeInnitiale,threecentime)
        else:
            loops.twocentime(SomeInnitiale,twocentime)
            break
    

print("La machine vous rendra:")
print("- {} picèce de 1 centime".format(SomeInnitiale))
print("- {} picèce de 2 centimes".format(twocentime))
print("- {} picèce de 3 centimes".format(threecentime))
print("- {} picèce de 5 centimes".format(fivecentime))
print("- {} picèce de 10 centimes".format(tencentime))
print("- {} picèce de 50 centimes".format(rendumiddlecentime))
print("- {} picèce de 1 euro".format(euro))