import re

class AR:
    def ar(n):
        x=n//1000
        a=x*"M"
        n=n-x*1000
        if n%1000>500:
            a=a+"D"
            n=n-500
        x=n//100
        a=a+x*"C"
        n=n-x*100
        if n%100>50:
            a=a+"L"
            n=n-50
        x=n//10
        a=a+x*"X"
        n=n-x*10
        if n%10>5:
            a=a+"V"
            n=n-5
        x=n
        a=a+x*"I"
        return a
    def ra(a):
        x=0
        a=list(a)
        for i in a:
            if "M" in a:
                x+=1000
                a.remove("M")
            if "C" in a:
                x+=100
                a.remove("C")
            if "D" in a:
                x+=500
                a.remove("D")
            if "L" in a:
                x+=50
                a.remove("L")
            if "X" in a:
                x+=10
                a.remove("X")
            if "V" in a:
                x+=5
                a.remove("V")
            if "I" in a:
                x+=1
                a.remove("I")
        return x

n=input("Qual número deve ser transformado?")
d=AR()
op=input("")
if op==1:
    p=d.ar(n)
    print(p)
elif op==2:
    p=d.ra(a)
    print(p)    
