import math
table=[['s', 'd', 'e', 'w', 'b'], ['o', 'w', 'a', 'f', 'l'],
 ['o', 'i', 't', 'r', 'o'], ['b', 'u', 'r', 'f', 's'], ['v', 'd', 't', 'j', 'e']]
word="sofa"
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
while m<len(dimen)-1:   
   for i in range(len(dimen[m])):
       for j in range(len(dimen[m+1])):
           if abs(dimen[m][i][0]-dimen[m+1][j][0])<=1 and abs(dimen[m][i][1]-dimen[m+1][j][1])<=1:
              a.append(dimen[m][i])
              b.append(dimen[m+1][j])
   z=list(zip(a,b))
   print("a=",a)
   print("b=",b)                     
   m+=1
print("z=",z)
i=0   
while i < (len(b)-1):
    k=0
    print(i)
    j=0
    while j < (len(a)):
        print(j)
        if b[i]==a[j]:
          k=1  
          break
        j+=1
    if k==0:
        print(b)
        print(a)
        b.pop(i)
        a.pop(i)
        print(b)
        print(a)
        i-=1
    i+=1
z1=list(zip(a,b))
print(z1)
final=[]
final.append(a[0])
for i in range(len(b)):
    final.append(b[i])
    print(final)                   


                    