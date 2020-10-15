def pause():pause=input("Press enter to continue")
def append(namee,string):
    f=open("result{}.txt".format(namee),"a")
    f.write("{}".format(string))
    f.close()
def clean(namee):
    f=open("result{}.txt".format(namee),"w")
    f.close()
def read(file,variable):
    f=open("lists.txt", "r")
    variable=f.read()
    print(variable)
    f.close()
    return variable
list=[]
namegiven=False
liiste=[]
path="img/right_character/img"
image=""
fileOriginName=input("Please specify the name of the file to read: ")
try:
    #read(fileOriginName,fole)
    f=open("lists.txt", "r")
    variable=f.read()
    print(variable)
    f.close()
except:
    print("Sorry, couldn't find the file {}".format(fileOriginName))
    print("ending program")
    pause()
iamgename=input("name the variable that will contain the image: ")
for file in fole:
    if file!='\n':
        print(file)
        image+=file
        print("image={}".format(image))
    else:
        list.append("{}/{}".format(path,image))
        if namegiven==False:
            namee=image
            namegiven=True
        image=""
        print("list={}\npath={}\nimage={}".format(list,path,image))
    #pause=input("Press enter to continue")
#for i in range(len(list)):
    
f=open("result{}.txt".format(namee),"a")
f.write("{}={}".format(namee,list))
f.close()
pause()
