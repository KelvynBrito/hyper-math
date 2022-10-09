import numpy as np
import matplotlib
from numpy.core.numeric import asarray, array, asanyarray, concatenate
import math

if __name__=="__main__":
   print("This is a script")

def f(a,n,b): ##DEFINITION OF HYPER-OPERATION
    if n==0:
        return a+1
    elif n==1:
        return a+b
    elif n==2:
        return a*b
    elif n==3:
        return a**b
    elif a==1:
        return 1
    elif (n>=1 and b==0):
        return 1
    else:
        g=f(a,n,b-1)        
        return f(a,n-1,g)

print(f(2,3,3))
## CALCULATOR OF HYPEROPERATIONS:
    
print("Enter three numbers, a, n and b you want operate.")
print("This will result a[n]b.")
print("The first cases are: a[1]b=a+b; a[2]b= a*b, a[3]b=a**b, ...")    
while True:
    a=float(input(":"))
    n=float(input(":"))
    b=float(input(":"))

    print(f(a,n,b))
    if input("")=="c":
        break
