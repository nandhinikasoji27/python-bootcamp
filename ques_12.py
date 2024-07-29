#print min num in a given list


n=list(map(int,input().split()))
min=n[0]
for i in range(len(n)):
    if (n[i]<min):
        min=n[i]
print(min)