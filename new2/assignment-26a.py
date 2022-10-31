x="5-6*7"
mylist=list(x)
print(mylist)         
p=[]
for i in range(len(mylist)):
    print(mylist[i])
    if mylist[i]== "*" or mylist[i]=="/":
       p.append(i)       
if mylist[p[0]]=="*":
    m=int(mylist[p[0]-1])*int(mylist[p[0]+1])
elif x[p[0]]=="/":
    m=int(mylist[p[0]-1])//int(mylist[p[0]+1])        
print(m)    
mylist=mylist[:p[0]-1]
mylist.append(m)
print(mylist)
f=[]
o=[]
for i in mylist:
    if i=="+" or i=="-":
      o.append(i)
    else:
        f.append(int(i))
print(o)
print(f) 
for i in range(-1,-(len(o)+1),-1):
    if o[i]=="-":
        k=f[i-1]-f[i]            
        f.pop()
        f.pop()
        f.append(k)
        o.pop()
    elif o[i]=="+":
        k=f[i-1]+f[i]            
        f.pop()
        f.pop()
        f.append(k)
        o.pop()
print(f)            
