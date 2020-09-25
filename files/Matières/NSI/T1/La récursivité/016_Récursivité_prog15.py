# def cpt(n):
#     if n>=0:
#         return n
#         cpt(n-1)
#         print(n)

# def fibo1(n):
#     cpt(n)
#     u,v,cpt=0,1,0
#     while cpt<n:
#         cpt(cpt)
#         u,v,cpt=v,u+v,cpt+1
#         return u
# print("fibo(400)={}\ncpt={}".format(fibo1(400),cpt(400)))

def fibo2(n):
    u,v=0,1
    for i in range(n):
        u,v=v,u+v
    return u

# print ("fibo2(400)={}".format(fibo2(400)))
print(fibo2(5))