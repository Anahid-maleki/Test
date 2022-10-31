import math
import datetime
x=int(input("Enter type of number(primorial=1/factorial=2/power=3):"))
if x==1: 
    y=int(input("Enter primorial number:"))
    s=datetime.datetime.now()
    prime=[True for i in range(y+1)]
    i=2
    while i*i<=y:
        if prime[i]==True:
            for j in range(i*i,y+1,i):
                prime[j]=False
        i+=1
    m=0   
    for i in range(2,y+1):
        if prime[i]==True:
            m+=math.log10(i) 
    print("number of figuers of ",y,"#= ",int(m+1))                        
elif x==2:
    y=int(input("Enter factorial number:"))
    s=datetime.datetime.now() 
    m=0
    for i in range(1,y+1):
        m+=math.log10(i)
    print("number of figuers of ",y,"!=",int(m+1))         
elif x==3:
    y,z=input("Enter base and power:").split()
    s=datetime.datetime.now()
    y=int(y)
    z=int(z)
    m=z*math.log10(y)
    print("number of figuers of ",y,"^",z,"=",int(m+1)) 
a=datetime.datetime.now() 
c=a-s
print("time: ",int(c.total_seconds()) ) 
