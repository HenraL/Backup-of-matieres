def toto():
    a=5
    res=tata()
    print("adr2")
    return res

def tata():
    a=3
    res=titi()
    print ("adr3")
    return res

def titi():
    a=8
    print("je suis titi")
    res=10
    return res

a=50
res=toto()
print("adr1")
print ("res={}".format(res))