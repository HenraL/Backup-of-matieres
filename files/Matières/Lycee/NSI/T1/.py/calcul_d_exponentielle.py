from math import *

def KingKong(p):
    N=0
    U=0.5
    k=(sqrt(exp(1)))/((sqrt(exp(1))+1)**2)
    while ((k**N)/2)>=10**-p:
        N+=1
        U=exp(U)/(exp(U)+1)
    return U

print("p=2")
print(KingKong(2))
print("p=3")
print(KingKong(3))
