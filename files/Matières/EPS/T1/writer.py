class root:
    def __init__(self): #-> None
        self.Turn=0
        self.gender=None
        self.Rmc=["---------Choisissez un élément---------","0","1","2"] #Recovery_main_corresponds
        self.PGmc=["---------Choisissez un élément---------","0","2","4"] #Project_Gap_main_corresponds
        self.TG=["---------Choisissez un élément---------","9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25"]
        self.TB=["---------Choisissez un élément---------","7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31"]
        self.actTimeTurn_results=""
        self.BigRounds=1
        self.Turns=0
        self.ShowList=""
        self.actTimeTurn_results=""
        self.chosenList=[]
        self.lists=[["---------Choisissez un élément---------","0","1","2"],["---------Choisissez un élément---------","0","2","4"],["---------Choisissez un élément---------","9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25"],["---------Choisissez un élément---------","7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31"]]
        self.messages=["Tour n°1","Tour n°2","Tour n°3","Ecart Projet","Récupération"]



class test(root):
    def actTimeTurn(self):
        chosenList=[]
        if self.ShowList==5:
            chosenList=self.lists[0]#self.Rmc
            self.cL=chosenList
        elif self.ShowList==4:
            chosenList=self.lists[1]
            self.cL=chosenList
        elif self.ShowList<3:
            if self.gender=="Female":
                chosenList=self.lists[2]#self.TG
                self.cL=chosenList
            elif self.gender=="Male":
                chosenList=self.lists[3]#self.TB
                self.cL=chosenList
    def Test(self):
        for i in range(5):
            if i==0:
                self.ShowList=1
                self.gender="Female"
                test.actTimeTurn(self)
                print(self.cL)
            elif i==1:
                self.ShowList=2
                self.gender="Male"
                test.actTimeTurn(self)
                print(self.cL)
            elif i==2:
                self.ShowList=3
                test.actTimeTurn(self)
                print(self.cL)
            elif i==3:
                self.ShowList=4
                test.actTimeTurn(self)
                print(self.cL)
            elif i==4:
                self.ShowList=5
                test.actTimeTurn(self)
                print(self.cL)


T=test()
test.Test(T)