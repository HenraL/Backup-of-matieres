def rebours(n):
    if n>=0:
        print(n)
        rebours(n-1)

rebours(5)
pause=input("appuyez sur entré pour continuer...")