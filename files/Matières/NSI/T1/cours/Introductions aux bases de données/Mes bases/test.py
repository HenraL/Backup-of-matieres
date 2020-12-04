#f=open("Les plus grandes viles d'Asie.txt","r")
originalfile="test"
FormAt="txt"
f=open("{}.{}".format(originalfile,FormAt),"r")
c=f.read()
f.close()
print(c)
word,t="",0
def clean(file,Format):
    f=open("{}_processed.{}".format(file,Format),"w")
    f.close()
def wrote(file,FoRmAt,element):
    f=open("{}_processed.{}".format(file,FoRmAt),"a")
    f.write(element)
    f.close()

#clean("Les_plus_grandes_viles_d'Asie","txt")
clean(originalfile,"txt")
	
for i in c:
    if i=="\n":
      e3=word
      #wrote("Les_plus_grandes_viles_d'Asie","txt","{}|{}|{}\n".format(e1,e2,e3))
      wrote(originalfile,"txt","{}|{}|{}\n".format(e1,e2,e3))
      e3=""
      word=""
      t=0
    elif i=="	":
        if t==0:
            e1=word
            t+=1
        elif t==1:
            e2=word
            t+=1
        else:
            word+=str(i)
    
    print("word=",word)
    print("i=",i)

#f=open("Les_plus_grandes_viles_d'Asie_processed.txt","r")
f=open("{}_processed.{}".format(originalfile,FormAt),"r")
d=f.read()
f.close()
print(d)
