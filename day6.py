'''
#wite a program print tribonacci series 

n=int(input())
a,b,c=0,1,1
res=0
for i in range(3,n+1):
    res=a+b+c
    a=b
    b=c
    c=res
print(res)


#Write a program to count the number of digits in a given integer.
n=int(input())
if n==0:
  print(1)
else:
  c=0
  while n>0:
    c+=1
    n//=10
  print(c)



#write a program to find the sum of all even digits
n=int(input())
sum1=0
while n>0:
    r=n%10
    if r%2==0:
        sum1+=r
    n//=10
print(sum1)


#Write a program to find the product of all digits of a given integer.
n=int(input())
p=1
while n>0:
    r=n%10
    p*=r
    n//=10
print(p)


#Write a program to reverse a given integer.
n=int(input())
rev=0
while n>0:
  r=n%10
  rev=rev*10+r
  n//=10
print(rev)


#write a program to find the given number is palindrome or not
n=int(input())
n1=n
rev=0
palindrome=False
if n1==0:
  palindrome=True
while n>0:
  r=n%10
  rev=rev*10+r
  if rev==n1:
    palindrome=True
    break
  n//=10
if palindrome==True:
  print("Palindrome")
else:
  print("Not Palindrome")


#Write a program to find the first digit of a given number.
n=int(input())
while n>=10:
    n//=10
print(n)


#Write a program to check whether a number is a Strong number.
n=int(input())
n1=n
res=0
while n>0:
  r=n%10
  f=1
  for i in range(1,r+1):
    f=f*i
  res=res+f
  n//=10
if res==n1:
  print("Strong")
else:
  print("Not Strong")



#Write a program to check whether a given number is an Armstrong number or not.
n=int(input())
n1=n2=n
c,res=0,0
while n>0:
  c+=1
  n//=10
while n1>0:
  r=n1%10
  res=res+int(pow(r,c))
  n1//=10
if res==n2:
  print("Armstrong")
else:
  print("Not Armstrong")



#find gcd of two numbers using for and while loop get two numbers from user and find gcd of them
a=int(input())
b=int(input())
m1=min(a,b)
gcd=0
for i in range(1,m1+1):
  if a%i==0 and b%i==0:
    gcd=i
print(gcd)
while b!=0:
  c=a%b
  a=b
  b=c
print(a)


#Write a program to count how many zeros (0s) are present in a given number.
n=int(input())
c=0
if n==0:
  c+=1
while n>0:
  r=n%10
  if r==0:
    c+=1
  n//=10
print(c)


#write a python program to repeatedly ask the user to enter a password until the entered password is correct. The correct password is "python123".
pas="python123"
a=input()
while a!=pas:
  print("Incorrect")
  a=input()
print("pas is correct")


# A number is called Perfect if the sum of its proper divisors (excluding itself) is equal to the number.
num = int(input("Enter a number: "))
div_sum = 0
for i in range(1, num):
    if num % i == 0:
        div_sum += i
if div_sum == num:
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")


#Count How Many Times a Given Digit Occurs in an Integer
n=int(input())
key=int(input())
c=0
while n>0:
    r=n%10
    if r==key:
        c+=1
    n//=10
print(c)


#Repeatedly Divide a Number by 2 Until It Becomes 0 and Count the Number of Divisions
n=int(input())
c=0
while n>0:
    n=n//2
    c+=1
print(c)



#QUESTION 3: Display a Menu Repeatedly Until the User Chooses the Exit Option 
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = int(input("Enter your choice:\n"))

    if choice == 3:
        print("Exiting...")
        break


#pattern:write the program square pattern using * (box pattern)
n=int(input())
for i in range(n):
    print("*"*n)

#write the program print right angle triangle using *
n=int(input())
for i in range(1,n+1):
    print("*"*i)
    
# write the program print inverted right angle triangle 
n=int(input())
for i in range(n,0,-1):
    print("*"*i)

#write a program to print right angle tringle using number 
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
      print(j,end=" ")
    print("")

    
#write a program to print right angle triangle using numbers on incremental order
n=int(input())
c=1
for i in range(1,n+1):
  for j in range(1,i+1):
    print(c,end=" ")
    c+=1
  print("")


# write the program print right angle triangle using alphabet
n=int(input())
for i in range(1,n+1):
    c=65
    for j in range(1,i+1):
      print(chr(c),end=" ")
      c+=1
    print(" ")
      

#print left angle triangle using star*
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

#inverted lft angle triangle using star
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i)

'''

#write the program to print pyramid pattern using *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))