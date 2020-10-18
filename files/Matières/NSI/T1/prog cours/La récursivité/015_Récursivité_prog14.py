from time import sleep
e,i,n=0,0,0
def suite(n):
    if n>=1:
        f=0
        while f<301:
            
            # fn=fn1+fnmin2
            n1=(n-1)
            n2=(n-2)
            N=n1+n2
            # global i
            # i+=1
            print("n={}".format(n))
            print("N={}".format(N))
            print("f={}".format(f))
            suite(n+1)
            # sleep(1)
            f+=1
            # return n #,i
    else:
        global e
        e+=1
        suite(n+1)
        sleep(1)
        return n,e


print(suite(2))
# print("nn={}".format(n))
print("e={},i={}".format(e,i))