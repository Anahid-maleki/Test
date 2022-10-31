import math
from math import pi
from math import atan 
lengths=input("Enter 4 lengths of quadrilateral:").split()
widths=input("Enter 4 widths of quadrilateral :").split() 
for i in range (4):
    lengths[i]=int(lengths[i])
    widths[i]=int(widths[i])       
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
    if i!=3 :
       l=lengths[i+1]-lengths[i]
       w=widths[i+1]-widths[i]
    else:
       l=lengths[3]-lengths[0]
       w=widths[3]-widths[0]
    lengthv.append(l)
    widthv.append(w)   
    if l!=0:         #this is added cause i saw on i=4  can not calcuate w/l due to infinity slope 
        a.append(w/l)
    else:
        a.append("infinity") 
print("a=",a)
print("lengthv=",lengthv)
print("widthv=",widthv)             
b=[]     #intercept of course about lines which their slope isn't infinity,if  so formula of line is x=b
for i in range(4):
    if a[i]!="infinity":
       w=widths[i]-a[i]*lengths[i]
       b.append(w)
    else:
        b.append("parallel to X-axis")
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
        if lenh[1]==lengths[0]:
            k=i
            print("hit point is on line",i+1)
        else:
            i+=1 
# finding symmetry of ray vector of light with respect to the side of quadrilateral that the light hit 
#k+1 indicates line number
#symmetry of a vector with respect to b vector formula: [2*(a.b)/(|b|^2)]*b-a 
# t=2*(a.b) , m=|b|^2            
for i in range (10):
    print(lenh)
    print(widh)
    l=lenh[i+1]-lenh[i]
    w=widh[i+1]-widh[i]
    lengthv.append(l)
    widthv.append(w)
    t=2*(lengthv[4+i]*lengthv[k]+widthv[4+i]*widthv[k])
    m=lengthv[k]**2+widthv[k]**2
    t/=m                # t=2*(a.b)/(|b|^2)
    l=t*lengthv[k]-lengthv[4+i]  
    w=t*widthv[k]-widthv[4+i]
    print("l=",l,"    w=",w)
    if l!=0:
       slope=w/l
       print("slope=",slope)
       print("arctan(slope)=",(180/pi)*atan(slope) ," degrees")
    else:
       slope='infinity'
       print("slope=",slope)
       print("arctan(slope) =90 degrees")
    #formula of reflected ray line
    a.append(slope)
    print(a)
    if a[4+i]!="infinity":  
       w=widh[i+1]-a[4+i]*lenh[i+1]
       b.append(w)
    else:
       b.append("parallel to Y-axis")
    #finding point of intersection
    #in order to find intersection point we should formula of 3 other sides of quadrilateral except that-
    #one which ray is reflected from, we have been on line k+1 until now so from i=1 till i=4 except i=k+1-
    # we should check lines
    for j in range (4):
        q=0
        if j!=k:
            if a[j]=="infinity" and a[i+4]!="infinity":
                if a[i+4]*lengths[j]+b[i+4]>widths[j] and a[i+4]*lengths[j]+b[i+4]<widths[j]:
                    k=j
            elif a[j]!="infinity" and a[i+4]=="infinity": 
                if a[j]*lenh[i+1]+b[j] > widths[j] and a[j]*lenh[i+1]+b[j] < widths[j]:
                    k=j  
            elif  a[j]!="infinity" and a[i+4]!="infinity": 
                  for m in range (4):
                    if a[i+4]*lengths[m]+b[i+4]:
                        print("ray hits one of quadrilateral's vertex between line",m,m+1)
                        q=1
                    else:
                        x=(b[i+4]-b[j])/(a[j]-a[i+4])
                        if x>lengths[j] and x<lengths[j+1]:
                            k=j
            else:  #side=="infinity" & ray=="infinity"                     
                if lengths[j]==lenh[i]:
                    print("ray hits one of quadrilateral's vertex between line",j,j+1,"and matchs side: x=",lengths[j])
                    q=1
                else: # side and ray are parallel
                    k=j+1    
            if q==1:
               break

          