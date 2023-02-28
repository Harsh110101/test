'''WAP to i/p a number from user and find it is Armstrong number or not.
Armstrong number is a number that is equal to the sum of cubes of its digits.
For example,
0, 1, 153, 370, 371 and 407 are the Armstrong numbers.'''

a=int(input("Enter the value of a\n"))
d=0
c=0
s=str(a)

mylist=[]
mylist.extend(s)

for val in mylist:
    i=int(val)
    d=i**3
    c=c+d
    

print("Sum=", c)

if(a==c):
    print("Armstrong number")
else:
    print("Not a Armstrong number")
    
    
