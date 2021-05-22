from math import *
math=[70.00,35.43,35.26,6.36,5.16]
joule=[]
joule2=[]
def write(e):
    f=open("stat_conversion_ex_10_poly.txt","w")
    f.write(e)
    f.close()
for i in range(len(math)):
    numm=math[i]
    num=int(numm)
    print("Je prend le nombre {} et je le divise par 1000 pour passer du kilo à la tonne.".format(num))
    write("Je prend le nombre {} et je le divise par 1000 pour passer du kilo à la tonne.".format(num))
    num/=1000
    print("Je prend le nombre {} et je mulitîplie par 41900000000 pour passer de la tonne au Joule.".format(num))
    write("Je prend le nombre {} et je mulitîplie par 41900000000 pour passer de la tonne au Joule.".format(num))
    num*=41900000000
    print("Le nombre {} (en kg) est égale à {} Joule(s).".format(numm,num))
    write("Le nombre {} (en kg) est égale à {} Joule(s).".format(numm,num))
    joule.append(num)
    joule2.append(num)
#print(joule)

for i in range(len(joule)):
    for e in range(len(joule2)):
        if joule[i]<joule2[e]:
            print("{} est supérieur à {}".format(joule[i],joule2[e]))
            write("{} est supérieur à {}".format(joule[i],joule2[e]))
        elif i>e:
            print("{} est inférieur à {}".format(joule[i],joule2[e]))
            write("{} est inférieur à {}".format(joule[i],joule2[e]))
        elif joule[i]==joule2[e]:continue

pause=input("press Enter to continue")
        
        
