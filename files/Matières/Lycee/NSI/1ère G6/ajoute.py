def ajoute(n,p):
 somme=0
 for i in range(n,p+1):
  somme+=i
 return somme

def pause():
    pause=input("appuyez sur entrer pour continuer....")

print(ajoute(2,4))

print("mystere T")
def mystere(T):
    s = 0
    for k in T:
        if k % 2 == 0:
            s = s+k
    return s

print("question F.3")
def f(x):
    x = x + 1
    return x + 1
x = 0
print(f(x+1))

print("question F.4")
def f(x,y,z):
    if x+y == z:
        return True
    else:
        return False

print("f(1,2,3)={}".format(f(1,2,3)))
print("f(1.1,2.3,3.2)={}".format(f(1.1,2.3,3.2)))
print("f(0.1,0.2,0.3)={}".format(f(0.1,0.2,0.3)))
print("f(5,2,4)={}".format(f(5,2,4)))
print("f(5.1,2.3,4.2)={}".format(f(5.1,2.3,4.2)))
print("f(0.5,0.2,0.4)={}".format(f(0.5,0.2,0.4)))
print("f(1,2,3)={}".format(f(1,2,3)))
print("f(1.1,2.3,3.2)={}".format(f(1.1,2.3,3.2)))
print("f(0.1,0.2,0.3)={}".format(f(0.1,0.2,0.3)))
t1=[1,2,3]
t2=[4,3]
t3=[4,5]
print("f(t1[1,2,3])={}".format(f(t1,t2,t3)))
t1=[1.1,2.3,3.2]
t2=[4,3]
t3=[4,5]
print("f(t1[1.1,2.3,3.2])={}".format(f(t1,t2,t3)))
t1=[0.1,0.2,0.3]
t2=[4,3]
t3=[4,5]
print("f(t1[0.1,0.2,0.3])={}".format(f(t1,t2,t3)))

print("Question F.6")
a = 4
b = 4
c = 4
while a < 5:
    a = a - 1
    b = b + 1
    c = c * b
    if a==0:
        a=6

print("a,b,c={}{}{}".format(a,b,c))

def search(x, y):
# x est la valeur à chercher
# y est une liste de valeurs
    for i in range(len(y)):
        if x == y[i]:
            return i
    return None

L1=[1,2,3,4,5,6,7,8,9]
print("search(5,L1)={}".format(search(5,L1)))
print("search(0,L1)={}".format(search(0,L1)))
print("search(1,L1)={}".format(search(1,L1)))
print("search(2,L1)={}".format(search(2,L1)))
print("search(3,L1)={}".format(search(3,L1)))
print("search(4,L1)={}".format(search(4,L1)))
print("search(6,L1)={}".format(search(6,L1)))
print("search(7,L1)={}".format(search(7,L1)))
print("search(8,L1)={}".format(search(8,L1)))
print("search(9,L1)={}".format(search(9,L1)))
print("search(10,L1)={}".format(search(10,L1)))

print("Questioon G.2")
def f(T,i):
    indice = i
    m = T[i]
    for k in range(i+1, len(T)):
        if T[k] < m:
            indice = k
            m = T[k]
    return indice


print ("f([ 7, 3, 1, 8, 19, 9, 3, 5 ], 0)={}".format(f([ 7, 3, 1, 8, 19, 9, 3, 5 ], 0)))

print("F.5")

L=[]
i=1
while i<11:
    L.append(5*i)
    i+=2

print(L)

print("F.6")
def maxi(x,y) :
    m = (x-y+abs(x+y))/2
    print("x-y={}".format(x-y))
    print("abs(x+y)={}".format(abs(x+y))
    print("x-y+abs(x+y))={}".format(x-y+abs(x+y)))
    print("(x-y+abs(x+y))/2)={}".format((x-y+abs(x+y))/2))
    return m

print("maxi(3,-2)={}".format(maxi(3,-2)))
print("maxi(2,2)={}".format(maxi(2,2)))
print("maxi(3,2)={}".format(maxi(3,2)))
print("maxi(2,3)={}".format(maxi(2,3)))

pause()
pause()
