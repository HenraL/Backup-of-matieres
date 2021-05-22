def factorielle(n):
    if n>0:
        return n*factorielle(n-1)
    else:
        return 1

print("factorielle(5)={}".format(factorielle(5)))
print("factorielle(4)={}".format(factorielle(4)))
print("factorielle(3)={}".format(factorielle(3)))
print("factorielle(2)={}".format(factorielle(2)))
print("factorielle(1)={}".format(factorielle(1)))
print("factorielle(0)={}".format(factorielle(0)))