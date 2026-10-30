'''
#write a program to change the first letter of the string 
a=input()
a="J"+a[1:]
print(a)


#string iteration using for loop
a=input()
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)
#write the program join two strings sample ip:hello ,world  op:hello world
a=input()
b=input()
print(a+" "+b)

#using join
a=input()
b=input()
print(" ".join([a,b]))

#write the program to toggle the cases in a string ip:HellO op:hELLo
a=input()
print(a.swapcase())

#write the program convert every word first letter as uppercase
a=input()
print(a.title())

#write the program print upper case letter count in given string
a=input()
count=0
for i in a:
    if i.isupper():
        count+=1
print(count)

#write a program check if the given string is alphanumeric or not
a=input()
le=num=False
for i in a:
    if  i.isalpha():
        le=True
    elif i.isdigit():
        num=True
if le and num:
    print("yes")
else:
    print("no")


#write the program check given string is palindrome or not
a=input()
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#write the program print count of words in given string ip:hello welcome students op:3
a=input()
print(len(a.split()))


#write a program to print only vowels in given string 
n=input()
a=["a","e","i","o","u","A","E","I","O","U"]
for i in n:
    if i in a:
        print(i)


#important:write the program check given string is anagram or not
f=input()
s=input()
f=f.replace(" ","").upper()
s=s.replace(" ","").upper()
if sorted(f)==sorted(s):
    print("true")
else:
    print("false")


#list:it is a collection of multiple data types
#list iteration using for loop
b=list(map(int,input().split()))
for i in range(len(b)):
    print(b[i],end=" ")

print()
for i in b:
    print(i,end=" ")

#write the program print sum of evenn numbers in list
a=list(map(int,input().split()))
s=0
for i in a:
    if i%2==0:
        s+=i
print(s)


#write the program to print second maximum element in given list
a=list(map(int,input().split()))
m=float('-inf')
sm=float('-inf')
for i in a:
    if i>m :
        sm=m
        m=i
    elif i<m and i>sm:
        sm=i
print(sm)


a=list(map(int,input().split()))
m=None
sm=None
for i in a:
    if m is None or i>m :
        sm=m
        m=i
    elif sm is None or i<m and i>sm:
        sm=i
print(sm)
'''

n=int(input())
if n>=1000:
    last=n%100
    first=n
    while first>=100:
        first=first//100
    print(first+last)
else:
    print("invalid")
