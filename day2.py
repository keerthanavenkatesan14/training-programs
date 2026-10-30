'''
Part 1 — Print & Variables
1. Print Hello World.
                                                                                                                                                          
2. Store your name in a variable and print it.

3. Store your name, age and city in separate variables and print them on one line with spaces.

4. Create two variables a = 10 and b = 20. Print both in the same line separated by a hyphen.

5. Swap two variables and print their values before and after swapping.

Part 2 — Data Types & Type Conversion

1. Create one variable each for int, float, string and bool. Print their values.

2. Take your age as input and print its data type.

3. Take two integers as input and print their sum.

4. Take a number as input and convert it into a float. Print its type.

5. Take a number as a string and convert it into an integer. Add 5 to it.

Part 3 — Arithmetic Operators

1. Take two numbers as input and print their sum, difference, product and quotient.

2. Take two integers and print the result of floor division (//).

3. Find the remainder when one number is divided by another.

4. Take a two-digit number and print its last digit using the modulus operator.

5. Take a two-digit number and print the sum of its digits using // and %.

6. Calculate the square and cube of a number.

7. Calculate the area and perimeter of a rectangle using length and breadth.

Part 4 — Comparison Operators
1. Take two numbers and check whether they are equal.
2. Take two numbers and print the greater number using only a comparison expression.
3. Check whether a number is between 10 and 50, inclusive, using chained comparison.
4. Take three numbers and check whether a > b > c.
5. Predict the output of: print(10 == 10.0), print(10 != 5), print(7 < 3).



Part 5 — Logical Operators
1. Check whether a number is greater than 10 and less than 100.
2. Check whether a number is divisible by both 3 and 5.
3. Check whether a number is divisible by either 3 or 5.
4. Check whether a number is not equal to zero using the not operator.
5. Predict the output of: print(True and False), print(True or False), print(not True).



Part 7 — Assignment Operators
1. Set a = 10 and use += 5. Print a.
2. Set a = 20 and use -= 7. Print a.
3. Set a = 6 and use *= 3. Print a.
4. Set a = 20 and use //= 3. Print a.
5. Set a = 17 and use %= 5. Print a.
6. Set a = 4 and use **= 3. Print a.
7. Set a = 25 and use /= 4. Print a.
8. Predict the output: a = 10; a += 5; a *= 2; a -= 4; print(a).


#1
print("hello world")
#2
a="keerthana"
b=20
print(f"my name is {a} and i am {b} years old")

#3
a="keerthana"
b=20
c="chennai"
print(a,b,c ,sep=" ")

#4,5
a=10
b=20
print(f"{a}-{b}")
print("before swapping", a,b)
print("after swapping", b,a)

#6
a=10
b="20"
c=20.0
d=True
print(type(a),type(b),type(c),type(d))
print(a,b,c,d,sep="\n")
#7
age=int(input("enter your age :"))
print(type(age))
age=str(age)
print(type(age))
#8
a=int(input("enter a value of a:"))
b=int(input("enter a value of b:"))
print("the sum is :",a+b)
#9
a=input("enter a value of a:")
a=int(a)
print("the value is :",a+5)

a=2
b=20
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a//b)
print(a/b)
print("the last digit is :",a%10)
print(a**2)
print(a**3)
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a//=5
print(a)
a%=5
print(a)
a**=5
print(a)
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
print("the area of rectangle is :",length*breadth)
print("the perimeter of rectangle is :",2*(length+breadth))

a=int(input("enter a number:"))
if (a>=10 and a<=99):
    b=a//10
    c=a%10
    print("the sum is:",b+c)
else:
    print("enter a two digit number ")
'''
a=10
b=20
print(a==b)
if a>b:
    print("a is the greatest number",a)
elif b>a:
    print("b is the greatest number",b)


