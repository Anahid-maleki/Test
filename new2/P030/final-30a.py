import math
table=[['s', 'd', 'e', 'w', 'b'], ['o', 'w', 'a', 'f', 'l'],
 ['o', 'i', 't', 'r', 'o'], ['b', 'u', 'r', 'f', 's'], ['v', 'd', 't', 'j', 'e']]
word="fruit"
x=[]
y=[]
dimen=[]
m=0
n=0
for i in range(len(word)):
    for j in range(len(table)):
        for k in range(len(table)):
            if table[j][k]==word[i]:
                x.append(j)
                x.append(k)
                y.append(x[m:m+2])
                m+=2
    dimen.append(y[n:len(y)])
    n=len(y)
print(dimen)
if len(dimen)<len(word):
    print(word,"is not found.")
m=0 
a=[]
b=[]
s=0
while m<len(dimen)-1:   
   for i in range(len(dimen[m])):
       for j in range(len(dimen[m+1])):
           if abs(dimen[m][i][0]-dimen[m+1][j][0])<=1 and abs(dimen[m][i][1]-dimen[m+1][j][1])<=1:
              a.append(dimen[m][i])
              b.append(dimen[m+1][j])
              if m==0:
                s+=1
   z=list(zip(a,b))
   print("a=",a)
   print("b=",b)                     
   m+=1
print("z=",z)
print("s=",s)
i=0
while i<s:
    j=s
    while j<2*s:
      if b[i]==a[j]:
        print("equal")
      else:
        a.pop(i)
        b.pop(i)
        i-=1
        j-=1
        s-=1
      j+=1  
    i+=1
print("a=",a)
print("b=",b)            
i=0
while i< len(b)-1:
    if b[i]==a[i+1]:
        print("equal")
    else:
        a.pop(i+1)
        b.pop(i+1)
        i-=1
    i+=1
z1=list(zip(a,b))
print(z1)
final=[]
final.append(a[0])
for i in range(len(b)):
    final.append(b[i])
    print(final)        



                    