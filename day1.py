                   #operators


#print greatest among three numbers 
'''
a=int(input("enter a value of a:"))
b=int(input("enter a value of b:"))
c=int(input("enter a value of c:"))
if(a>b&a>c):
    print("a is the greatest number",a)
elif(b>a&b>c):
    print("b is the greatest number",b)
else:
    print("c is the greatest number",c)
'''
#type conversion
'''
a=10
b=float(a)
print(a,b)
'''
'''
#input formatting
a=int(input())
b=float(input())
c=str(input())
stud_id,roll_no,name=map(int,input().split())
lst=list(map(int,input().split()))
'''

'''
#delete
a=5
b=10
print(a,b)
del a
print(a,b) #this will give error because a is deleted
'''
'''
#fstring
a=67.48300098
print(f"{a:.7f}") #this will print the value of a upto 7 decimal places
print("{:.2f}".format(a)) #this will print the value of a upto 2 decimal places
print(round(a,7))

'''
'''

#write the program check given  number is odd or even 
a=13
if(a%2==0):
    print("even number")
else:
    print("odd")

#write the program find the average of subject marks note:5 subjects theb print the average output 3 decimal places 
sub1=int(input("enter the marks of subject 1:"))
sub2=int(input("enter the marks of subject 2:"))
sub3=int(input("enter the marks of subject 3:"))
sub4=int(input("enter the marks of subject 4:"))
sub5=int(input("enter the marks of subject 5:"))
total=sub1+sub2+sub3+sub4+sub5
average=total/5
print("the average marks of 5 subjects is: {:.3f}".format(average))

'''

#printformat
a,b,c,d,e=map(int,input().split())
print(a,b,c,d,e,sep="-")
print(a,end="*\n")
stu_id=int(input())
name=input()
print("my name %s,my id %d" % (name,stu_id))