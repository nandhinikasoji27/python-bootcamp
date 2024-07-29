a=int(input())
b=int(input())
c,d=a,b
while b!=0:
    a,b=b,a%b
print((c*d)//a)    