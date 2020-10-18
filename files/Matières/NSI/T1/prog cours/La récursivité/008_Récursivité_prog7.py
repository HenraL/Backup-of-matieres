def affiche(k):
    if k<10:
        print(k)
        affiche(k+1)

affiche(0)
pause=input("appuyez sur entré pour continuer...")