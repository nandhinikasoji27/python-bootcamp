z=True
h=int(input("enter the height:"))
w=int(input("enter the weight:"))
if(h>140 and w%2==0 ):
    print("YOU ARE ELIGIBLE")
    x=True
h1=int(input("enter the height:"))
w1=int(input("enter the weight:"))
if((h1>118 and h1<148) and w1%7==0):
    print("YOU ARE ELIGIBLE")
    y=True
if(x==True and y==True and z==True):
    print("x,y,z travel  in the same plane")
else:
    print("no")
       
