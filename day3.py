#to get character AS INPUT
'''
a=input().strip()
print(a)

#discount calculator:write a program that calculates the final price of a purchase after applying discounts based on a total purchase amount.
#requirements:the program should prompt the user to enter the total purchase amount(a positive decimal num)
#apply the following discount rule 1)if the purchase amount is more that $1000,apply a 20% discount 
#2)if the purchase amount is between $500 and $1000(inclusive apply a 10% discount)
#3)if the purchase amount is less than $500,no discount should be applied 
#the program sgould then display the final price after applying the discount.
#ip:1200 op:960.00 , ip:750 op:675.00 , ip:300 op:300.00

a=float(input())
if a>1000:
    dis=a*(0.20)
    print(a-dis)
elif a>=500 and a<=1000:
    dis=a*(0.10)
    print(a-dis)
else:
    print(a)

#student mark percentage get the marks obtained and total marks from the user calculate the percentage and print it with exactly two decimal places 
#sample input enter marks obtained: 425
#enter total marks: 500
#output:percentage=85.00%

a=int(input("enter marks obtained:"))
b=int(input("enter total marks:"))
c=(a/b)*100
print(f"percentage={c:.2f}%")

#delivery distance calculator a delivery app records a distance as a decimal number get the distance and display the whole number distance by removing the decimal part without rounding 
#sample input:34.89 output :34

d=float(input("enter distance:"))
print(int(d))

#packaging calculator a warehouse needs to pack items into boxes that hold a fixed number of items get the total number of items and capacity of one box find minimum numner of boxes required
#sample input:25 6 output:5

import math
from django.conf.locale import sl
total_items=int(input("enter total items:"))
box_capacity=int(input("enter box capacity:"))
print(math.ceil(total_items/box_capacity))

#floor tile calculator. a square floor has an area entered  by the user. calculate the side length and print it to two decimal places sample ip:144 op:12.00

import math
area=int(input())
print(math.sqrt(area))

#access permission checker . a system stores permission as bits.get an integer permission value and a bit mask from the user. check whether any matching permission 
# bits are enabled and print the resulting value ip:7 \n 4  op: 4(hint:we are seeing bitwise operator for 7:0111,4:0100 common is 4 so op 4)

a=int(input())
b=int(input())
print(a&b)
'''
#shared item distribution two teams need to share the certain number of items equally get the total number of items and teams print  how many items receives and how 
# many remain sample ip: 23 /n 4  op:5   3 

#coordinate distance calculator get two points (x1,y1)and (x2,y2), as decimal inputs calculate the distance between them and print the answer to teo decimal places ip:1 2 4 6 op:
import math
x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
print("%.2f"%(math.sqrt((x2-x1)**2+(y2-y1)**2)))
