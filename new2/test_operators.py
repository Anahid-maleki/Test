str="2+3*5/2-7"
list=[]
for i in range(len(str)):
    list.append(str[i])
print(list)
for i in range(len(list)):
    if list[i]!="+" and list[i]!="-" and list[i]!="*" and list[i]!="/":
       list[i]=int(list[i])
print(list) 
for i in range(len(list)):
    print("list[{}]={}".format(i,list[i]))
    if list[i]=="*":
        list[i-1]*=list[i+1]
        list.pop(i)
        list.pop(i)
        i-=2
        print(list)
    if list[i]=="/":
        list[i-1]/=list[i+1]
        list.pop(i)
        list.pop(i)
        i-=2
        print(list)       
for i in range(len(list)):
    if list[i]=="-":
        b=list[i-1]-list[i+1]
        list.pop(i-1)
        list.pop(i-1)
        list.pop(i-1)
        list.insert(i-1,b)
        print(list)
    if list[i]=="+":
        b=list[i-1]+list[i+1]
        list.pop(i-1)
        list.pop(i-1)
        list.pop(i-1)
        list.insert(i-1,b)
        print(list) 

