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
k=0
m=0
n=0 
i=0
result=[]
while m < (len(dimen))-1:
   print("result=",result ,"m=",m,"n=",n)
   while i <len(dimen[m+1]):
      if abs(dimen[m][n][0]-dimen[m+1][i][0])<=1 and abs(dimen[m][n][1]-dimen[m+1][i][1])<=1 :
        print(dimen[m][n][0]-dimen[m+1][i][0])
        print(abs(dimen[m][n][1]-dimen[m+1][i][1]))
        result.append(n)
        result.append(i)
        m+=1
        n=i
        k=1
        break
      i+=1  
   if k==0  :
      m-=1
      n=result[-2]
      i=result[-1]+1
   k=0               
               
