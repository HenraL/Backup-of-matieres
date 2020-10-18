def fibo(n):
    if n==0 or n==1:
        return n
    else:
        calcule1=fibo(n-1)
        calcule2=fibo(n-2)
        return (calcule1+calcule2)

print(fibo(7))