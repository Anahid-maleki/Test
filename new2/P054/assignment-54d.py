import math
import datetime
x=int(input("Enter a number:"))
s=datetime.datetime.now()
prime=[2,3,5]
p2=[]
f=math.log10(2*3*5)
j=1
m=1
t=2
while j==1:
   y=6*m-1
   z=6*m+1
   if y<=x and z<=x :
      p2.append(y)
      p2.append(z)
      t+=2
      m+=1
   elif y<=x and z>x :
      p2.append(y)
      t+=1
      m+=1
   else:
      j=0          
for i in range (1,len(p2)):
    v=int(math.sqrt(p2[i]))
    j=2
    g=0
    while(prime[j]<=v):
        if p2[i]%prime[j]==0:
            g=1
            break
        j+=1 
    if g==0:
        prime.append(p2[i]) 
        f+=math.log10(p2[i])           
print("len=",len(prime),"f=",int(1+f))
a=datetime.datetime.now() 
c=a-s
print("time: ",int(c.total_seconds()) )                    
                            
