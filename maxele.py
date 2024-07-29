n=list(map(int,input().split()))
maxi=n[0]
for i in range(len(n)):
    if (n[i]>maxi):
        maxi=n[i]
print(maxi)
