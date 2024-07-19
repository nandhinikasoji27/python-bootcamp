a=int(input("enter a number"))
b=int(input("enter a number"))
div=1
sum1=0
sum2=0
while div<=a//2:
    if a%div==0:
        sum1=sum1+div
    div+=1
div=1
while div<=b//2:
    if b%div==0:
        sum2=sum2+div
    div+=1
if(sum1==b and sum2==a):
    print("friendly")
else:
    print("not")
