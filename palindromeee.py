n=int(input())
s=n
r=0
d=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(r==s):
    print("palindrome")
else:
    print("not a palindrome")
    