def toto():
    global n
    a=1
    n=n+1
    print(n,end=" ")
    res=toto()
    return

#programme principal:
n=0
res=toto()
