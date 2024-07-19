import math
n=int(input("enter a number"))
s=n
a=str(n)
r=0
d=0
while(n!=0):
    d=n%10
    r=r+int(math.pow(d,len(a)))
    n=n//10
if(r==s):
    print("it is armstrong number")
else:
    print("not a armstrong")