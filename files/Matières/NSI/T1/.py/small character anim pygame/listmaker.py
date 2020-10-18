def pause():pause=input("Press enter to continue")
def append(namee,string):
    f=open("result_{}.txt".format(namee),"a")
    f.write("{}".format(string))
    f.close()
def clean(namee):
    f=open("result_{}.txt".format(namee),"w")
    f.close()
def read(file,variable):
    try:
        f=open("{}".format(file), "r")
        variable=f.read()
        print(variable)
        f.close()
        return variable
    except:
        print("Sorry, couldn't find the file {}".format(fileOriginName))
        print("ending program")
        pause()
w=""" """
namee=""
variable=""
list=[]
namegiven=False
liiste=[]
# path="img/right_character/img"
path="img/The unknown thing/exported"
image=""
fileOriginName=input("Please specify the name of the file to read: ")
read(fileOriginName,variable)
try:
    f=open("{}".format(fileOriginName), "r")
    variable=f.read()
    print(variable)
    f.close()
    imageName=input("name the variable that will contain the image: ")
    for file in variable:
        if file!='\n':
            # print(file)
            image+=file
            # print("image={}".format(image))
        else:
            list.append("{}/{}".format(path,image))
            if namegiven==False:
                namee=image
                namegiven=True
            image=""
            # print("list={}\npath={}\nimage={}".format(list,path,image))
        #pause=input("Press enter to continue")
    #for i in range(len(list)):

    # print("namee={}".format(namee))

    clean("{}".format(namee))
    append(namee,w)
    finalList=[]
    finalListPure=[]
    for i in range(len(list)):
        finalList.append("{}{}=\"{}\"".format(imageName,i+1,list[i]))
        finalList.append("\"{}\"".format(list[i]))
        # finalListPure.append("{}{}".format(imageName,i+1))
        append(namee,"{}{}=\"{}\"\n".format(imageName,i+1,list[i]))

    append(namee,"{}={}".format(imageName,finalList))
    print(w)
    print("{}={}".format(imageName,finalList))
    print("Work finished, find the result in the file : result_{}.txt".format(namee))
    print("Program created by Henry Letellier")
    pause()
except:
    print("Sorry, couldn't find the file {}".format(fileOriginName))
    print("ending program")
    pause()

