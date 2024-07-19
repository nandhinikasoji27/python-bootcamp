 #person x goes to market buys 10 apples , 2 dozen banana ,8 oranges
#cost of 1 apples is 15rs
#cost of 1 banaba is 4rs
#1 orange is 5rs 700 is given by mother

n=int(input("how moch money do you have:"))
apple=int(input("no of apples:"))
banana=int(input("no of bananas:"))
orange=int(input("no of oranges:"))
sum=apple*15+banana*4+orange*5
print(sum)
if sum<n:
    print("not cheated")
else:
    print("cheated")
        
