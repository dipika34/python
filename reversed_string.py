name = input("enter a string:")

temp = len(name)
# print(temp)

for  i in  range (1,temp+1):
    print(name[temp-i],end="")
