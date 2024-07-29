# #print the element in a particular index in cyclic  rotation
# #find the element present in k index
# #sample input: 3 6 8 4 61 2
# #k=3
# #sample op:4



# a=list(map(int,input().split()))
# k=int(input())
# n=k%len(a)
# print(a[n-1])

a=list(map(int,input().split()))
k=int(input())
n=k%len(a)
print(a[n])


