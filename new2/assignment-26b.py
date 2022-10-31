x="3+4*2-5-6*7+3+9-8/4+8"
l=list(x)
operand=[]
operator=[]
i=1
while i < len(l)-1:
    if l[i]=="*":
        k=int(l[i-1])*int(l[i+1])
        l.pop(i-1)
        l.pop(i-1)
        l.pop(i-1)
        l.insert(i-1,k)
        i-=1
    elif l[i]=="/":
        k=int(l[i-1])/int(l[i+1])
        l.pop(i-1)
        l.pop(i-1)
        l.pop(i-1)
        l.insert(i-1,int(k))
        i-=1
    elif l[i]=="%":
        k=int(l[i-1])%int(l[i+1])
        l.pop(i-1)
        l.pop(i-1)
        l.pop(i-1)
        l.insert(i-1,k)
        i-=1            
    i+=1
print(l)
i=1
while i<len(l)-1:        
    if l[i]=="+":
        k=int(l[i-1])+int(l[i+1])
        l.pop(i-1)
        l.pop(i-1)
        l.pop(i-1)
        l.insert(i-1,k)
        i-=1
    elif l[i]=="-":
        k=int(l[i-1])-int(l[i+1])
        l.pop(i-1)
        l.pop(i-1)
        l.pop(i-1)
        l.insert(i-1,k)
        i-=1
    i+=1    
print(l)        