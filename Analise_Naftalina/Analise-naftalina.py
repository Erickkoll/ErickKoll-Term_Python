# -*- coding: utf-8 -*-
import math
print("Aluno: Erick Cordeiro Kollross  GRR:20124195")
print("Programa criado para diciplica de transferência de Calor e massa via Python")
print("A análise da variação de massa da sublimação da naftalina pelo tempo")
print("Digite '1' para a opção sem abertura do armário. Digite '2' para a opção com abertura do armário")
Z = int(input("Digite a opção do programa: "))
n = float(input("Digite o número de naftalinas: "))
print("Digite '1' para para a variação da massa pelo tempo. Digite '2' para para a variação da raio pelo tempo")
X = int(input("Digite a opção do programa: "))
ri=0.01
if(Z == 1):
    if(X == 1):
        mi = 6.545*10**-4
        x,y = mi,0
        t=0
        m=6.545*10**-4
        while (x > m/100):
            print(round(100-round(100*((mi-x)/mi),1),1),",",round(y/3600,2))
            x-=0.001*m
            t=9.94716*10**7*(n*mi-n*x)-1.27321*10**5*((math.log(n*x))-math.log(n*mi))
            x , y = x, t
    if(X == 2):
        x,y = ri,0
        t=0
        r=0.01
        while (x > ri/100):
            print(round(100-round(100*((ri-x)/ri),3),3),",",round(y/3600,2))
            x-=0.0001*ri
            t=3.906*10**7*(n*ri-n*x)+4.775*(n/(n*x**2)-n/(n*r**2))
            x , y = x, t
if(Z == 2):       
    if(X == 1):
        mi=6.545*10**-4
        m=6.545*10**-4
        t=0
        x,y, z = m,t,m
        z=x
        d=24*3600
        while (t < d**2):
            e=t**0.5
            print(round(100-round(100*((m-x)/m),2),2),",",round(y**0.5/3600,3))
            x-=0.01*m
            t=(9.94716*10**7*(n*m-n*x)-(1.27321*10**5*((math.log(n*x))-math.log(n*mi))))**2
            x, y = x, t
        else:
            mi=x
            t=y
            y1=y
            x1=x
            while(t < (2*d)**2):
                e=t**0.5
                print(round(100-round(100*((m-x1)/m),2),2),",",round(e/3600,3))
                x1-=0.01*m
                t=(16*3600)**2+(9.94716*10**7*(n*m-n*x1)-(1.27321*10**5*((math.log(n*x1))-math.log(n*mi))))**2
                x1, y = x1, t
            else:
                mi=x1
                t=y
                y2=y1
                x2=x1
                while(t < (3*d)**2):
                    e=t**0.5
                    print(round(100-round(100*((m-x2)/m),1),1),",",round(e/3600,2))
                    x2-=0.01*m
                    t=(d)**2+(9.94716*10**7*(n*m-n*x2)-(1.27321*10**5*((math.log(n*x2))-math.log(n*mi))))**2
                    x2, y = x2, t
                else:
                    mi=x2
                    t=y
                    y3=y2
                    x3=x2
                    while(t < (4*d)**2):
                        e=t**0.5
                        print(round(100-round(100*((m-x3)/m),1),1),",",round(e/3600,2))
                        x3-=0.01*m
                        t=(1.5*d)**2+(9.94716*10**7*(n*m-n*x3)-(1.27321*10**5*((math.log(n*x3))-math.log(n*mi))))**2
                        x3, y = x3, t
                    else:
                        mi=x3
                        t=y
                        y4=y3
                        x4=x3
                        while(t < (5*d)**2):
                            e=t**0.5
                            print(round(100-round(100*((m-x4)/m),1),1),",",round(e/3600,2))
                            x4-=0.01*m
                            t=(2*d)**2+(9.94716*10**7*(n*m-n*x4)-(1.27321*10**5*((math.log(n*x4))-math.log(n*mi))))**2
                            x4, y = x4, t
                        else:
                            mi=x4
                            t=y
                            y5=y4
                            x5=x4
                            while(t < (6*d)**2):
                                e=t**0.5
                                print(round(100-round(100*((m-x5)/m),1),1),",",round(e/3600,2))
                                x5-=0.01*m
                                t=(2.5*d)**2+(9.94716*10**7*(n*m-n*x5)-(1.27321*10**5*((math.log(n*x5))-math.log(n*mi))))**2
                                x5, y = x5, t
                            else:
                                mi=x5
                                t=y
                                y6=y5
                                x6=x5
                                while(t < (7*d)**2):
                                    e=t**0.5
                                    print(round(100-round(100*((m-x6)/m),1),1),",",round(e/3600,2))
                                    x6-=0.01*m
                                    t=(3.0*d)**2+(9.94716*10**7*(n*m-n*x6)-(1.27321*10**5*((math.log(n*x6))-math.log(n*mi))))**2
                                    x6, y = x6, t
                                else:
                                    mi=x6
                                    t=y
                                    y7=y6
                                    x7=x6
                                    while(t < (8*d)**2):
                                        e=t**0.5
                                        print(round(100-round(100*((m-x7)/m),1),1),",",round(e/3600,2))
                                        x7-=0.01*m
                                        t=(3.9*d)**2+(9.94716*10**7*(n*m-n*x7)-(1.27321*10**5*((math.log(n*x7))-math.log(n*mi))))**2
                                        x7, y = x7, t
                                    else:
                                        mi=x7
                                        t=y
                                        y8=y7
                                        x8=x7
                                        while(t < (9*d)**2):
                                            e=t**0.5
                                            print(round(100-round(100*((m-x8)/m),1),1),",",round(e/3600,2))
                                            x8-=0.01*m
                                            t=(4.8*d)**2+(9.94716*10**7*(n*m-n*x8)-(1.27321*10**5*((math.log(n*x8))-math.log(n*mi))))**2
                                            x8, y = x8, t
                                        else:
                                            mi=x8
                                            t=y
                                            y9=y8
                                            x9=x8
                                            while(t < (10*d)**2):
                                                e=t**0.5
                                                print(round(100-round(100*((m-x9)/m),1),1),",",round(e/3600,2))
                                                x9-=0.01*m
                                                t=(5.7*d)**2+(9.94716*10**7*(n*m-n*x9)-(1.27321*10**5*((math.log(n*x9))-math.log(n*mi))))**2
                                                x9, y = x9, t
                                            else:
                                                mi=x9
                                                t=y
                                                y10=y9
                                                x10=x9
                                                while(t < (11*d)**2):
                                                    e=t**0.5
                                                    print(round(100-round(100*((m-x10)/m),1),1),",",round(e/3600,2))
                                                    x10-=0.01*m
                                                    t=(6.6*d)**2+(9.94716*10**7*(n*m-n*x10)-(1.27321*10**5*((math.log(n*x10))-math.log(n*mi))))**2
                                                    x10, y = x10, t
                                                
    if(X == 2):
        ri=0.01
        r=0.01
        t=0
        x,y, z = ri-10**-10,t, ri-10**-10
        d=24*3600
        while (x > r/99):
            if(0 <t< d):    
                ri=r
                z=x
            k=1
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=2
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=3
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=4
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=5
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=6
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=7
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=8
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=9
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=10
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=11
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=12
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=13
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=14
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=15
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=16
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=17
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=18
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=19
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=20
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=21
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=22
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=23
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=24
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=25
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=26
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=27
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=28
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=29
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=30
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=31
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=32
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=33
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=34
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=35
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=36
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=37
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=38
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=39
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=40
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=41
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=42
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=43
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=44
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=45
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=46
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=47
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=48
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=49
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=50
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=51
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=52
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=53
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=54
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=55
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=56
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=57
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=58
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            k=59
            if(k*d <t< (k+1)*d):    
                ri=x
                z=x
            print(round(100-round(100*((r-x)/r),2),2),",",round(y/3600,2))
            z-=0.0001*r
            x-=0.0001*r
            t=3.906*10**7*(n*r-n*x)+4.775*(n/(n*x**2)-n/(n*ri**2))
            x , y = x, t