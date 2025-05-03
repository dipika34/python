
n=int(input("enter a no:"))

temp = 0
for i in range(2,n):
    if(n % i == 0):
        temp=1
        break
if(temp == 0):
    print("prime")
else:
    print("not prime")