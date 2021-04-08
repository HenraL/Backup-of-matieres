from tkinter import *
__Author__="Henry Letellier"
__credits__="Created by © Henry Letellier"
__Version__="1.0.0.0"
__To_quote__="__© Henry Letellier__"
DL0="Theses rules apply for all the files in this folder and sub-files in sub-folders."
DL1="This file contains a certain amount of variables for gathering info, about a windows computer, it is for educational purpose."
DL2="This program is to be used as if and without any guaranty."
DL3=f"The creator, {__To_quote__}, cannot be held responsible for any damage caused on your computer."
DL4="This program will do no harm to your computer."
DL5="This program, although no harm to your computer will be done will still expose sensitive content contained on your windows computer."
DL6="This program will also expose content from software it has been programmed to search."
DL7="This program also uses elements from other scripts, which (if the script itself and not the snipsets) could have a negative impact on your computer."
DL8="This program has does not require any other installation than python itself."
DL9="This program will automatically terminate if executed on a system other than windows."
DL10="It is authorised to use this program in other non harmful intension programs."
DL11=f"If this program happens to be used in another program, please quote it's author ({__To_quote__}). "
DL12="Please avoid running parts of this program (outside of itself) if you do not know what you are doing."
DL=[#DL0,
    DL1,DL2,DL3,DL4,DL5,DL6,DL7,DL8,DL9,DL10,DL11,DL12]
    #0  #1   #2  #3 #4  #5   #6  #7  #8  #9  #10  #11
__Description__=""
for i in range(len(DL)):__Description__+=f" {DL[i]}\n"

pfonty="Times New Roman"
pfontw="normal"
pfontb="bold"
pfonts=9
BGC="white"
FGC="black"

def refused():
    TT.destroy()
    TTT=Tk()
    TTT["bg"]="white"
    TTT.title("License")
    TTT.geometry(f"{x}x{y}")
    TTT.minsize(x,y)
    FrameText=Frame(TTT,borderwidth=0,relief=FLAT,bg="white")
    FrameText.pack(fill=X,side=TOP)
    FrameButt=Frame(TTT,borderwidth=0,relief=FLAT,bg="white")
    FrameButt.pack(fill=X,side=TOP)
    TITLE=Label(FrameText,text="You have refused to accept the license.",bg=BGC, font=(pfonty,pfonts,pfontw))
    TITLE.pack(fill=X,pady=0)
    TITLE2=Label(FrameText,text="This program is now aborting",bg=BGC, font=(pfonty,pfonts,pfontw))
    TITLE2.pack(fill=X,pady=0)
    boutonDeny=Button(FrameButt, text="Quit", command=TTT.destroy, font=(pfonty,pfonts,pfontw))
    boutonDeny.pack(anchor=CENTER)
    TTT.mainloop()
def accepted():
    TT.destroy()
    print("accepted")

def put_in_bold(line,string,var_for_insert,pfonty,pfonts,pfontb,style_index):
    default=[]
    this=0
    colum=0
    bold_index=0
    ab_index=0
    bold_word=""
    the_end=""
    the_beg=""
    
    for b in string:default.append(b)
    
    b=0
    while b<len(default):
        
        if this==2:
            the_end+=default[b]
            
        elif default[b]=="_" and default[b+1]=="_" and this==1:
            ab_index=b+4
            this=2
            b+=1
            
        elif this==1:
            bold_word+=default[b]
            
        elif default[b]=="_" and default[b+1]=="_" and this==0:
            bold_index=b+3
            this=1
            b+=1
            
        else:
            the_beg+=default[b]
            
        b+=1
        
    print(f"line={line}\ndefault=\n{default}\nthis={this}\ncolum={colum}\nbold_index={bold_index}\nab_index={ab_index}\nbold_word={bold_word}\nthe_end={the_end}\nthe_beg={the_beg}""")

    print(f"var_for_insert.insert(float(f\"{line}.{colum}\"),f\"b1 {the_beg}\")")
    var_for_insert.insert(float(f"{line}.{colum}"),f"{the_beg}")
    
    #var_for_insert.insert(index=float(f"{line}.{bold_index}"),text=f"{bold_word}\n",tags="boold")

    print(f"var_for_insert.insert(float(f\"{line}.{bold_index}\"),f\"b2 {bold_word}\",f\"boold{style_index}\")")
    var_for_insert.insert(float(f"{line}.{bold_index}"),f"{bold_word}",f"boold{style_index}")
    
    Test.tag_config(f"boold{style_index}",font=(pfonty,pfonts,pfontb))
    
    #Test.tag_config(f"boold{style_index}",background="blue")

    print(f"var_for_insert.insert(float(f\"{line}.{ab_index}\"),f\"b3 {the_end}\\n\",f\"nboold{style_index}\")")
    var_for_insert.insert(float(f"{line}.{ab_index}"),f"{the_end}\n",f"nboold{style_index}")
    
    Test.tag_config(f"nboold{style_index}",font=(pfonty,pfonts,pfontw))
    
    #Test.tag_config(f"nboold{style_index}",background="white")
    
def put_in_color(line,colum,string,var_for_insert,style_index,color,BGColor):
    default=[]
    this=0
    for b in string:default.append(b)
    var_for_insert.insert(float(f"{line}.{colum}"),f"{string}\n",f"red{style_index}")
    Test.tag_config(f"red{style_index}",background=f"{BGColor}",foreground=f"{color}")
    
x=730
y=420
TT=Tk()
TT["bg"]="white"
TT.title("License")
TT.geometry(f"{x}x{y}")
TT.minsize(x,y)
FrameText=Frame(TT,borderwidth=0,relief=FLAT,bg=BGC)
FrameText.pack(fill=X,side=TOP,pady=3)
FrameLicence=Frame(TT,borderwidth=0,relief=FLAT,bg=BGC)
FrameLicence.pack(fill=X,side=TOP)
FrameButt=Frame(TT,borderwidth=0,relief=FLAT,bg=BGC)
FrameButt.pack(fill=X,side=TOP,pady=10)
TITLE=Label(FrameText,text="Please read and accept this license before proceeding.",bg=BGC,fg=FGC,font=(pfonty,pfonts,pfontw))
TITLE.pack(fill=X,pady=0)
Test=Text(
    FrameLicence,
    bg=BGC,
    fg=FGC,
    cursor="X_cursor",
    state="normal",
    wrap="word",
    exportselection=0,
    width=500,#37,
    height=22,
    font=(pfonty,pfonts,pfontw),
    padx=5,
    pady=5)
infoCFG="white"
infoCBG="black"
Description=4
my_list=["About:",f"Version={__Version__}",f"Author={__Author__}",f"Credits={__credits__}"]
for i in range(len(my_list)):
    put_in_color(i+1,1,my_list[i],Test,f"a{i}\n",infoCFG,infoCBG)
put_in_color(i+len(my_list)+1,0,"Description:\n",Test,f"a{i}","Blue","yellow")
for i in range(len(DL)):
    if i==2 or i==10:
        put_in_bold(i+(len(my_list)+Description),f"{DL[i]}",Test,pfonty,pfonts,pfontb,i)
    elif i==8:
        put_in_color(i+(len(my_list)+Description),0,f"{DL[i]}",Test,i,"red",infoCFG)
    else:
        Test.insert(float(i+(len(my_list)+Description)),f"{DL[i]}\n")
#for i in range(20):
 #   put_in_color(i+(len(my_list)+Description)+len(DL),0," ",Test,f"z{i}",infoCBG,infoCFG)
    
#Test.config(state="disabled")
Test.pack()
boutonDeny=Button(FrameButt, text="Refuse", font=(pfonty,pfonts,pfontw), fg=FGC, command=refused)
boutonDeny.pack(side=LEFT, padx=5)
boutonAccept=Button(FrameButt, text="Accept", font=(pfonty,pfonts,pfontw), fg=FGC, command=accepted)
boutonAccept.pack(side=RIGHT,padx=5)
#TT.mainloop()
