x=input("Enter an expression:")
def cal(m,n,operator):
    if operator=="+":
        m+=n
    elif operator=="-":
        m-=n
    elif operator=="*":
        m*=n
    elif operator=="/":
        m/=n
    return m
open=[]
close=[]    
for i in range(len(x)):
    if x[i]=="(":
        open.append(i)
    elif x[i]==")":
        close.append(i)
i=open[-1]+1        
if x[i]=="-":
    m=-1*int(x[i+1])
    operator=x[i+2]
    n=int(x[i+3])
elif x[i]=="+":
    m=int(x[i+1])
    operator=x[i+2]
    n=int(x[i+3])
else:
    m=int(x[i])
    operator=x[i+1]
    n=int(x[i+2])
print(cal(m,n,operator))                                           

 
           