from math import*
d=5 #en cm
r=d/2 #en cm
r=r*0.01 #m
#print(r)
n=1.33 #
#n=float(n)
#r=float(r)
def fOF(n,r):
    global f
    f=(n*r)/(2*(n-1))
    return f
print(fOF(n,r))
