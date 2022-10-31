import math
import datetime
s=datetime.datetime.now()
x=int(input("Enter a number:"))
s=datetime.datetime.now()
p=[]
i=0
j=1 
while j==1:
    y=int(1+math.pow(2,math.pow(2,i)))
    if y<x: 
       p.append(y)
       i+=1
    else:
        j=0        
m=math.log10(2)
prime=[2]        
for j in range (3,x,2):
    t=0
    a=0
    for a in range (i):
        if p[a]==j:
            t=1
            prime.append(j)
            m+=math.log10(j)
            break
    if t==0:
        k=1+int(math.sqrt(j))
        n=0
        w=0
        while prime[n]<k:
            if j%prime[n]==0:
                w=1
                break
            else:
                n+=1
        if w==0:
           prime.append(j)
           m+=math.log10(j)              
print("result=",int(1+m))        
g=datetime.datetime.now() 
c=g-s
print("time: ",int(c.total_seconds()) )


        

            
           