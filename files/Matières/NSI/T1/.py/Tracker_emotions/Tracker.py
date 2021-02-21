import turtle,os,datetime,tkinter
def pause():pause=input("Press enter to continue...")
DATE=datetime.datetime.now()
Questions_B_1={
"In general, to what extent do you lead a purposeful and meaningful life?":0,
"How much of the time do you feel you are making progress towards accomplishing your goals?":0,
"How often do you become absorbed in wht you are doing?":0,
"In general, how would you say your health is?":0,
"In general, how often do you feel joyful?":0,
"To what extent do you receive help and support from others when you need it?":0,
"In general, how often do you feel anxious?":0,
"How often do you achieve the important goals you have set for yourself?":0,
"In general, to what extent do you feel that what you do in your life is valuable and worthwhile?":0,
"In general, how often do you feel positive?":0,
"In general, to what extent do you feel exited and interested in things?":0,
"How lonely do you feel in your daily life?":0,
"How satisfied are you with your current physiscal health?":0,
"In general, how often do you feel angry?":0,
"To what extent do you feel loved?":0,
"How often are you able to handle your responsabilities ?":0,
"To what extent do you feel you have a sens of direction in your life?":0,
"Compared to others of your same age and sex, how is your health?":0,
"How satisfied are you with your personal relationships?":0,
"In general, how often do you feel sad?":0,
"How often do you lose track of time while doing something?":0,
"In general, to what extent do you feel contented?":0,
"Taking all things together, how happy would you say you are?":0}#1_to_10

#a="Text:"
#b="'(b)'Values:"
#c="(n)Scientific reasearch shows that when we don't live in accordance with our values, our well-being decreases. It is also the balance regarding the interplay of our values that dictates many of the actions we take in our lives."
#d="(n)(t)Please take a moment to think about who you are and what you value in life. Then read the following descriptions of different people. For each one, read the description, and then indicate how much the person in the description is like you."


#from 1 to 10
Questions_B_2_P_1={"WORK:":0,
                   "TIME BALANCE:":0,
                   "EDUCATION, ARTS & CULTURE:":0,
                   "ACHIEVEMENT:":0,
                   "MATERIAL WELL-BEING:":0,
                   "HEALTH:":0,
                   "GOOD TIMES:":0,
                   "HELPING OTHERS:":0,
                   "SECURITY:":0,
                   "NATURE:":0,
                   "FAMILY":0,
                   "SPIRITUALITY:":0,
                   "OTHER:":0}
                   
Questions_B_2_P_2=["This person enjoys working hard, finding a lot of meaning in daily activities, wether paid employement or unpaid activities.",
"This person enjoys keeping a balance between work, family, and social aspects of life, allowing for time for excitement, rest, and stimulation.",
"This person enjoyes learning. He or she likes to visit museums and other cultural centers, or engage in artisic pursuits.",
"This person like to have people recognize his or her achievements. Being very successful is important to this person.",
"This person likes to have a lot of money and expensive things. It is important for this person to be rich.",
"This person like to engage in healthy behaviors. Staying physically or mentally fit is important to this person.",
"This person likes to have a good time, doing things that make him or her feel throughout the day.",
"This person likes to care for and help others.",
"This person likes to avoid anything that might be dangerous. It is important to live in secure surroundings and feel safe.",
"This person likes to spend time in nature. He or she seeks out green spaces, and strives to care for natural resources.",
"This person likes to spend time with his or her family. Filing family needs is important to this person.",
"This person feels connected to something higher than him- or herself. Feelings of spirituality or religious or spiritual practices are important to this person.",
"Values not listed here."]
#main menu
class ShowStats:
    def __init__(self):
        self.numbers={}
        self.colour=["#407294","#ff4a4a","#0660bd","#754a6c","#9e9e8b","#00008B","#B8860B","#8B0000","#B22222","#808080","#FF69B4","#4B0082","#778899","#800000","#0000CD","#BA55D3","#9370DB","#3CB371","#7B68EE","#C71585","#191970","#000080","#808000","#FF4500","#DA70D6","#800080","#FF0000","#4169E1","#8B4513","#2E8B57","#6A5ACD","#708090","#4682B4","#008080","#EE82EE","#DDA0DD"]
        self.chosen=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
        self.questions=""
        self.T=turtle.Turtle()

    def pause():pause=input("Press enter to continue...")
    def sum_points_from_days(listday):
        total=0
        for i in range(len(listday)):
            total+=int(listday[i])
        return total
    def create_number(self):
        self.numbers={}
        c=10
        y=250
        for i in range(11):
            self.numbers[c]=y
            c-=1
            y-=50
        self.numbers[0]=-230
    def init(self,questions):
        self.T.speed(10)
        self.T.penup()
        self.T.goto(-250,250)
        self.T.write("Score")
        self.T.goto(-270,250)
        self.T.write("<--")
        self.T.goto(-300,250)
        y=200
        c=10
        for i in range(11):
            self.T.write(c)
            c-=1
            self.T.goto(-300,y)
            y-=50
        self.T.up()
        self.T.goto(-285,-250)
        self.T.down()
        self.T.width(5)
        self.T.goto(-285,260)
        self.T.up()
        self.T.goto(-310,-230)
        self.T.write(0)
        self.T.goto(-285,-230)
        self.T.down()
        self.T.goto(-310,-230)
        self.T.goto(310,-230)
        self.T.up()
        self.T.goto(280,-210)
        self.T.write("Days ")
        self.T.goto(0,225)
        self.T.write("Cathegorie:\nQuestions:{}".format(questions))
        y=-250
        x=-250
        for i in range(len(day_list)):
            self.T.goto(x,y)
            self.T.write("day{}".format(i+1))
            x+=50
    def test(day_data_list,data_index_to_show,day_list,numbers,colour,T,Width):
        T.width(Width)
        T.color(colour)
        y=-230
        x=-285
        T.goto(x,y)
        T.down()
        x=-250
        for i in range(len(day_data_list)):
            m=int(day_data_list[i][data_index_to_show])
            y=numbers[m]
            T.down()
            T.goto(x,y)
            T.circle(radius=2)
            T.up()
            x+=50
            y+=50
        T.write(data_index_to_show)
    def init_main(self):
        for i in range(len(self.chosen)):
            if i==len(self.chosen)-1:
                self.questions+="{}".format(self.chosen[i])
            else:
                if int(self.chosen[i])==21:
                    self.questions+="\n"
                self.questions+="{},".format(self.chosen[i])
        ShowStats.init(T,self.questions)
        colo=0
        for i in self.chosen:
            ShowStats.test(self.day_data_list,i,self.day_list,self.numbers,self.colour[colo],self.T,3)
            colo+=1

        pause()

def process_namefile(name):
    namefile=""
    for i in name:
        if i==" ":
            namefile+="_"
        else:
            namefile+=i
    return namefile
def check(question):
    cont=True
    while cont==True:
        answer=input("{}: (from 1 to 10)".format(question))
        try:
            answer=int(answer)
            bip=True
            while bip==True:
                if answer>=1 and answer<=10:
                    cont=bip=False
                else:
                    print("Please only enter a number above 0 and below 11")
                    bip=False     
        except:
            print("Please only enter a number")
    return answer

def test_path(path):
    if os.path.exists(path)==False:
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)
def write_info_to_file(liste):
    for i in liste:
        f.write("{}\n".format(liste[i]))
get_name=input("Please enter your name:")
nameFile=process_namefile(get_name)
CurrentDay="{}_{}_{}".format(DATE.day,DATE.month,DATE.year)
print("Welcome to the tracking program")
print("The following set of questions are to be answered by a number ranging from 1 to 10")
for i in Questions_B_1:
    answer=check(i)
    Questions_B_1[i]=answer

print("Text:")
print("Values:")
print("Scientific reasearch shows that when we don't live in accordance with our values, our well-being decreases.\n It is also the balance regarding the interplay of our values that dictates many of the actions we take in our lives.")
print("\tPlease take a moment to think about who you are and what you value in life.\n Then read the following descriptions of different people.\n For each one, read the description, and then indicate how much the person in the description is like you.")

c=0
for i in Questions_B_2_P_1:
    answer=check("{}\n{}".format(i,Questions_B_2_P_2[c]))
    Questions_B_2_P_1[i]=answer
    c+=1

filename="data_of_the_{}_by_{}.txt".format(CurrentDay,nameFile)
pathlist=["data",nameFile,filename]
for i in range(len(pathlist)-1):
    test_path(pathlist[i])
f=open("{}".format(pathlist[2]),"w")
f.write("{}/{}/{}\n".format(DATE.day,DATE.month,DATE.year))
write_info_to_file(Questions_B_1)
write_info_to_file(Questions_B_2_P_1)
f.close()
for i in range(len(pathlist)-1):
    os.chdir("..")
Show_Stats=input("Do you whish to show your stats? [(y)es/(n)o]").lower()
if Show_Stats=="y":
    ShowStats.init()
