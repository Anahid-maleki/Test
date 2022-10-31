import math
import datetime
x=int(input("Enter a number:"))
n=datetime.datetime.now()
prime=[True for i in range(x+1)]
a=2
while  a*a < x+1:
    if prime[a]==True:
        if a==2:
           q=a
        else:
            q=2*a 
        for j in range (a*a,x+1,q):
            prime[j]=False
    a+=1    
m=0
for i in range(2,x+1):
    if prime[i] == True:
       m+=math.log10(i)           
print("m=",int(1+m))       
k=datetime.datetime.now() 
s=k-n
print("time: ",int(s.total_seconds()) ) 