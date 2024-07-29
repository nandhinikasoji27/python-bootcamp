# n=8
# for i in range(2,n):
#     if(n%i==0):
#         print("not prime")
#         break
#     else:
#         print("prime")


# a=int(input("enter a number:"))
# r=a**0.5
# count=0
# for i in range(2,int(r+1)):
#     if a%i==0:
#         count=1
#         break
# if count==0 :
#     print(" not prime")
# else:
#     print(" prime")


a=int(input("enter a number:"))
r=a**0.5
count=0
if a==1:
    print("not a prime")
elif a==2:
    print("prime number")
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break
if count==0 :
    print(" not prime")
else:
    print(" prime")



    