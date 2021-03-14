accusatif=["durch","für","gegen","ohne","um"]
datif=["aus","bei","mit","nach","seit","von","zu"]
genitif=["außerhalb","ausserhalb","innerhalb","trotz","während","wegen"]
d_or_g=["an","auf","hinter","in","neben","über","unter","vor","zwischen"]
All=[]
for i in range(len(accusatif)):
	All.append(accusatif[i])
for i in range(len(datif)):
	All.append(datif[i])
for i in range(len(genitif)):
	All.append(genitif[i])
for i in range(len(d_or_g)):
	All.append(d_or_g[i])
text=input("Enter text to annalise:")+" "
words=[]
words_type={}
word=""
dots=commas=semi_colons=exclamation_marks=question_marks=colons=quote=brackets_open=brackets_closed=square_brackets_open=square_brackets_closed=asterix=slash=anti_slash=hashtag=0
for i in text:
	if i==" ":
		words.append(word)
		words_type[word]=""
		word=""
	else:
		if i==".":dots+=1
		elif i==",":commas+=1
		elif i==";":semi_colons+=1
		elif i=="!":exclamation_marks+=1
		elif i=="?":question_marks+=1
		elif i==":":colons+=1
		elif i=="\"":quote+=1
		elif i=="(":brackets_open+=1
		elif i==")":brackets_closed+=1
		elif i=="[":square_brackets_open+=1
		elif i=="]":square_brackets_closed+=1
		elif i=="*":asterix+=1
		elif i=="/":slash+=1
		elif i=="\\":anti_slash+=1
		elif i=="#":hashtag+=1
		else:word+=i
print("words={}, words_type={}".format(words,words_type))
print("dots={}, commas={}, semi_colons={}, exclamation_marks={}, question_marks={}, colons={},quote={},brackets_open={},brackets_closed={},square_brackets_open={},square_brackets_closed={},asterix={},slash={},anti_slash={},hashtag={}".format(dots,commas,semi_colons,exclamation_marks,question_marks,colons,quote,brackets_open,brackets_closed,square_brackets_open,square_brackets_closed,asterix,slash,anti_slash,hashtag))
options=["accusatif","datif","genitif","d_or_g"]
types={"accusatif":[],"datif":[],"genitif":[],"d_or_g":[]}
for i in range(len(words)):
        if words[i] in All:
                if words[i] in accusatif:
                        T=0
                        words_type[words[i]]=options[T]
                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]]))
                        print(str(words[i])==str(types[options[T]]))
                        if len(types[options[T]])>0:
                                for b in types[options[T]]:
                                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]][b]))
                                        print(str(words[i])==str(types[options[T]][b]))
                                        if str(words[i])==str(types[options[T]][b]):
                                                types[options[T]][words[i]]+=1
                                        else:
                                                types[options[T]].append({"{}".format(words[i]):1})
                        else:
                                types[options[T]].append({"{}".format(words[i]):1})
                elif words[i] in datif:
                        T=1
                        words_type[words[i]]=options[T]
                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]]))
                        print(str(words[i])==str(types[options[T]]))
                        if len(types[options[T]])>0:
                                for b in types[options[T]]:
                                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]][b]))
                                        print(str(words[i])==str(types[options[T]][b]))
                                        if str(words[i])==str(types[options[T]][b]):
                                                types[options[T]][words[i]]+=1
                                        else:
                                                types[options[T]].append({"{}".format(words[i]):1})
                        else:
                                types[options[T]].append({"{}".format(words[i]):1})
                elif words[i] in genitif:
                        T=2
                        words_type[words[i]]=options[T]
                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]]))
                        print(str(words[i])==str(types[options[T]]))
                        if len(types[options[T]])>0:
                                for b in types[options[T]]:
                                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]][b]))
                                        print(str(words[i])==str(types[options[T]][b]))
                                        if str(words[i])==str(types[options[T]][b]):
                                                types[options[T]][words[i]]+=1
                                        else:
                                                types[options[T]].append({"{}".format(words[i]):1})
                        else:
                                types[options[T]].append({"{}".format(words[i]):1})
                elif words[i] in d_or_g:
                        T=3
                        words_type[words[i]]=options[T]
                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]]))
                        print(str(words[i])==str(types[options[T]]))
                        if len(types[options[T]])>0:
                                for b in types[options[T]]:
                                        print("words[i]={}, types[options[T]][b]={}".format(words[i],types[options[T]][b]))
                                        print(str(words[i])==str(types[options[T]][b]))
                                        if str(words[i])==str(types[options[T]][b]):
                                                types[options[T]][words[i]]+=1
                                        else:
                                                types[options[T]].append({"{}".format(words[i]):1})
                        else:
                                types[options[T]].append({"{}".format(words[i]):1})
print("options={}\ntypes={}\nwords_type={}\ntypes[\"{}\"]={}\ntypes[\"{}\"]={}\ntypes[\"{}\"]={}\ntypes[\"{}\"]={}".format(options,types,words_type,options[0],types[options[0]],options[1],types[options[1]],options[2],types[options[2]],options[3],types[options[3]]))
print("Created By Henry Letellier")
