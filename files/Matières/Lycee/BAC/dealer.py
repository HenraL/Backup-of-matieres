import os
f=open("to_take.txt","r")
a="""{}""".format(f.read())
c=[]
for i in a:c.append(i)

def pause():pause=input("Appuyez sur entré pour continuer...")

i=0
A=0
link=""
definition=""
links=[]
descriptions=[]
maximum=len(c)
while i<maximum:
 if c[i]=="a" and c[i+1]==" " and c[i+1]=="h" and c[i+2]=="r" and c[i+3]=="e" and c[i+4]=="f" and c[i+5]=="=" and c[i+6]=="\"":
  A=1
  i+=7
 elif c[i]=="\"" and c[i+1]==">":
  A=2
  print("link={}".format(link))
  if len(link)>0:
      links.append(link)
      link=""
  i+=1
 elif A==1:
  print("link={} c[{}]={}".format(link,i,c[i]))
  link+=c[i]
 #elif c[i]=="<" and c[i+1]=="b" and c[i+2]==">":
 # A=2
 # i+=2
 elif c[i]=="<" and c[i+1]=="/" and c[i+2]=="a" and c[i+3]==">":
  A=0
  print("definition={}".format(definition))
  descriptions.append(definition)
  definition=""
  i+=3
 elif A==2:
  print("definition={} c[{}]={}".format(definition,i,c[i]))
  definition+=c[i]
 i+=1

#f=open("links.csv","w")
#for i in range(len(links)):
# f.write("{}\n".format(links[i]))

#f.close()
#f=open("names.txts","w")
#for i in range(len(descriptions)):
# f.write("{}\n".format(descriptions[i]))

#f.close()

print(descriptions)
pause()

print(links)
pause()
print("len(links)={}, len(descriptions)={}".format(len(links),len(descriptions)))
pause()
print("starting downloader.py")
#os.system("start downloader.py")
pause()
