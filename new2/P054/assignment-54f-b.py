import math
import datetime
x=int(input("Enter a number:"))
n=datetime.datetime.now()
prime=[True for i in range(x+1)]
for i in range (4,x+1,2):
    prime[i]=False
prime[0]=False
a=3    
while  a*a < x+1:
    if prime[a]==True:
        for j in range (a*a,x+1,2*a):
            prime[j]=False
    a+=2    
m=0
for i in range(2,x+1):
    if prime[i] == True:
       m+=math.log10(i)           
print("m=",int(1+m))       
k=datetime.datetime.now() 
s=k-n
print("time: ",int(s.total_seconds()) ) 