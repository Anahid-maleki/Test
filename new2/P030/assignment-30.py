x=5
table=[['k', 'd', 'e', 'w', 'b'], ['o', 'w', 'a', 'f', 'l'],
 ['o', 'i', 't', 'r', 'o'], ['b', 'v', 'r', 'f', 's'], ['v', 'd', 't', 'j', 'e']]
words=['sofa', 'fruit', 'impossible', 'dart']
q=0
for i in range(len(words)):
    result=[]
    for k in range(len(table)):
        for l in range(len(table[k])):
            print("i={},j=0,k={},l={}".format(i,k,l))
            if words[i][0]==table[k][l]:
                result.append(k+1)
                result.append(l+1)
                print(result)
                q=1
                break
        if q==1:
           break
    if q==1:
        q=0
    else:
        print("{} is not found. j=0".format(words(i)))    
        continue    
    for j in range(1,len(words[i])):
        q=0
        print(j)
        print(result[-2]-1)
        print(result[-1]-1)
        for m in range(result[-2]-2,result[-2]+1):
            print("m=",m)
            if m==len(table[k]) :
               break
            elif m<0:
                m=0
            for n in range(result[-1]-2,result[-1]+1):
                if n==len(table[k]) :
                    break
                elif n<0:
                    n=0
                print("i={},j={},m={},n={}".format(i,j,m,n))
                if words[i][j]==table[m][n]:
                    result.append(m+1)
                    result.append(n+1)
                    q=1
                    break    
            if q==1 and j!=len(words[i])-1:
                break
            elif q==1 and j==len(words[i])-1:
               pairs=[(result[w],result[w+1]) for w in range(0,len(result)-1,2)]
               print(words[i],"is found in",pairs)
               break
        if q==0:
            print("{} is not found. j={}".format(words(i),j))    
            break
                      

                 


       
  
