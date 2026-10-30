'''

#mirror number right angle pattern

n=int(input())
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print(" ")
#level 3 pattern write the program to print hollow square pattern 

n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*n)
    else:
        print("* "+"  "*(n-2)+"*")

#write a program to  print x pattern using * 
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")

#write a program to print +pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==(n//2)+1 or j==(n//2)+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#write a program to implement M pattern using *
n = int(input())

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or (i == j and i <= n // 2) or (i + j == n - 1 and i <= n // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()