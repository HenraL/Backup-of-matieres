# F0=F1=1
# Fn=Fn-1+Fn-2
def fibonacci(n, boucle):
    if n==0 or n==1:
        boucle+=1
        n=1
        return n
    else:
        boucle+=1
        print("boucle={}".format(boucle))
        print("n={}".format(n))
        n=fibonacci(n-1,boucle)+fibonacci(n-2,boucle)
        return n

boucle=0
print("fibonacci(6)={}".format(fibonacci(7,0)))