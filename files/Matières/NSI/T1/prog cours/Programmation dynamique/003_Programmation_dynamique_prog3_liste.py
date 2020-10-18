def fibo(n):
    global t
    print(n)
    if n==0 or n==1:
        t[n]=n
        return n
    elif t[n]>0:
        return t[n]
    t[n]=fibo(n-1)+fibo(n-2)
    return (t[n])

n=int(input("Entrer l'indice d'Un:"))
t=[0]*(n+1)
print(t)
print("resultat = ",fibo(n))
print(t)
# for N in range(n):
#     t=[0]*(N+1)
#     print(t)
#     print("resultat = ",fibo(N))
#     print(t)
