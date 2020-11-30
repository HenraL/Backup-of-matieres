a=[]
i=float(5.25)
print(i)
#for e in range(5):
 #   i-=0.01
  #  print(i)

d1=4#6 #
d2=10
d3=10
for i in range(d1):
    for e in range(d2):
        for c in range(d3):
            v="{}'{}{}".format(i,e,c)
            a.append(v)
            print(v)

a.reverse()
print(a)
