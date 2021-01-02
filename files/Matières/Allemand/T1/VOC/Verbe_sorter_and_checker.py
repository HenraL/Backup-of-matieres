from tkinter import *
from random import randint
from time import sleep
import os
class root:
    def __init__(self):
        self.acorrect=0
        self.awrong=0
        self.givenanswer=0
        self.Background_colour="white"
        self.element=["term","definition"]
        self.Tbg="gray82" #lightGrey
        self.Tfg="black"
        self.Fbg="white"
        self.afg="blue"
        self.abg="gray82" #lightGrey
        self.cleanBackground="white"
        self.voc=[]
        self.Font="Times_New_Roman"
        self.Size=8
        self.WBG="Orange"
        self.FBG="White"
        self.LBG="grey"
        self.TBG="#f0f0f0"#"lightGrey"
        self.WFG="black"
        self.LFG="white"
        self.F1=FLAT
        self.F1T=RIDGE
        self.hfq="blue"
        self.hbq="green"
        self.BACKGround="#2CDF85"
        self.background=self.BACKGround
        self.watermark="{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(chr(169),chr(32),chr(67),chr(114),chr(233),chr(233),chr(32),chr(112),chr(97),chr(114),chr(32),chr(72),chr(101),chr(110),chr(114),chr(121),chr(32),chr(76),chr(101),chr(116),chr(101),chr(108),chr(108),chr(105),chr(101),chr(114))
        self.writecmdcont="cont"
        self.showerWindow="GRAPH"
        self.listOrd=['caractère: ,code:32', 'caractère:☺,code:9786', 'caractère:☻,code:9787', 'caractère:♥,code:9829', 'caractère:♦,code:9830', 'caractère:♣,code:9827', 'caractère:♠,code:9824', 'caractère:\n,code:10', 'caractère:♫,code:9835', 'caractère:☼,code:9788', 'caractère:►,code:9658', 'caractère:◄,code:9668', 'caractère:↕,code:8597', 'caractère:‼,code:8252', 'caractère:¶,code:182', 'caractère:§,code:167', 'caractère:▬,code:9644', 'caractère:↨,code:8616', 'caractère:↑,code:8593', 'caractère:↓,code:8595', 'caractère:→,code:8594', 'caractère:←,code:8592', 'caractère:∟,code:8735', 'caractère:↔,code:8596', 'caractère:▲,code:9650', 'caractère:▼,code:9660', 'caractère: ,code:32', 'caractère:!,code:33', 'caractère:",code:34', 'caractère:#,code:35', 'caractère:$,code:36', 'caractère:%,code:37', 'caractère:&,code:38', "caractère:',code:39", 'caractère:(,code:40', 'caractère:),code:41', 'caractère:*,code:42', 'caractère:+,code:43', 'caractère:,,code:44', 'caractère:-,code:45', 'caractère:.,code:46', 'caractère:/,code:47', 'caractère:0,code:48', 'caractère:1,code:49', 'caractère:2,code:50', 'caractère:3,code:51', 'caractère:4,code:52', 'caractère:5,code:53', 'caractère:6,code:54', 'caractère:7,code:55', 'caractère:8,code:56', 'caractère:9,code:57', 'caractère::,code:58', 'caractère:;,code:59', 'caractère:<,code:60', 'caractère:=,code:61', 'caractère:>,code:62', 'caractère:?,code:63', 'caractère:@,code:64', 'caractère:A,code:65', 'caractère:B,code:66', 'caractère:C,code:67', 'caractère:D,code:68', 'caractère:E,code:69', 'caractère:F,code:70', 'caractère:G,code:71', 'caractère:H,code:72', 'caractère:I,code:73', 'caractère:J,code:74', 'caractère:K,code:75', 'caractère:L,code:76', 'caractère:M,code:77', 'caractère:N,code:78', 'caractère:O,code:79', 'caractère:P,code:80', 'caractère:Q,code:81', 'caractère:R,code:82', 'caractère:S,code:83', 'caractère:T,code:84', 'caractère:U,code:85', 'caractère:V,code:86', 'caractère:W,code:87', 'caractère:X,code:88', 'caractère:Y,code:89', 'caractère:Z,code:90', 'caractère:[,code:91', 'caractère:\\,code:92', 'caractère:],code:93', 'caractère:^,code:94', 'caractère:_,code:95', 'caractère:`,code:96', 'caractère:a,code:97', 'caractère:b,code:98', 'caractère:c,code:99', 'caractère:d,code:100', 'caractère:e,code:101', 'caractère:f,code:102', 'caractère:g,code:103', 'caractère:h,code:104', 'caractère:i,code:105', 'caractère:j,code:106', 'caractère:k,code:107', 'caractère:l,code:108', 'caractère:m,code:109', 'caractère:n,code:110', 'caractère:o,code:111', 'caractère:p,code:112', 'caractère:q,code:113', 'caractère:r,code:114', 'caractère:s,code:115', 'caractère:t,code:116', 'caractère:u,code:117', 'caractère:v,code:118', 'caractère:w,code:119', 'caractère:x,code:120', 'caractère:y,code:121', 'caractère:z,code:122', 'caractère:{,code:123', 'caractère:|,code:124', 'caractère:},code:125', 'caractère:~,code:126', 'caractère:⌂,code:8962', 'caractère:€,code:8364', 'caractère:\ufffe,code:65534', 'caractère:‚,code:8218', 'caractère:ƒ,code:402', 'caractère:„,code:8222', 'caractère:…,code:8230', 'caractère:†,code:8224', 'caractère:‡,code:8225', 'caractère:ˆ,code:710', 'caractère:‰,code:8240', 'caractère:Š,code:352', 'caractère:‹,code:8249', 'caractère:Œ,code:338', 'caractère:Ž,code:381', 'caractère:‘,code:8216', 'caractère:’,code:8217', 'caractère:“,code:8220', 'caractère:”,code:8221', 'caractère:•,code:8226','caractère:–,code:8211', 'caractère:—,code:8212', 'caractère:˜,code:732', 'caractère:™,code:8482', 'caractère:š,code:353', 'caractère:›,code:8250', 'caractère:œ,code:339', 'caractère:ž,code:382', 'caractère:Ÿ,code:376', 'caractère:\xa0,code:160', 'caractère:¡,code:161', 'caractère:¢,code:162', 'caractère:£,code:163', 'caractère:¤,code:164', 'caractère:¥,code:165', 'caractère:¦,code:166', 'caractère:§,code:167', 'caractère:¨,code:168', 'caractère:©,code:169', 'caractère:ª,code:170', 'caractère:«,code:171', 'caractère:¬,code:172', 'caractère:\xad,code:173', 'caractère:®,code:174', 'caractère:¯,code:175', 'caractère:°,code:176', 'caractère:±,code:177', 'caractère:²,code:178', 'caractère:³,code:179', 'caractère:´,code:180', 'caractère:µ,code:181', 'caractère:¶,code:182', 'caractère:·,code:183', 'caractère:¸,code:184', 'caractère:¹,code:185', 'caractère:º,code:186', 'caractère:»,code:187', 'caractère:¼,code:188', 'caractère:½,code:189', 'caractère:¾,code:190', 'caractère:¿,code:191', 'caractère:À,code:192', 'caractère:Á,code:193', 'caractère:Â,code:194', 'caractère:Ã,code:195', 'caractère:Ä,code:196', 'caractère:Å,code:197', 'caractère:Æ,code:198', 'caractère:Ç,code:199', 'caractère:È,code:200', 'caractère:É,code:201', 'caractère:Ê,code:202', 'caractère:Ë,code:203', 'caractère:Ì,code:204', 'caractère:Í,code:205', 'caractère:Î,code:206', 'caractère:Ï,code:207', 'caractère:Ð,code:208', 'caractère:Ñ,code:209', 'caractère:Ò,code:210', 'caractère:Ó,code:211', 'caractère:Ô,code:212', 'caractère:Õ,code:213', 'caractère:Ö,code:214', 'caractère:×,code:215', 'caractère:Ø,code:216', 'caractère:Ù,code:217', 'caractère:Ú,code:218', 'caractère:Û,code:219', 'caractère:Ü,code:220', 'caractère:Ý,code:221', 'caractère:Þ,code:222', 'caractère:ß,code:223', 'caractère:à,code:224', 'caractère:á,code:225', 'caractère:â,code:226', 'caractère:ã,code:227', 'caractère:ä,code:228', 'caractère:å,code:229', 'caractère:æ,code:230', 'caractère:ç,code:231', 'caractère:è,code:232', 'caractère:é,code:233', 'caractère:ê,code:234', 'caractère:ë,code:235', 'caractère:ì,code:236', 'caractère:í,code:237', 'caractère:î,code:238', 'caractère:ï,code:239', 'caractère:ð,code:240', 'caractère:ñ,code:241', 'caractère:ò,code:242', 'caractère:ó,code:243', 'caractère:ô,code:244', 'caractère:õ,code:245', 'caractère:ö,code:246', 'caractère:÷,code:247', 'caractère:ø,code:248', 'caractère:ù,code:249', 'caractère:ú,code:250', 'caractère:û,code:251', 'caractère:ü,code:252', 'caractère:ý,code:253', 'caractère:þ,code:254', 'caractère:ÿ,code:255']
        self.listOrd=[{'caractère': ' ', 'code': 32}, {'caractère': '☺', 'code': 9786}, {'caractère': '☻', 'code': 9787}, {'caractère': '♥', 'code': 9829}, {'caractère': '♦', 'code': 9830}, {'caractère': '♣', 'code': 9827}, {'caractère': '♠', 'code': 9824}, {'caractère': '\n', 'code': 10}, {'caractère': '♫', 'code': 9835}, {'caractère': '☼', 'code': 9788}, {'caractère': '►', 'code': 9658}, {'caractère': '◄', 'code': 9668}, {'caractère': '↕', 'code': 8597}, {'caractère': '‼', 'code': 8252}, {'caractère': '¶', 'code': 182}, {'caractère': '§', 'code': 167}, {'caractère': '▬', 'code': 9644}, {'caractère': '↨', 'code': 8616}, {'caractère': '↑', 'code': 8593}, {'caractère': '↓', 'code': 8595}, {'caractère': '→', 'code': 8594}, {'caractère': '←', 'code': 8592}, {'caractère': '∟', 'code': 8735}, {'caractère': '↔', 'code': 8596}, {'caractère': '▲','code': 9650}, {'caractère': '▼', 'code': 9660}, {'caractère': ' ', 'code': 32}, {'caractère': '!', 'code': 33}, {'caractère': '"', 'code': 34}, {'caractère': '#', 'code': 35}, {'caractère': '$', 'code': 36}, {'caractère': '%', 'code': 37}, {'caractère': '&', 'code': 38}, {'caractère': "'", 'code': 39}, {'caractère': '(', 'code': 40}, {'caractère': ')', 'code': 41}, {'caractère': '*', 'code': 42}, {'caractère': '+', 'code': 43}, {'caractère': ',', 'code': 44}, {'caractère': '-', 'code': 45}, {'caractère': '.', 'code': 46}, {'caractère': '/', 'code': 47}, {'caractère': '0', 'code': 48}, {'caractère': '1', 'code': 49}, {'caractère': '2', 'code': 50}, {'caractère': '3', 'code': 51}, {'caractère': '4', 'code': 52}, {'caractère': '5', 'code': 53}, {'caractère': '6', 'code': 54}, {'caractère': '7', 'code': 55}, {'caractère': '8', 'code': 56}, {'caractère': '9', 'code': 57}, {'caractère': ':', 'code': 58}, {'caractère': ';', 'code': 59}, {'caractère': '<', 'code': 60}, {'caractère': '=', 'code': 61}, {'caractère': '>', 'code': 62}, {'caractère': '?', 'code': 63}, {'caractère': '@', 'code': 64}, {'caractère': 'A', 'code': 65}, {'caractère': 'B', 'code': 66}, {'caractère': 'C', 'code': 67}, {'caractère': 'D', 'code': 68}, {'caractère': 'E', 'code': 69}, {'caractère': 'F', 'code': 70}, {'caractère': 'G', 'code': 71}, {'caractère': 'H', 'code': 72}, {'caractère': 'I', 'code': 73}, {'caractère': 'J', 'code': 74}, {'caractère': 'K', 'code': 75}, {'caractère': 'L', 'code': 76}, {'caractère': 'M', 'code': 77}, {'caractère': 'N', 'code': 78}, {'caractère': 'O', 'code': 79}, {'caractère': 'P', 'code': 80}, {'caractère': 'Q', 'code': 81}, {'caractère': 'R', 'code': 82}, {'caractère': 'S', 'code': 83}, {'caractère': 'T', 'code': 84}, {'caractère': 'U', 'code': 85}, {'caractère': 'V', 'code': 86}, {'caractère': 'W', 'code': 87}, {'caractère': 'X', 'code': 88}, {'caractère': 'Y', 'code': 89}, {'caractère': 'Z', 'code': 90}, {'caractère': '[', 'code': 91}, {'caractère': '\\', 'code': 92}, {'caractère':']', 'code': 93}, {'caractère': '^', 'code': 94}, {'caractère': '_', 'code': 95}, {'caractère': '`', 'code': 96}, {'caractère': 'a', 'code': 97}, {'caractère': 'b', 'code': 98}, {'caractère': 'c', 'code': 99}, {'caractère': 'd', 'code': 100}, {'caractère': 'e', 'code': 101}, {'caractère': 'f', 'code': 102}, {'caractère': 'g', 'code':103}, {'caractère': 'h', 'code': 104}, {'caractère': 'i', 'code': 105}, {'caractère': 'j', 'code': 106}, {'caractère': 'k', 'code': 107}, {'caractère': 'l', 'code': 108}, {'caractère': 'm', 'code': 109}, {'caractère': 'n', 'code': 110}, {'caractère': 'o', 'code': 111}, {'caractère': 'p', 'code': 112}, {'caractère': 'q', 'code': 113},{'caractère': 'r', 'code': 114}, {'caractère': 's', 'code': 115}, {'caractère': 't', 'code': 116}, {'caractère': 'u', 'code': 117}, {'caractère': 'v', 'code': 118}, {'caractère': 'w', 'code': 119}, {'caractère': 'x', 'code': 120}, {'caractère': 'y', 'code': 121}, {'caractère': 'z', 'code': 122}, {'caractère': '{', 'code': 123}, {'caractère': '|', 'code': 124}, {'caractère': '}', 'code': 125}, {'caractère': '~', 'code': 126}, {'caractère': '⌂', 'code': 8962}, {'caractère': '€', 'code': 8364}, {'caractère': '\ufffe', 'code': 65534}, {'caractère': '‚', 'code': 8218}, {'caractère': 'ƒ', 'code': 402}, {'caractère': '„', 'code': 8222}, {'caractère': '…', 'code': 8230},{'caractère': '†', 'code': 8224}, {'caractère': '‡', 'code': 8225}, {'caractère': 'ˆ', 'code': 710}, {'caractère': '‰', 'code': 8240}, {'caractère': 'Š', 'code': 352},{'caractère': '‹', 'code': 8249}, {'caractère': 'Œ', 'code': 338}, {'caractère': 'Ž', 'code': 381}, {'caractère': '‘', 'code': 8216}, {'caractère': '’', 'code': 8217},{'caractère': '“', 'code': 8220}, {'caractère': '”', 'code': 8221}, {'caractère': '•', 'code': 8226}, {'caractère': '–', 'code': 8211}, {'caractère': '—', 'code': 8212}, {'caractère': '˜', 'code': 732}, {'caractère': '™', 'code': 8482}, {'caractère': 'š', 'code': 353}, {'caractère': '›', 'code': 8250}, {'caractère': 'œ', 'code': 339}, {'caractère': 'ž', 'code': 382}, {'caractère': 'Ÿ', 'code': 376}, {'caractère': '\xa0', 'code': 160}, {'caractère': '¡', 'code': 161}, {'caractère': '¢', 'code': 162}, {'caractère': '£', 'code': 163}, {'caractère': '¤', 'code': 164}, {'caractère': '¥', 'code': 165}, {'caractère': '¦', 'code': 166}, {'caractère': '§', 'code': 167}, {'caractère': '¨', 'code': 168}, {'caractère': '©', 'code': 169}, {'caractère': 'ª', 'code': 170}, {'caractère': '«', 'code': 171}, {'caractère': '¬', 'code': 172}, {'caractère': '\xad', 'code': 173}, {'caractère': '®', 'code': 174}, {'caractère': '¯', 'code': 175}, {'caractère': '°', 'code': 176}, {'caractère': '±', 'code': 177}, {'caractère': '²', 'code': 178}, {'caractère': '³', 'code': 179}, {'caractère': '´', 'code': 180}, {'caractère': 'µ', 'code': 181}, {'caractère': '¶', 'code': 182}, {'caractère': '·', 'code': 183}, {'caractère': '¸', 'code': 184}, {'caractère': '¹', 'code': 185}, {'caractère': 'º', 'code': 186}, {'caractère': '»', 'code': 187}, {'caractère': '¼', 'code': 188}, {'caractère': '½', 'code': 189}, {'caractère': '¾', 'code': 190}, {'caractère': '¿', 'code': 191}, {'caractère': 'À', 'code': 192}, {'caractère':'Á', 'code': 193}, {'caractère': 'Â', 'code': 194}, {'caractère': 'Ã', 'code': 195}, {'caractère': 'Ä', 'code': 196}, {'caractère': 'Å', 'code': 197}, {'caractère': 'Æ', 'code': 198}, {'caractère': 'Ç', 'code': 199}, {'caractère': 'È', 'code': 200}, {'caractère': 'É', 'code': 201}, {'caractère': 'Ê', 'code': 202}, {'caractère': 'Ë', 'code': 203}, {'caractère': 'Ì', 'code': 204}, {'caractère': 'Í', 'code': 205}, {'caractère': 'Î', 'code': 206}, {'caractère': 'Ï', 'code': 207}, {'caractère': 'Ð', 'code': 208}, {'caractère': 'Ñ', 'code': 209}, {'caractère': 'Ò', 'code': 210}, {'caractère': 'Ó', 'code': 211}, {'caractère': 'Ô', 'code': 212}, {'caractère': 'Õ', 'code': 213}, {'caractère': 'Ö', 'code': 214}, {'caractère': '×', 'code': 215}, {'caractère': 'Ø', 'code': 216}, {'caractère': 'Ù', 'code': 217}, {'caractère': 'Ú', 'code': 218}, {'caractère': 'Û', 'code': 219}, {'caractère': 'Ü', 'code': 220}, {'caractère': 'Ý', 'code': 221}, {'caractère': 'Þ', 'code': 222}, {'caractère': 'ß', 'code': 223}, {'caractère': 'à', 'code': 224}, {'caractère': 'á', 'code': 225}, {'caractère': 'â', 'code': 226}, {'caractère': 'ã', 'code': 227}, {'caractère': 'ä', 'code': 228}, {'caractère': 'å', 'code': 229}, {'caractère': 'æ', 'code': 230}, {'caractère': 'ç', 'code': 231}, {'caractère': 'è', 'code': 232}, {'caractère': 'é', 'code': 233}, {'caractère': 'ê', 'code': 234}, {'caractère': 'ë', 'code': 235}, {'caractère': 'ì', 'code': 236}, {'caractère': 'í', 'code': 237}, {'caractère': 'î', 'code': 238}, {'caractère': 'ï', 'code': 239}, {'caractère': 'ð', 'code': 240}, {'caractère': 'ñ', 'code': 241}, {'caractère': 'ò', 'code': 242}, {'caractère': 'ó', 'code': 243}, {'caractère': 'ô', 'code': 244}, {'caractère': 'õ', 'code': 245}, {'caractère': 'ö', 'code': 246}, {'caractère': '÷', 'code': 247}, {'caractère': 'ø', 'code': 248}, {'caractère':'ù', 'code': 249}, {'caractère': 'ú', 'code': 250}, {'caractère': 'û', 'code': 251}, {'caractère': 'ü', 'code': 252}, {'caractère': 'ý', 'code': 253}, {'caractère': 'þ', 'code': 254}, {'caractère': 'ÿ', 'code': 255}]
    def pause():
        pause=input("Press enter to continue...")
    def srint(t,e,et,s):
        if e==0:
            print(t)
            sleep(s)
        elif e==1:
            print(t,end="")
            sleep(s)
        elif e==2:
            print(t,end="{}".format(et))
            sleep(s)
class get(root):
    def no_blank_words(self):

        for i in range(len(self.voc)):
            if self.voc[i]["term"]=="" or self.voc[i]["term"]==None:
                entred=False
                while entred==False:
                    self.voc[i]["term"]=input("No term has been found for {} please enter it:".format(self.voc[i]["definition"]))
                    if len(self.voc[i]["term"])>0:
                        entred=True

            if self.voc[i]["definition"]=="" or self.voc[i]["definition"]==None:
                self.voc[i]["definition"]=input("No term has been found for {} please enter it:".format(self.voc[i]["term"]))
                entred=False
                while entred==False:
                    if len(self.voc[i]["definition"])>0:
                        entred=True
                    
    def treater(self):
        f=open(self.file,"r")
        c=f.read()
        f.close()
        word=term=definition=buff=""
        content=[]
        for i in c:content.append(str(i))
        for i in range(len(content)):
            if content[i]=="\n":
                definition=word
                self.voc.append({"term":"{}".format(term),"definition":"{}".format(definition)})
                term=definition=word=""
            elif (content[i]==" " and content[i+1]==self.symbol) or (content[i]==" " and content[i-1]==self.symbol):
                buff=content[i]
            elif content[i]==self.symbol:
                term=word
                word=""
            else:
                word+=content[i]
        # print(self.voc)
        get.no_blank_words(self)
        play.temp(self)
    
    def hiddenl():
        entred=False
        print("You have found a hidden part of the program.")
        while entred==False:
            doots=input("Enter un whole number (from 0 onwards):")
            try:
                doots=int(doots)
                entred=True
            except:
                print("I told you to enter a whole number that can be 0 or hiher.\nYou have entred '{}'".format(doots))
        entred=False
        while entred==False:
            symbol=input("Enter the character to display (enter s to enter an ascii code corresponding to the character):")
            if len(symbol)>1:
                print("I told you to enter 'the' character not 'the characters'.\nYou have entered {} characters.\nThese characters are {}.".format(len(symbol),symbol))
            elif len(symbol)==0:
                print("I told you to enter 'the' character not 'no characters'.\nYou have entered {} characters.".format(len(symbol)))
            elif symbol=="s" or symbol=="S":
                got_it=False
                while got_it==False:
                    spec=input("Enter List to se a small list of the ascii signification of letters.\nEnter the code of you're letter (can be optained by entering ord(\"<your character>\"):")
                    spec.lower()
                    if spec=="list":
                        line=colum=0
                        for i in "":
                            if colum==10:
                                print()
                                colum=0
                            else:
                                print("The symbol: {} Its Ascii: {}".format(i,ord(i)),end="")
                                colum+=1
                    else:
                        try:
                            spec=int(spec)
                            symbol=chr(spec)
                            got_it=True
                        except:
                            print("Are you sure you only entred the result generated by the comand ord(\"<your character>\")?\nYou have entered: {}".format(spec))
                            root.pause()
                
            else:entred=True
        lll=["l","o","a","d","i","n","g"," ","n","o","t","h","i","n","g",".",".","."]
        for i in range(len(lll)):root.srint(t="{}".format(lll[i]),e=1,et="",s=0.5)
        print("\n[",end="")
        for i in range(doots):
            root.srint(t="{}".format(symbol),e=1,et="",s=0.01)
        print("][Loaded]\n")

    def chosenfile(self):
        self.file=self.files[self.filename]
        print(self.file)
        def getContent():
            RI.symbol = myEntry.get()
            TT.destroy()
            get.treater(self)
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Quel est le symbole qui sépare le terme et sa définition.")
        TT.geometry("250x100")
        TT.minsize(250,100)
        #TT.iconbitmap(self.icon)
        Framemain = Frame(TT, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Framemain.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame1 = Frame(Framemain, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame1.pack(side=BOTTOM, padx=0, pady=0,fill=X)
        Frame2 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame2.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame3 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame3.pack(side=TOP, padx=0, pady=0,fill=X)
        ST=Label(Framemain, text="Veuillez entrer le symbole qui sépare le terme et sa définition:",wraplength=200,bg=self.cleanBackground)
        ST.pack(fill=X,pady=0,side=TOP)
        myEntry = Entry(Frame2, width=40)
        myEntry.pack(pady=0)
        btn = Button(Frame3, height=1, width=10, text="Valider",command=getContent, activeforeground=self.hfq)
        btn.pack(side=TOP)
        LC=Label(Frame3,text=self.watermark)
        LC.pack(side=RIGHT,pady=0)
        TT.mainloop()
    def hidden():
        entred=False
        print("You have found a hidden part of the program.")
        while entred==False:
            doots=input("Enter un whole number (from 0 onwards):")
            try:
                doots=int(doots)
                entred=True
            except:
                print("I told you to enter a whole number that can be 0 or hiher.\nYou have entred '{}'".format(doots))
        for i in range(doots):
            print(".",end="")

    def file_name(self):
        files=self.files=os.listdir()
        def chosenFile(*args):
            RI.filename = int(FIILE.get())
            TT.destroy()
            get.chosenfile(self)
        TT=Tk()
        # TT.geometry("500x200")
        TT['bg']=self.Background_colour
        TT.title("Quel fichier désirez-vous ouvrir?")
        LM=Label(TT,text="Quel fichier désirez-vous ouvrir?",bg=self.Tbg,fg=self.Tfg)
        LM.pack(side=TOP,fill=X)
        Frame1 = Frame(TT, borderwidth=2, relief=FLAT, bg="white")
        Frame1.pack(side=TOP, padx=10, pady=10)
        ligne=0
        colonne=0
        for I in range(len(files)):
            Label(Frame1, text="Index repère: {} nom du fichier: {} ".format(I,files[I]), borderwidth=1,bg="white").grid(row=ligne, column=colonne)
            if ligne==20:
                ligne,colonne=0,colonne+1
            else:ligne+=1
        bla = Label(TT, text="Quel fichier voulez-vous voir:")
        bla.pack(side=LEFT)
        FIILE=Spinbox(TT, from_=0, to=len(files)-1, increment=1)
        FIILE.pack(side=LEFT, padx=5)
        bouton=Button(TT, text="Ouvrir", command=chosenFile, activeforeground=self.afg,activebackground=self.abg,bg=self.Tbg,fg=self.Tfg)
        bouton.pack(side=LEFT, padx=5)
        TT.mainloop()

class create(root):
    def finished_message(self):
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Le fichier {} a été créé et rempli avec succès.".format(self.filename))
        TT.geometry("250x90")
        TT.minsize(250,90)
        #TT.iconbitmap(self.icon)
        Framemain = Frame(TT, borderwidth=0, relief=GROOVE)
        Framemain.pack(side=BOTTOM, padx=0, pady=0)
        Frame1 = Frame(Framemain, borderwidth=0, relief=GROOVE)
        Frame1.pack(side=BOTTOM, padx=0, pady=0)
        Frame3 = Frame(Frame1, borderwidth=0, relief=GROOVE)
        Frame3.pack(side=TOP, padx=0, pady=0)
        ST=Label(Framemain, text="Le fichier {} a été créé et rempli avec succès.".format(self.filename))
        ST.pack(fill=X,pady=0,side=TOP)
        btn = Button(Frame3, height=1, width=10, text="Fermer",command=TT.destroy, activeforeground=self.hfq)
        btn.pack(side=TOP)
        LC=Label(Frame3,text=self.watermark)
        LC.pack(side=RIGHT,pady=0)
        TT.mainloop()
    def file(self):
        print("create the file with name and elements")
        f=open(self.filename,"w")
        for i in range(len(termlist)):
            f.write("{}{}{}".format(term,separator,definition))
        f.close()
        f=open(self.filename,"r")
        print("Résultat:\n{}".format(f.read))
        f.close()
        create.finished_message(self)
    def name(self):
        """get file name"""
        def getContent():
            RI.symbol = myEntry.get()
            TT.destroy()
            get.treater(self)
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Quel est le symbole qui sépare le terme et sa définition.")
        TT.geometry("250x100")
        TT.minsize(250,100)
        #TT.iconbitmap(self.icon)
        Framemain = Frame(TT, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Framemain.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame1 = Frame(Framemain, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame1.pack(side=BOTTOM, padx=0, pady=0,fill=X)
        Frame2 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame2.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame3 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame3.pack(side=TOP, padx=0, pady=0,fill=X)
        ST=Label(Framemain, text="Veuillez entrer le symbole qui sépare le terme et sa définition:",wraplength=200)
        ST.pack(fill=X,pady=0,side=TOP)
        myEntry = Entry(Frame2, width=40)
        myEntry.pack(pady=0)
        btn = Button(Frame3, height=1, width=10, text="Valider",command=getContent, activeforeground=self.hfq)
        btn.pack(side=TOP)
        LC=Label(Frame3,text=self.watermark)
        LC.pack(side=RIGHT,pady=0)
        TT.mainloop()
    def content(self):
        print("get file content\nterm\ndefinition")
        def getContent():
            RI.symbol = myEntry.get()
            TT.destroy()
            get.treater(self)
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Quel est le symbole qui sépare le terme et sa définition.")
        TT.geometry("250x100")
        TT.minsize(250,100)
        #TT.iconbitmap(self.icon)
        Framemain = Frame(TT, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Framemain.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame1 = Frame(Framemain, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame1.pack(side=BOTTOM, padx=0, pady=0,fill=X)
        Frame2 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame2.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame3 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame3.pack(side=TOP, padx=0, pady=0,fill=X)
        ST=Label(Framemain, text="Veuillez entrer le symbole qui sépare le terme et sa définition:",wraplength=200)
        ST.pack(fill=X,pady=0,side=TOP)
        myEntry = Entry(Frame2, width=40)
        myEntry.pack(pady=0)
        btn = Button(Frame3, height=1, width=10, text="Valider",command=getContent, activeforeground=self.hfq)
        btn.pack(side=TOP)
        LC=Label(Frame3,text=self.watermark)
        LC.pack(side=RIGHT,pady=0)
        TT.mainloop()
    def separator(self):
        """get seperator for file coding"""
        def getContent():
            RI.symbol = myEntry.get()
            TT.destroy()
            get.treater(self)
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Quel est le symbole qui sépare le terme et sa définition.")
        TT.geometry("250x100")
        TT.minsize(250,100)
        #TT.iconbitmap(self.icon)
        Framemain = Frame(TT, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Framemain.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame1 = Frame(Framemain, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame1.pack(side=BOTTOM, padx=0, pady=0,fill=X)
        Frame2 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame2.pack(side=TOP, padx=0, pady=0,fill=X)
        Frame3 = Frame(Frame1, borderwidth=0, relief=GROOVE,bg=self.cleanBackground)
        Frame3.pack(side=TOP, padx=0, pady=0,fill=X)
        ST=Label(Framemain, text="Veuillez entrer le symbole qui sépare le terme et sa définition:",wraplength=200)
        ST.pack(fill=X,pady=0,side=TOP)
        myEntry = Entry(Frame2, width=40)
        myEntry.pack(pady=0)
        btn = Button(Frame3, height=1, width=10, text="Valider",command=getContent, activeforeground=self.hfq)
        btn.pack(side=TOP)
        LC=Label(Frame3,text=self.watermark)
        LC.pack(side=RIGHT,pady=0)
        TT.mainloop()
    
class play(root):
    def temp(self):
        c="cont"
        while c=="cont":
            d=input("1(writecmddt),2(writecmdtd),3(writecdmr):")
            try:
                d=int(d)
                if d==1:play.writecmddt(self)
                elif d==2:play.writecmdtd(self)
                elif d==3:play.writecmdr(self)
                c="not"
            except:
                print("error:\n{}".format(d))
                root.pause()

    def correct(self,answ,a):
        if self.showerWindow=="CMD":
            print("Well Done, You got the wright answer.\n{} Does correspond to {}".format(answ,a))
        else:
            aaaa = Tk()
            aaaa['bg']='white'
            aaaa.title("Correct")
            aaaa.geometry("250x200")
            aaaa.minsize(250,200)
            Frame1=Frame(aaaa, borderwidth=2, relief=self.F1, bg=self.FBG)
            Frame1.pack(side=TOP, expand=YES, pady=10, fill=X)
            #aaaa.iconbitmap("the icone of the software in.ico")
            aaaa.config(background="#2CDF85")
            label = Label(Frame1, text="Well Done, You got the wright answer.", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text="{}".format(answ), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text="Does correspond to ", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text=" {}".format(a), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            bouton=Button(aaaa, text="close", font=(self.Font,self.Size), bg=self.WBG, fg=self.WFG, command=aaaa.destroy ,activebackground=self.hbq, activeforeground=self.hfq)
            bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
            aaaa.mainloop()
    
    def wrong(self,answ,a,qu):
        if self.showerWindow=="CMD":
            print("Wrong\n\nBetter luck next time!\nYou chose: '{}' but the correct answer was '{}' and corresponded to '{}'.".format(answ,a,qu))
        else:
            aaaa = Tk()
            aaaa['bg']='white'
            aaaa.title("Wrong")
            aaaa.geometry("310x250")
            aaaa.minsize(310,250)
            Frame1=Frame(aaaa, borderwidth=2, relief=self.F1, bg=self.FBG)
            Frame1.pack(side=TOP, expand=YES, pady=10, fill=X)
            #aaaa.iconbitmap("the icone of the software in.ico")
            aaaa.config(background="#2CDF85")
            label = Label(Frame1, text="Wrong", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text="\n Better luck next time!", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text="You chose:", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text=" '{}'".format(answ), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text=" but the correct answer was ", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text="'{}'.".format(a), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text=" and corresponded to ", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            label = Label(Frame1, text="'{}'.".format(qu), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
            bouton=Button(aaaa, text="close", font=(self.Font,self.Size), bg=self.WBG, fg=self.WFG, command=aaaa.destroy ,activebackground=self.hbq, activeforeground=self.hfq)
            bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
            aaaa.mainloop()
    def cmdQ(self,qu,a):
        answ=input("A quoi correspond '{}'?".format(qu))
        if answ==a:
            play.correct(self,answ,a)
            self.acorrect+=1
            self.givenanswer+=1
        elif answ=="QuIt" or answ=="qUiT":play.goodbye(self)
        elif answ=="DoNt" or answ=="dOnT" or answ=="DoN't" or answ=="dOn'T":
            print("The answer was: {}".format(a))
            TypedIn=False
            while TypedIn==False:
                typeItIn=input("Please type in the answer for '{}':".format(qu))
                if typeItIn==a:
                    TypedIn=True
                else:
                    print("The answer was: {}".format(a))
        elif answ=="DoT" or answ=="dOt":get.hidden()
        elif answ=="LoAd" or answ=="lOaD":get.hiddenl()
        else:
            play.wrong(self,answ,a,qu)
            self.awrong+=1
            self.givenanswer+=1
            
    def options(self):
        print("to come in a future version")
        self.showerWindow="GRAPH"
    def writetd(self):
        print("coding in progress")
        self.showerWindow="GRAPH"
    def QMCtd(self):
        print("to fetch from an other program")
        self.showerWindow="GRAPH"
    def writedt(self):
        print("coding in progress")
        self.showerWindow="GRAPH"
    def QMCdt(self):
        print("to fetch from an other program")
        self.showerWindow="GRAPH"
    def writer(self):
        print("to come in a future version")
        self.showerWindow="GRAPH"
    def QMCr(self):
        print("to fetch from an other program")
        self.showerWindow="GRAPH"
    def writecmddt(self):
        print("coding in progress")
        self.showerWindow="CMD"
        self.writecmdcont="cont"
        for i in range(len(self.voc)):
            if self.writecmdcont=="cont":
                play.cmdQ(self,qu=self.voc[i][self.element[1]],a=self.voc[i][self.element[0]])
            else:
                print(i)
                break
    def writecmdtd(self):
        print("coding in progress")
        self.showerWindow="CMD"
        self.writecmdcont="cont"
        for i in range(len(self.voc)):
            if self.writecmdcont=="cont":
                play.cmdQ(self,qu=self.voc[i][self.element[0]],a=self.voc[i][self.element[1]])
            else:
                print(i)
                break
    def writecmdr(self):
        print("coding in progress")
        self.showerWindow="CMD"
        self.writecmdcont="cont"
        for i in range(len(self.voc)):
            if self.writecmdcont=="cont":
                c=randint(0,1)
                if c==1:
                    d=0
                else:
                    d=1
                play.cmdQ(self,qu=self.voc[i][self.element[c]],a=self.voc[i][self.element[d]])
            else:
                print(i)
                break
    def goodbye(self):
        self.writecmdcont="not"
        if self.acorrect==1:self.acs=""
        else:self.acs="s"
        if self.awrong==1:self.aws=""
        else:self.aws="s"
        if self.givenanswer==1:self.aqs=""
        else:self.aqs="s"
        if self.showerWindow=="CMD":
            print("Goodbye, see you next time. :-)\n\nYou have {} point{}.\nYou have made {} mistake{}.\nYou have answered {} question{}.".format(self.acorrect,self.acs,self.awrong,self.aws,self.givenanswer,self.aqs))
        else:
            print("Goodbye, See you next time")
            aaaa = Tk()
            aaaa['bg']='white'
            aaaa.title("Language:")
            aaaa.geometry("250x200")
            aaaa.minsize(250,200)
            #aaaa.iconbitmap("the icone of the software in.ico")
            # aaaa.config(background="#2CDF85")
            label = Label(aaaa, text="Goodbye, see you next time. :-)", font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
            label = Label(aaaa, text="You have {} point{}.".format(self.acorrect,self.acs), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
            label = Label(aaaa, text="You have made {} mistake{}.".format(self.awrong,self.aws), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
            label = Label(aaaa, text="You have answered {} question{}.".format(self.givenanswer,self.aqs), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)
            label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
            bouton=Button(aaaa, text="close", font=(self.Font,self.Size), bg=self.WBG, fg=self.WFG, command=aaaa.destroy ,activebackground=self.hbq, activeforeground=self.hfq)
            bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
            aaaa.mainloop()

RI=root()
get.file_name(RI)
