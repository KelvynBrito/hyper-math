
'''
THIS PROGRAM WRITE A NUMBER IN AN ARBITRARY NUMERICAL SYSTEM
'''
def num_sys(x,a):
    ##Euclides Algorithm for a-th numerical systems: x=p*q+r
        B=[]
        q=x
        p=x
        i=0
        while p>0:
            p=x//a              ##
            r=x%a               ##      REPLICATE THIS PIECE 
            B.insert(0,int(r))  ##      IN AN ANALOGOUS WAY
            x=p                 ##      IN THE FUNCTION ABOVE

        B.append("|")
        
        while q-int(q)!=0:
            s=(q-int(q))*a
            B.append(int(s))
            q=s
            i+=1
            if i>50:
                break  
        return B

x=input("What number do you want to represent?")
a=input("In what numerical basis?")
print(num_sys(x,a))
##while True:
##        x=int(input("Enter the number do you want to represent?"))
##        a=int(input("In what base a do you represent it?:"))
##        for i in range(x):
##                y=numerical_system(i+1,a)
##                print(str(x)+"="+str(y))
## 
##
