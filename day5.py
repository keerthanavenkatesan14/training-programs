'''
#Print Numbers from 1 to 10
for i in range(1,11):
    print(i)


#Print Numbers from N to 1 in Reverse Order
n=int(input("enter a number:"))
for i in range(n,0,-1):
    print(i)


 #Print All Even Numbers from 1 to N
n=int(input("enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")


# Print All Odd Numbers from 1 to N
n=int(input("enter a number:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")


#Find the Sum of Numbers from 1 to N
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)


#Print the Multiplication Table of a Given Number up to 10
n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")


# Print the Squares and cube of Numbers from 1 to N
n=int(input("enter a number:"))
for i in range(1,n+1):
    #print(i*i)
    print(i*i*i,end=" ")


#Find the Sum of All Even Numbers from 1 to N
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if i%5==0:
        count+=1
print(count)


#Find the Sum of Numbers Divisible by Both 3 and 5 Between 1 and N
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        sum+=i
print(sum)


#Find the Sum of All Even Numbers from 1 to N
sum=0
for i in range(1,11):
    if i%2==0:
        sum+=i
print(sum)


#Find the Product of All Numbers from 1 to N
n=int(input("enter a number:"))
product=1
for i in range(1,n+1):
    product*=i
print(product)


#Find the Factorial of a Given Number
n=int(input("enter a number:"))
factorial=1
if n<0:
    print("factorial does not exist for negative numbers")
elif n==0: 
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial*=i
    print(factorial)


#Print All Factors of a Given Number
n=int(input("enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")


#Check Whether a Given Number Is a Perfect Number
n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")

    
#Check Whether a Given Number Is Prime
n=int(input("enter a number:"))
is_prime=True
if n<2:
    is_prime=False
else:
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
if is_prime:
    print("prime number")
else:
    print("not a prime number")

    
#Print the Fibonacci Series for N Terms
n=int(input("enter a number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


#Calculate the Power of a Number Without Using the Exponential Operator
n=int(input("enter a number:"))
p=int(input("enter the power:"))
result=1
for i in range(p):
    result*=n
print(result)


#Print All Perfect Squares Between 1 and N
n=int(input("enter a number:"))
for i in range(1,n+1):
    if i*i<=n:
        print(i*i,end=" ")



#digit manupulation.write the program print count of the given digit or length of given digit sample i/p:1496 op:4(w/o converting string or list)
n=int(input())
c=0
while n>0:
    c+=1
    n//=10
print(c)


#print sum of digits ip:1234 op:10
n=int(input())
c=0
while n>0:
    c+=(n%10)
    n//=10
print(c)
'''

#print count of even digits in gn input sample ip:4362 op:3, ip:111 op:0
n=int(input())
c=0
while n>0:
    r=n%10
    if r%2==0:
        c+=1
    n//=10
print(c)
