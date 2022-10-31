length=input("Enter six lengths:").split()
width=input("Enter six widths:").split()
# first 4 points are foursquare and fifth point is light source and sixth is where it hits
for i in range (6):
    length[i]=int(length[i])
    width[i]=int(width[i])
    a=[]
for i in range(5):
    print(i)
    if i==3:
       slope=(width[3]-width[0])/(length[3]-length[0])
       a.append(slope) 
    else:     
       slope=(width[i+1]-width[i])/(length[i+1]-length[i])
       a.append(slope)
print(a)
degree=[]
import math
from math import pi
for i in range(5):
    c=180/pi*math.atan(a[i])
    degree.append(c)
print(degree)   
# now,we want to calculate the angle that light hit the surface 
# first we have to see hit point is on which line
b=[]
for i in range(4):
    w=width[i]-a*length[i]
    b.append(w)
print(b)    






