#version récursive
def factoriel(n):
    
    if n==0:
        res=1 #concition d'arrêt
    else:
        res=n*factoriel(n-1) #appel récursif avec n-1
        print(res)
    print("n={}".format(n))
    print("res={}".format(res))
    return res

print("factoriel(4)={}".format(factoriel(4)))