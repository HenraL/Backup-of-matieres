def toto():
    global a
    a=10
    print("Dans la fonction a={}".format(a))

a=5
toto()
print("A l'exterieur de la fonciton a={}".format(a))
