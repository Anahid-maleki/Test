import math
table=[['s', 'd', 'e', 'w', 'b'], ['o', 'w', 'a', 'f', 'l'],
 ['o', 'i', 't', 'r', 'o'], ['b', 'u', 'r', 'f', 's'], ['v', 'd', 't', 'j', 'e']]
word="dart"
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
   m+=1
print("a=",a)
print("b=",b)
p=[]
q=[]
k=0
for i in range(len(b)-1):
    for j in range(i+1,len(a)):
        if b[i]==a[j]:
            p.append(a[i])
            q.append(b[i])
            k=1
            break
    if k==1:
        break
for j in range(i,len(a)):
    if a[j]==q[-1]:
        p.append(a[j])
        q.append(b[j]) 
print("p=",p)
print("q=",q) 
final=[]
final.append(p[0])
for i in range(len(q)):
    final.append(q[i])
print(final)                     
