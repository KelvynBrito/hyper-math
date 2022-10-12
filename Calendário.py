
for i in range(1000):
    d=int(input(""))
    m=int(input(""))
    a=int(input(""))

    D=d%7-1
    
    if (a%4)!=0:
        mes=[0,3,3,-1,1,-3,-1,2,-2,0,3,-2]
    elif (a%4)==0:
        mes=[0,3,-3,0,2,-2,0,3,-1,1,-3,-1]
    M=mes[m-1]

    b=a-1
    if (b%4)!=0:
        A=(b//4)*(-2)+b%4
    elif (b%4)==0:
        A=(b//4)*(-2)
            
    Sem=(D+M+A)%7

    if Sem==0:
        print("Domingo")
    if Sem==1:
        print("Segunda")
    if Sem==2:
        print("Terça")
    if Sem==3:
        print("Quarta")
    if Sem==4:
        print("Quinta")
    if Sem==5:
        print("Sexta")
    if Sem==6:
        print("Sábado")
    
        



