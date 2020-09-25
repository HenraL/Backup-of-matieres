Wriite=""
def importlist():
    print("Work in progress.")
def Cleaner():
    f=open("list.txt","w")
    f.write("")
    f.close()

def writer(Wriite):
    f=open("list.txt","a")
    f.write("{}".format(Wriite))
    print(Wriite)
    f.close()


def showcontent():
    f=open("list.txt","r")
    content=f.read()
    f.close()
    for Ii in range(content):
        
    print(content)
    return content

def log(a):
    f=open("log.txt","a")
    f.write(a)
    f.close()

def pause():
    pause=input("Press enter to continue...")

def adcall(dates):
    contiinue="go"
    while contiinue=="go":
        termgood="no"
        while termgood=="no":
            currentterm=input("enter st to exit this section\nPlease enter your term:")
            if currentterm=="st":
                contiinue="st"
                break
            else:contiinue="go"
            print("You have entered : {}".format(currentterm))
            answeredcorrectly="n"
            while answeredcorrectly=="n" and contiinue=="go":
                # termgod=input("Do you whant to change your term? [(y)es/(n)o]")
                termgod="n"
                if termgod=="y" or termgod=="Y":
                    answeredcorrectly="y"
                    continue
                elif termgod=="n" or termgod=="N":answeredcorrectly,termgood="y","Yes"
                else: 
                    print("Please ensure you have either entered y or Y for yes or n or N for no\nYou have entered: '{}'".format(answeredcorrectly))
                    pause()
                    continue
        definitiongood="no"
        while definitiongood=="no" and contiinue=="go":
            currrentdefinition=input("Please enter your definition:")
            print("You have entered : {}".format(currrentdefinition))
            answeredcorrectly="n"
            while answeredcorrectly=="n":
                # definitiongod=input("Do you whant to change your definition? [(y)es/(n)o]")
                definitiongod="n"
                if definitiongod=="y" or definitiongod=="Y":
                    answeredcorrectly="y"
                    continue
                elif definitiongod=="n" or definitiongod=="N":answeredcorrectly,definitiongood="y","Yes"
                else: 
                    print("Please ensure you have either entered y or Y for yes or n or N for no\nYou have entered: '{}'".format(answeredcorrectly))
                    pause()
                    continue
        if contiinue=="go":
            MAX=len(dates)
            if MAX==0:
                currentindex=0
            else:                
                currentindex=MAX
            dates.append({"term":"{}".format(currentterm),"definition":"{}".format(currrentdefinition),"index":"{}".format(currentindex)})
            global Wriite
            Wriite+="{};{};{}\n".format(currentterm,currrentdefinition,currentindex)
        else:contiinue="st"
    return dates, Wriite

def targeteddelete(dates):
    delete="yes"
    while delete=="yes":
        DEL=input("Show the list (S) Delete a line from the list (D) Exit (E)")
        if DEL=="S" or DEL=="s":
            for II in range(len(dates)):
                print("line number:{} term:{} definition:{}".format(II,dates[II]["term"],dates[II]["definition"]))
        elif DEL=="D" or DEL=="d":
            DDELETE="yes"
            while DDELETE=="yes":
                DELETE=input("Please enter the line number you whant to delete:")
                if DELETE.isnumeric()==True:
                    DELETE=int(DELETE)
                    DELETEMAKESURE=input("Are you sure you whant to delete the line n°{} corresponding to {}={}? [(y)es/(n)o]".format(DELETE,dates[DELETE]["term"],dates[DELETE]["definition"]))
                    if DELETEMAKESURE=="y" or DELETEMAKESURE=="Y":
                        try:
                            del dates[DELETE]
                            print("The line {} has successfully been deleted.".format(DELETE))
                        except:
                            print("Failed to delete the line {}.".format(DELETE))
                            for II in range(len(dates)):
                                print("line number:{} term:{} definition:{}".format(II,dates[II]["term"],dates[II]["definition"]))
                        DDELETE="no"
                    elif DELETEMAKESURE=="n" or DELETEMAKESURE=="N":
                        print("Delete aborted")
                        maiinmenu=input("Do you whish to return to the main menu? [(y)es/(n)o]")
                        if maiinmenu=="y" or maiinmenu=="Y":
                            DDELETE="no"
                            delete="no"
                        elif maiinmenu=="n" or maiinmenu=="N":
                            DDELETE="no"
                        else:
                            print("Please ensure that you have either entered y or Y for yes or n or N for no.\nYou have entered '{}'".format(maiinmenu))
                            pause()
                            continue
                    else:
                        print("Please ensure that you have either entered y or Y for yes or n or N for no.\nYou have entered '{}'".format(DELETEMAKESURE))
                        pause()
                        continue
                else:
                    print("Please ensure that you have either entered a number from the list.\nYou have entered '{}'".format(DELETEMAKESURE))
                    pause()
                    continue
        elif DEL=="E" or DEL=="e":delete="no"
        else:
            print("Please ensure that you have either typed S or S or d or D.\nYou have entered '{}'".format(DEL))
            pause()
            continue
dates=[]
{"date":"","event":"","index":""}

i="cont"
while i=="cont":
    action=input("afficher contenu de la liste (a), ajouter du contennu à la liste (b), supprimer du contenu de la liste (c), supprimer tout le contenu de la liste (d), supprimer tout le contenu du fichier (e), écrire la liste dans le fichier (f), importer le contenu de la liste dans le programme (i) quitter le programme (q)")
    if action=="a" or action=="A":
        showcontent()
        # print(content)
    elif action=="b" or action=="B":
        adcall(dates)
        print(dates)
        print(Wriite)
    elif action=="c" or action=="C":
        # c
        targeteddelete(dates)
    elif action=="d" or action=="D":
        # sd
        dates=[]
        print("The whole content of the list has been deleted.")
    elif action=="e" or action=="E":
        # sf
        Cleaner()
        print("The file has succesfully been cleaned")
    elif action=="f" or action=="F":
        # ef
        try:
            writer(Wriite)
            print("The file has succesfully been written to.")
        except:
            print("Failed to write to the file.")
        print(Wriite)
    elif action=="i" or action=="I":
        try:
            importlist()
            print("list successefully imported.")
        except:
            print("Failed to import list")
    elif action=="default":
        writer("zzzzzzz;z;30\naaaaaaa;a;31\nbbbbbbb;b;32\nccccccc;c;33\nddddddd;d;34\neeeeeee;e;35\nfffffff;f;36\nggggggg;g;37\nhhhhhhh;h;38\niiiiiii;i;39\njjjjjjj;j;40\nkkkkkkk;k;41\nlllllll;l;42\nmmmmmmm;m;43\nnnnnnnn;n;44\nooooooo;o;45\nppppppp;p;46\nqqqqqqq;q;47\nrrrrrrr;r;48\nsssssss;s;49\nttttttt;t;50\nuuuuuuu;u;51\nvvvvvvv;v;52\nwwwwwww;w;53\nxxxxxxx;x;54\nyyyyyyy;y;55\nzzzzzzz;z;56\n")

    elif action=="q" or action=="Q":
        i="quit"
    else:
        print("Please make sure you haven either entered a or A b or B c or C d or D e or E f or F i o I q or Q.\n You have entrerd '{}'".format(action))
        pause()
        print("Created by Henry Letellier")
        continue
