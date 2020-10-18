def fibo3(n):
    if n==0 or n==1:
        return n
    else:
        print(n)
        return fibo3(n-1)+fibo3(n-2)

print(fibo3(5))