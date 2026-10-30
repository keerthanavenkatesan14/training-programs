'''write the program print the given number type using match case and also check guven number is odd or even i/p:5 o/p:number 5 is positive and odd
a=int(input())
match a:
    case a if a%2==0 and a>0:
        print(f"number {a} is positive and even")
    case a if a%2==0 and a<0:
        print(f"number {a} is negative and even")
    case a if a%2!=0 and a<0:
        print(f"number {a} is negative and odd")
    case a if a%2!=0 and a>0:
        print(f"number {a} is positive and odd")
    case _:
        print(f"number {a} is zero and even")

#print sum of n natural numbers sample ip:5 op:15

n=int(input())
sum1=0
for i in range(1,n+1):
    sum1+=i
print(sum1)#because we need the single answer as sum

#write the program print only even numbers in given n natural numbers i/p:12 o/p:2,4,6,8,10,12
a=int(input())
for i in range (1,a+1):
    if i%2==0:
        print(i,end=" ")
    

#count the odd numbers in a given n natural numbers without using if 
n=int(input())
count=0
for i in range(1,n+1,2):
    count+=1
print(count)

#write the program print factorial value of a guven number ip:4 op:24
n=int(input())
a=1
for i in range(1,n+1):
    a=a*i
print(a)

'''
#write the program print the factors of a given numbers ip:10 op:1,2,5,10
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
