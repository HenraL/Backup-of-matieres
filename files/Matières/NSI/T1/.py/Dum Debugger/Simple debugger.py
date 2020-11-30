string=str("(('eeee')")
opbrack=[]
cbrack=[]
move=[]
opbraCk=0
cbraCk=0
error="^"
spaces=""
for i in string:
    if i=="(":
        opbraCk+=-1
        opbrack.append(opbraCk)
        move.append(opbraCk)
        cbrack.append(0)
    elif i==")":
        cbraCk+=1
        opbrack.append(0)
        move.append(cbraCk)
        cbrack.append(cbraCk)
    else:
        opbrack.append(0)
        move.append(0)
        cbrack.append(0)

#print(opbrack)
#print(move)
#print(cbrack)

if opbrack<cbrack:
    i=0
    contiinue=True
    while contiinue==True:
        if opbraCk==move[i]:
            print("{}\n{}{}".format(string,spaces,error))
            contiinue=False
        else:
            spaces+=" "
        i+=1
elif opbrack>cbrack:
    i=0
    contiinue=True
    while contiinue==True:
        if cbraCk==move[i]:
            print("string\n{}{}".format(spaces,error))
            contiinue=False
        else:
            spaces+=" "
        i+=1
