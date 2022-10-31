import math
from math import pi
from math import atan 
lengths=input("Enter 6 lengths of quadrilateral and light and hit point:").split()
widths=input("Enter 6 widths of quadrilateral and light and hit point:").split()
for i in range (6):
    lengths[i]=int(lengths[i])
    widths[i]=int(widths[i])
a=[]     #slope of 4 sides of a quadrilateral and the line between light point and hit point to the side 
lengthv=[]   #length of sides's vector and first ray vector
widthv=[]    #width of sides's vector and first ray vector
for i in range (5):
    if i!=3 :
       l=lengths[i+1]-lengths[i]
       w=widths[i+1]-widths[i]
    else:
       l=lengths[3]-lengths[0]
       w=widths[3]-widths[0]
    lengthv.append(l)
    widthv.append(w)   
    if l!=0:         #this is added cause i saw on i=4  can not calcuate w/l due to infinitive slope 
        a.append(w/l)
    else:
        a.append("infinitive") 
print("a=",a)
print("lengthv=",lengthv)
print("widthv=",widthv)             
b=[]     #intercept of course about lines which their slope isn't infinitive,if  so formula of line is x=b
for i in range(5):
    if a[i]!="infinitive":
       w=widths[i]-a[i]*lengths[i]
       b.append(w)
    else:
        b.append(lengths[i])
print("b=",b)          
# hit point test (we want to see hit point is on which side of quadrilateral) 
i=0 
k=-1     
while k==-1:
    if a[i]!="infinitive":
        if widths[5]==a[i]*lengths[5]+b[i]:
            k=i
            print("hit point is on line",i+1)
        else:
            i+=1
    else:
        if lengths[5]==b[i]:
            k=i
            print("hit point is on line",i+1)
        else:
            i+=1 
# finding symmetry of first ray vector of light with respect to the side that the light hit 
#k+1 indicates line number
#symmetry of a vector with respect to b vector formula: (2(a.b)/|b|^2*b)-a 
# t=2*(a.b) , m=|b|^2
t=2*(lengthv[4]*lengthv[k]+widthv[4]*widthv[k])
m=lengthv[k]**2+widthv[k]**2
t/=m
l=t*lengthv[k]-lengthv[4]
w=t*widthv[k]-widthv[4]
print("l=",l,"    w=",w)
if l!=0:
    slope=w/l
    print("slope=",slope)
    print("arctan(slope)=",atan(slope)*180/pi ," degrees")
else:
    slope='infinitive'
    print("slope=",slope)
    print("arctan(slope)=90 degrees")
#formula of reflected ray line
a.append(slope)
if a[6]!="infinitive":  
    w=lengths[5]-a[6]*lengths[5]
    b.append(w)
else:
    b.append(lengths[5]) 

         
     

                

       