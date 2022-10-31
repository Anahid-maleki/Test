x=5
table=[['k', 'd', 'e', 'w', 'b'], ['o', 'w', 'a', 'f', 'l'],
 ['o', 'i', 't', 'r', 'o'], ['b', 'u', 'r', 'f', 's'], ['v', 'd', 't', 'j', 'e']]
import math
words=['sofa', 'fruit', 'impossible', 'dart']
letter_dimen=[]
y=[]
q=0
m=0
for i in range(len(words)):
    for j in range(len(words[i])):
        n=m
        for k in range(len(table)):
            for l in range(len(table[k])):
                if words[i][j]==table[k][l]  :
                    y.append(k)
                    y.append(l)
                    m+=2
        if len(y)==0:
           print(words[i],"is not found.")
           q=1
           break
        else:
           letter_dimen.append(y[n:m])
    if q==1:
        q=0
        break
    d=[] 
    print(letter_dimen)
    j=0
    k=0
    l=0
    while j!=len(letter_dimen):
        while k!=len(letter_dimen[j]):
            while l!=len(letter_dimen[j+1]):
                m=abs(letter_dimen[j][k]-letter_dimen[j+1][l])
                n=abs(letter_dimen[j][k+1]-letter_dimen[j+1][l+1])
                if m>=2 or n>=2 and j!=len(letter_dimen):
                    letter_dimen[j+1].pop(l)
                    letter_dimen[j+1].pop(l)
                    print(letter_dimen)
                    l-=2  
                l+=2
            k+=2
        j+=1            
                                                           



                      

                 


       
  
