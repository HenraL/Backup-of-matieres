import time, datetime
def write(r,d):
 f=open("Time1.log","a")
 f.write("round{}={}\n".format(r,d))
 f.close()
date=datetime.datetime.now()
f=open("Time1.log","a")
f.write("Date=\"{}/{}/{}\" Start Time=\"{}/{}/{}\"\nCreated By Henry Letellier\n".format(date.day,date.month,date.year,date.hour,date.minute,date.second))
f.close()
i=0
r=0
while i==0:
 d=time.time()
 write(r,d)
 time.sleep(1)
 r+=1
""" Created By Henry Letellier"""
