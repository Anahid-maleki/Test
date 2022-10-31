import math
x=int(input("Enter the type of your number(primorial Enter 1,factorial enter 2,power enter 3):"))    
y=int(input("Enter a number:"))
prime=[2,3]
if x==1:
    w=0
    m=math.log10(2*3)
    for i in range (5,y,2):
        t=0
        j=0
        k=1+int(math.sqrt(i))
        while prime[j] <k :
            if i%prime[j]==0:
                t=1
                break
            j+=1
        if t==0:
            prime.append(i)
            w+=1
            m+=math.log10(i)                        
print("m=",int(m+1))
print("number of primes=",w+2)   


                