import math
lengths=input("Enter 4 lengths of quadrilateral:").split()
widths=input("Enter 4 widths of quadrilateral :").split() 
for i in range (4):
    lengths[i]=int(lengths[i])
    widths[i]=int(widths[i])
lengths.append(lengths[0])
widths.append(widths[0])
print("lengths=",lengths)
print("widths=",widths)          
lenh=[]  #light source point's length and hit points's length
widh=[]  #light source point's width and hit point's width
x,y=input("Enter light source point's length and first hit point's length:").split()
lenh.append(int(x))
lenh.append(int(y))
x,y=input("Enter light source point's width and first hit point's width:").split()
widh.append(int(x))
widh.append(int(y))
a=[]     #slope of 4 sides of a quadrilateral and the line between light point and hit point to the side 
lengthv=[]   #length of sides's vector and first ray vector
widthv=[]    #width of sides's vector and first ray vector
for i in range (4):
    l=lengths[i+1]-lengths[i]
    w=widths[i+1]-widths[i]
    lengthv.append(l)
    widthv.append(w)   
    if l!=0:         #this is added cause i saw on i=4  can not calcuate w/l due to infinity slope 
        a.append(w/l)
    else:
        a.append("infinity")              
b=[]     #intercept of course about lines which their slope isn't infinity,if  so formula of line is x=b
for i in range(4):
    if a[i]!="infinity":
       w=widths[i]-a[i]*lengths[i]
       b.append(w)
    else:
        b.append("parallel to X-axis") 
a.append("not needed")
b.append("not needed")              
print("a=",a)
print("lengthv=",lengthv)
print("widthv=",widthv)        
print("b=",b)
# hit point test (we want to see hit point is on which side of quadrilateral)
i=0 
k=-1     
while k==-1:
    if a[i]!="infinity" :
        if widh[1]==a[i]*lenh[1]+b[i]:
            k=i
            print("hit point is on line",i+1)
        else:
            i+=1
    else:
        if lenh[1]==lengths[i] and (widh[1]-widths[i])*(widh[1]-widths[i+1])<0:
            k=i
            print("hit point is on line",i+1)
        else:
            i+=1                                
for i in range(11):
    print("i=",i)
    l=lenh[i+1]-lenh[i]
    lengthv.append(l)
    w=widh[i+1]-widh[i]
    widthv.append(w)
    #av and bv slope and y-intercept of vertical line to line k+1
    av=["not determined","not determined","not determined","not determined"]
    if a[k]==0 :
       av[k]="infinity"   #slope of vertical line
    elif a[k]=="infinity":
        t=0 
    else:
        t=-1/a[k]
    av[k]=t    
    bv=["not determined","not determined","not determined","not determined"]  #vetical lines to sides of quadrilaterals   
    if av[k]!="infinity":     
       m=widh[i+1]-av[k]*lenh[i+1]  #vertical line to side number k+1 which (lenh[i],widh[i]) is located on
       bv[k]=m
       d=abs(widh[i]-t*lenh[i]-bv[k])/math.sqrt((-t)**2+1)
       print("d=",d)
    else:
        bv[k]="parallel to X-axis"
        d=abs(lenh[i+1]-lenh[i])
        l=lenh[i]+2*d
        w=widh[i]
    # writting formula of the symmetry of ray with two points of it
    if (l-lenh[i+1])!=0:
       slope=(w-widh[i+1])/(l-lenh[i+1])
       a.appened(slope)
       t=w-a[i+5]*l
       b.appened(t)
    q=0
    for j in range (4):
        if j!=k:
            if a[j]=="infinity" and a[i+5]!="infinity":
                y=a[i+5]*lengths[j]+b[i+5]
                if (y-widths[j])*(y-widths[j+1])<0:
                    k=j
                    lenh.append(lengths[j])
                    widh.append(y)
                    q=1
            elif a[j]!="infinity" and a[i+5]=="infinity": 
                y=a[j]*lenh[i+1]+b[j]
                if  (y-widths[j])*(y-widths[j+1])<0:
                    k=j
                    lenh.append(lenh[i+1])
                    widh.append(y)
                    q=1  
            elif  a[j]!="infinity" and a[i+5]!="infinity": 
                x=(b[i+5]-b[j])/(a[j]-a[i+5])
                y=a[j]*x+b[j]
                if (x-lengths[j])*(x-lengths[j+1])<0:
                    k=j
                    lenh.append(x)
                    widh.append(y)
                    q=1 
           # else:  #side=="infinity" & ray=="infinity"                     
            #    print("ray and side are parallel")
        if q==1:
            break
print("lengths=",lengths)
print("widths=",widths)
print("lengthv=",lengthv)
print("widthv=",widthv)
print("a=",a)
print("b=",b)
print("av=",av)
print("bv=",bv)
print("lenh=",lenh)
print("widh=",widh)        


