x=["this","is","an","original","text"]
y=["is","is","a","national","text"]

my_list=list(zip(x,y))
print(my_list)
for i in my_list:
    if i[0]==i[1]:
        print(i)
        