class start:
    def __init__(self,file):
        self.file=file
        self.new_line="<"
        self.new_command=">"
        self.end_for_type=""
    def file(file,level,content=""):
        if level=="r":
            f=open(file,level)
            e=f.read()
            f.close()
        else:
            f=open(file,level)
            f.write(str(content))
            f.close()
        return e
    def make_and_type(content,new_line,new_command,end_for_type):
        command_line,code,code_type,temp_line=[],[],[],[]
        command_line_type={}
        B=e=g=INDEX=0
        for  i in content:
            if i==new_line:
                for b in range(len(temp_line)):
                    code.append(temp_line[b])
                #print(f"temp_line={temp_line}")
                temp_line=[]
                for b in command_line_type:
                    code_type.append({f"{b}":f"{command_line_type[b]}","line_index":INDEX,"type":f"{command_line_type[b]}","taken":False})
                #print(f"command_line_type={command_line_type}")
                command_line_type={}
                INDEX+=1
            elif i==new_command and B==1:
                the_type=""
                A=0
                print(f"g={g}:i={e}: command_line={command_line}\ni={i}")
                for b in command_line:
                    if b==end_for_type and A==1:
                        A==2
                        break
                    elif A==1:
                        the_type+=b
                    elif b==new_command:
                        A=1
                print(f"the_type={the_type}")
                temp_line.append(command_line)
                command_line_type[command_line]=the_type
                command_line=i
                g+=1
            elif i==new_command and B==0:
                command_line=i
                B=1
            else:
                command_line+=i
            e+=1
        RI.code_type=code_type
        print(f"\n\ncode={code}\n\n")
        print(f"code_type={code_type}\n\n")
        return code,code_type
    def treat_link(lst):
        temp=[]
        code_type=[]
        RI.a_s=[]
        word=word1=word2=""
        a_s_cut=[]
        to_eject=[]
        shift1="\""
        shift2=">"
        boot1="="
        boot2="\""
        for i in range(len(lst)):
            print(f"len(lst[{i}])>0={len(lst[i])>0},len({lst[i]})")
            if len(lst[i])>0:
                code_type.append({str(lst[i]):f"{lst[i][0]}","taken":False})
                temp.append(lst[i])
            else:
                to_eject.append(i)
        print(f"code_type={code_type}")
        for i in range(len(temp)):
            print(f"code_type[i][temp[i]]=='a'={code_type[i][temp[i]]=='a'},{code_type[i][temp[i]]}")
            if code_type[i][temp[i]]=="a":
                code_type[i]["taken"]=True
                RI.a_s.append(temp[i])
        print(f"RI.as={RI.a_s}")
        a_s=[]
        for i in range(len(RI.a_s)):a_s.append(RI.a_s[i])
        for i in range(len(a_s)):
            print(f"a_s[{i}]={a_s[i]}")
            A=0
            for b in range(len(a_s[i])):
                #print(f"a_s[{i}][{b}]]={a_s[i][b]}")
                #if a_s[i][b]==shift2:
                #    word2=word
                #    a_s_cut.append({"link":word1,"name":word2})
                #    word=word1=word2=""
                if A==3:
                    A=0
                elif a_s[i][b]==shift1 and a_s[i][b+1]==shift2:#el
                    word1=word
                    word=""
                    A=3
                elif A==1:
                    word=""
                    A=2
                elif A==2:
                    word+=str(a_s[i][b])
                elif a_s[i][b]==boot1 and a_s[i][b+1]==boot2:
                    A=1
                else:
                    word+=str(a_s[i][b])
            word2=word
            a_s_cut.append({"link":word1,"name":word2})
            word=word1=word2=""
            
        return a_s_cut
    def write_findings(file):
        links=""
        names=""
        for i in range(len(file)):
            links+=f"{file[i]['link']}\n"
            names+=f"{file[i]['name']}\n"
        start.file("links.csv","w",links)
        start.file("names.txts","w",names)
    def Boot(self,file):
        file_content=start.file(file,"r")
        print(f"file_content={file_content}")
        #self.c=start.make_and_type(content=file_content,new_line=self.new_line,new_command=self.new_command,end_for_type=self.end_for_type)
        self.c=file_content.split(self.new_line)
        print(f"c={self.c}")
        self.ascut=start.treat_link(self.c)
        print(f"ascut={self.ascut}")
        start.write_findings(self.ascut)
file="to_take.txt"
RI=start(file)
RI.Boot(file)#file)
