#find the element that is presemt in k+n index (k,n is given by user)  
#sample input:3 6 8 4 61 2
#k=3
#n=2
#sample output:2
#sample input:80 70 54 36 72
#k=3
#n=4
#op:error



a=list(map(int,input().split()))
n=int(input())
k=int(input())
for i in range(0,len(a)):
    print(a[k+n],end=" ")
    break