n = 4
n1=1
for i in range(n):
     for j in range(i,n):
       print(" ",end=" ")
     for j in range(i+1):
       print(n1,end=" ")
       n1+=1
     print()
