# #replace the element in an array with avg of max and min element 

# sample input:
# 13 2 67 20 68
# 68+2=70==35
# 35 35 35 35 35 


n=list(map(int,input().split()))
maxi=n[0]
mini=n[0]
avg=0
for i in range(len(n)):
    if (n[i]>maxi):
        maxi=n[i]
for i in range(len(n)):
    if (n[i]<mini):
        mini=n[i]
avg=(maxi+mini)//2
for i in range(len(n)):
    n[i]=avg
print(n)    
