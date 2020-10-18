# Fn=Fn-1²+(n-2)F(n-2)-3Fn-3

def sq(n):
    if n==0 or n==1 or n==2:
        if n==0:
            n=1
            return n
        elif n==1:
            n=3
            return n
        elif n==2:
            n=1
            return n
    else:
        print(n)
        n=(sq(n-1)*sq(n-1))+((n-2)*(sq((n-2))))-(3*(sq(n-3)))
        return n

# F0,F1,F2=1,3,1
print("sq(3)={}".format(sq(3)))