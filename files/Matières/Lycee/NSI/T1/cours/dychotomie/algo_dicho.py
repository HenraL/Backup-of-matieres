def dicho_math_et_tic(int_min,int_max,longueur): #https://www.youtube.com/watch?v=V7mlMCSrq1U
    amplitude=int_max-int_min
    #centre_interval=
    #image_du_centre=f(centre)
    while amplitude>longueur:
        x=(int_min+int_max)/2
        y=x**3-7*x-1
        if y>0:
            int_max=x
        else:
            int_min=x
        amplitude=int_max-int_min
    return int_min,int_max,amplitude
    
def dicho_prof(tab,val):
    gauche=0
    droite=len(tab)-1
    while gauche<=droite:
        milieu=(gauche+droite)//2
        if tab[milieu]==val:
            #val=trouvé dans tab, où = à position milieu
            return milieu
        elif tab[milieu]>val:
            #on cherche entre gauche et milieu
            droite=milieu-1
        else: #c'est-à-dire tab[milieu]<val
            #on cherche entre milieu+1 et droite
            gauche=milieu+1
        #on n'a pas trouvé donc on sort.
        return -1
Tab=[1,3,7,8,12,15,25,37,42]
val=14
e=dicho_prof(Tab,val)
print(f"e={e}")
val=12
e=dicho_prof(Tab,val)
print(f"e={e}")

c=dicho_math_et_tic(2,4,1)
print(f"{c[0]}<{c[2]}<{c[1]}")
c=dicho_math_et_tic(2,4,0.25)
print(f"{c[0]}<{c[2]}<{c[1]}")
c=dicho_math_et_tic(2,4,0.01)
print(f"{c[0]}<{c[2]}<{c[1]}")
c=dicho_math_et_tic(2,4,0.001)
print(f"{c[0]}<{c[2]}<{c[1]}")

print("Created By Henry Letellier")
