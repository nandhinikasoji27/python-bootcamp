#find duplicate elements


n=list(map(int,input().split( )))
a=[]
b=[]
for element in n:
    if element in a and element not in b:
        b.append(element)
    else:
        a.append(element)
print(b)



