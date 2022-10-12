import math
import numpy as np

'''THIS PROGRAM COMPUTE IF A NUMBER IS A PRIME NUMBER
AND LIST THE PRIME NUMBERS'''
###########################

def Prime(x):
    t=0
    X=[]
    for i in range(int(math.sqrt(x))+2):
        if i!=0 and i!=1:
            if x!=i and x%i==0:
                #print(i)
                X.append(i)
                if len(list(str(x)))>10 and len(X)!=0:
                    break
      
                            
    return [len(X),X]
S=int(input("What to do?:1- Verify is a number is prime\n or 2-list the prime numbers"))
if S==1:
    while True:
        x=int(input("what number?"))
        if Prime(x)[0]!=0:        
                print(str(x)+" is not a prime number")
                print("and have the following divisors:"+str(Prime(x)[1]))
        else:
                print(str(x)+" is a prime number")
elif S==2:
    m=int(input("up to how many?"))
    M=[]
    for i in range(m):
        if Prime(i)[0]==0:
            M.append(i)
    M.remove(0)
    M.remove(1)            
    print("The list of all numbers up to "+str(m)+"is\n"+str(M))
            
                
    
        
    
