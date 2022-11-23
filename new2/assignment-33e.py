x="""This is a sample text 
which spans across several 
lines."""
y="""is a new text
where spans ross new ver
lines."""
a=x.split("\n")
b=y.split("\n")
common=[]
def find_rest(t,j,i):
    c=""
    while b[i][j]==a[i][t]:
        c+=b[i][j]
        j+=1
        t+=1
    common.append(c)
    return len(c)
for i in range(len(b)):
    j=0
    t=0
    while j< len(b[i]):
        c=a[i][t:].find(b[i][j])
        if c!=-1:
            m=find_rest(t,j,i)
