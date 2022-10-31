x=int(input("Enter number the dimention of the table:"))
table=[]
words=[]
for i in range (x):
    y=input("Enter letters:")
    table.append((y.lower()).split())
while(1):
    y=input("Enter words to be searched:")
    if y=="END":
        break
    words.append(y)
print(table)
print(words) 