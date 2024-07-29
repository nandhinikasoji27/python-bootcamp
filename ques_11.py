# # find max element in given list

# n=list(map(int,input().split()))
# print(max(n))

n=list(map(int,input().split()))
maxi=n[0]
for i in range(len(n)):
    if (n[i]>maxi):
        maxi=n[i]
print(maxi)
