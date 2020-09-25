def pause():
    pause=input("pause")
f=open("liist.txt","r")
List=f.read()
f.close()
def read():
    f=open("liist.txt","r")
    List=f.read()
    f.close()
    return List
read()
print(List)
pause()
