import math
x=int(input("Enter the type of your number(primorial Enter 1,factorial enter 2,power enter 3):"))
if x==3:
    y,z=input("Enter base and power in order:").split()
    y=int(y)
    z=int(z)
elif x==1 or x==2:    
    y=int(input("Enter a number:"))
prime=[2]
t=1
if x==1:
    m=math.log10(2*3*5*7)
    for i in range(11,y,2) :          #finding prime numbers less than y
        k=0
        q=int(math.sqrt(i))
        for j in range(3,q+1):
            if(i%j==0):
                k=1
                break
        if k!=1:
           m+=math.log10(i)
elif x==2 :
    m=0
    for i in range (1,y+1):
       m+=math.log10(i)
elif x==3 :
    m=z*math.log10(y)      
print("m=",int(m+1))   


                