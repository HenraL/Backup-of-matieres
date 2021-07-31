import requests
from time import sleep
o=0
while o==0:
	f=open("MyWebsites.txt","r")
	e=f.read()
	f.close()
	r=e.split("\n")
	p=[]
	for i in range(len(r)):
		if r[i]=="":
			p.append(i)
	for i in range(len(p)):
		d=r.pop(p[i])
		print(f"d='{d}'")
	for i in range(len(r)):
		try:
			q=requests.get(r[i])
			print(f"q.status_code={q.status_code}")
		except:
			print("fail")
	sleep(1)