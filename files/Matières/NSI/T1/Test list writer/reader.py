def Import():
    Import=open("liist.txt","r")
    List=Import.read()
    Import.close()
    return List, Import

def LMaker():
    Liist=""
    for I in List:
        if I==";":
            if semi==3:
                semi=0
            elif semi!=3:

                Liist+="\n"
        elif I=="\n":
            Liist+="},{"
        else:Liist+="I"
