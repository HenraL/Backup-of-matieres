import os
a=os.listdir()
colum=0
progress=input("Do you wish to activate the info on the progres of the program? [(y)es/(n)o]").lower()
for i in range(len(a)):
    print("{} {}\t".format(i,a[i]),end="")
    if colum==2:
        colum=0
        print()
    colum+=1

b=int(input("\nEnter the index of the file to convert into a database:"))
c=a[b]
if progress=="y":
    print("Extracting the raw data from the file {}".format(c))
f=open(c,"r")
d=f.read()
f.close()
if progress=="y":
    print("Data Extracted")
#print(d)
e=input("Enter the character between the term and definition:")
f=input("Enter the character between each term/definition (enter ret to insert a python return '\\n'):")
if f=="ret":
    f="\n"
word=""
word2=""
temp=""
liste=[]
A=0
index=0
if progress=="y":
    print("Processing the data of the file",end="")
for i in d:
    #print("i={}".format(i))
    if i==f and A==1:
        #print('in if')
        word2=temp
        #print("word2={}".format(word2))
        liste.append({"index":index,"term":word,"definition":word2})
        #print("\"index\":{},\"term\":{},\"definition\":{}".format(index,word,word2))
        word=word2=temp=""
        A=0
        index+=1
        if progress=="y":
            print(".",end="")
    elif i==e and A==0:
        word=temp
        #print("word={}".format(word))
        temp=""
        A=1
    else:
        temp+=str(i)
        #print("temp={}".format(temp))
if progress=="y":
    print("[Done]")
liste.append({"index":index,"term":"Created by","definition":"Henry Letellier"})
#add function offer to change parting symbols (, ; \n ...)
j=input("Enter 0 to just write the list to a file.\nEnter 1 to specifie a specific character to put between the term and definitions:")
g=input("Enter the name of the file to write the results to:")
h=input("Enter the file extention (no . required):")
if j=="0":
    i=input("Enter the name of the list containing the processed data:")
    if progress=="y":
        print("List lenght={}\nWriting the processed data to the given file".format(len(liste)),end="")
    f=open("{}.{}".format(g,h),"w")
    f.write("{}=[".format(i))
    for i in range(len(liste)):
        f.write("{}".format(liste[i]))
        if progress=="y":
            print(".",end="")
    f.write("]")
    print("[Done]")
    f.close()
    if progress=="y":
        print("Data written")
else:
    k=input("Enter ret to insert a python return '\\n'\nEnter the character to insert between the term and the definition:")
    l=input("Enter ret to insert a python return '\\n'\nEnter the character to insert between each term/definition:")
    m=input("Do you wish to write the index for each line? [(y)es/(n)o]:").lower()
    if k.lower()=="ret":
        k="\n"
    if l.lower()=="ret":
        l="\n"
    if progress=="y":
        print("List lenght={}\nWriting the processed data to the given file".format(len(liste)),end="")
    f=open("{}.{}".format(g,h),"w")
    if m=="n":
        for i in range(len(liste)):
            f.write("{}{}{}{}".format(liste[i]["term"],k,liste[i]["definition"],l))
            if progress=="y":
                print(".",end="")
    else:
        for i in range(len(liste)):
            f.write("{}{}{}{}{}{}".format(liste[i]["index"],k,liste[i]["term"],k,liste[i]["definition"],l))
            if progress=="y":
                print(".",end="")

    f.close()
    if progress=="y":
        print("[Done]")
print("Finished")
print("Created by Henry Letellier")
