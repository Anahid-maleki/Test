# combining ferma thessis and all prime numbers except 2,3 are in form 6k+1 or 6k-1 if k={-1,0,1,2,...} and sqrt
# and starting from 3 with 2 step it means we dont check even numbers
import math
x=int(input("Enter a number:"))
prime=[2,3]
f=math.log10(2*3)
p2=[]
j=1
m=1
t=0
while j==1:
   y=6*m-1
   z=6*m+1
   if y<x and z<x:
      p2.append(y)
      p2.append(z)
      t+=2
      m+=1
   elif y<x and z>=x:
      p2.append(y)
      t+=1
      m+=1
   else:
      j=0
m=0         
#print("p2=",p2,"           t=",t) 
for i in range (t):
   q=int(math.sqrt(p2[i]))
   k=len(prime)
   for j in range (k):
      w=0
      if prime[j]<=q and p2[i]%prime[j]==0:
         w=1
         break
   if w==0:
      prime.append(p2[i])
      f+=math.log10(p2[i])
      #print(p2[i])
print(len(prime) ,"f=",int(f+1))
n=0