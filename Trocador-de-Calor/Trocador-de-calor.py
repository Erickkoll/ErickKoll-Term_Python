# -*- coding: utf-8 -*-
print("Aluno: Erick Cordeiro Kollross  GRR:20124195")
print("Programa criado para diciplica de transferência de Calor e massa via Python")
print("Dimensionamento de um trocador de calor")
print("para todas as condições dos exercícios será considerado regime turbulento tanto no escoamento interno quanto no interno. E o comprimento próximo ao diâmetro do tubo")
import math
print("item a")
cpf=4.179
print("calor específico da água",cpf)
cpq=(7*2.427+3*2.471)/10
print("calor específico da óleo",cpq)
mq=0.22
Tqin=250+273.15
Tqout=50+273.15
Tfin=40+273.15
Tfout=44.9+273.15
print("Consideraremos que Cmin será igual á Cq")
Cq=cpq*mq
Cmin=Cq
print("Cmin=Cq=",Cq,"W/K")
qmax=Cmin*(Tqin-Tfin)
print("qmax=",qmax,"W")
q=mq*cpq*(Tqin-Tqout)
print("A troca de calor do sistema é:",q,"W")
mf=q/(cpf*(Tfout-Tfin))
print("a vazão massica do fluído frio é:",mf)
print()
print("Consideraremos que Cmin será igual á Cq")
Cf=mf*cpf*(Tfout-Tfin)
Cmax=Cf
print("Cmax=Cf=",Cf,"W/K")
Cr=Cmin/Cmax
print("Cr=",Cr)
epsilion=q/qmax
print("Com isso aproximamos Cr para 0, e temos que NUT=ln*(1-epsilion)")
print("efetividade do sitema=",epsilion)
nut=-math.log(1-epsilion)
print("NUT=", nut)
pi=3.1416
print("Dado que Red=4*mdot/pi*d*mi, e sabendo que para escoamento turbulento Red>2300")
print("Para fins de calculo consideraremos Red=3000, para que possamos estabelecer certas relações com equações que exigem que renolds seja superior a 3000")
Redi=3000
miq=(7*0.564*10**-2+3*0.470*10**-2)/10
print("viscosidade do óleo=", miq, "N*s/m**2")
dci=4*mq/(Redi*pi*miq)
print(dci)
print("O valor máximo em milímetros dos tubos para serem turbulentos são:",dci*1000,"mm")
di=(int((dci*1000)))/1000
print("Para questões de projeto os tubos escolhidos terão como dimensão interna",di*1000,"mm")   
print()
print("Apartir disso podemos calcular a entalpia do interna, mas antes será calculado o novo Red interno")
Redi=4*mq/(di*pi*miq)
print("Red interno=", Redi)
print("Será calculado o coeficiente de atrito 'fi'")
fi=(0.790*math.log(Redi)-1.64)**-2
print("f interno=", fi)
print("Pr será determinado pela tabela")
Pri=(7*103+3*88)/10
print("Pr interno=", Pri)
print("Com isso podemos determinar o Nud")
Nudi=((fi/8)*(Redi-1000)*Pri)/(1+12.7*(fi/8)**2*(Pri**(2/3)-1))
print("Nud interno=", Nudi)
print("k será determinado pela tabela")
ki=(7*133*10**-3+3*132*10**-3)/10
print("k interno=", ki)
print()
print("Para determinarmos a entalpia interna necessitamos do 'dh', que é dado  tanto em função do diâmetro interno(di) como do externo(de). Para isso calcularemos primeiramento o 'de'")
Rede=3000
mif=631*10**-6
print("viscosidade da agua=", mif, "N*s/m**2")
dce=4*mf/(Rede*pi*mif)
print(dce)
print("O valor máximo em milímetros dos tubos para serem turbulentos são:",dce*1000,"mm")
print("Ou seja, o tubo pode ter o tamanho que se desejar, para tal usaremos que o diâmetro externo é o dobro do interno")
de=2*di
print("A dimensão externa do tudo será=",int(de*1000),"mm")
Rede=4*mf/(de*pi*mif)
print("Red externo=", Rede)
print("Será calculado o coeficiente de atrito 'fe'")
fe=(0.790*math.log(Rede)-1.64)**-2
print("f externo=", fe)
print("'Pr' externo será determinado pela tabela")
Pre=4.16
print("Pr externo=", Pre)
print("Com isso podemos determinar o Nud")
Nude=0.3+((0.62*Rede**(1/2)*Pre**1/3)/(1+(0.4/Pre)**(2/3)**(1/4)))*(1+(Rede/282000)**(5/8))**(4/5)
print("Nud externo=", Nude)
print("k externo será determinado pela tabela")
ke=634*10**-3
print("k externo=", ke)
dh=de-di
print("dh=", int(dh*1000), "mm")
hi=Nudi*ki/dh
he=Nude*ke/dh
print("entalpia interna=", hi)
print("entalpia externa=", he)
print("Temos que 1/U=1/hi+1/he")
U=(hi*he)/(hi+he)
print("U=",U, "W/(m**2*K)")
A=Cmin*nut/U
print("Assim temos que a área transversal do trocador de calor será=",A, "m**2")
L=A/(2*pi*de)
print("O comprimento do tubo será(L)=", L*1000,"mm")
print("Como podemos observar, o comprimento L é bem menor em relação ao diâmetro externo. Para isso refazeremos os calculos dividindo em tubos o projeto")
n=2
dit=di/n
mqt=mq/n
print("O número de tubos será", n)
print("O diâmetro interno será", dit)
print("A vazão quente do tubo será", mqt)
Redi=4*mqt/(dit*pi*miq)
print("O novo renolds calculado será Redi=",Redi)
print("COmo podemos observar o Renolds se manteve constante. Isso porque a vazão e o diâmetro são inversamente proporcionais")
print("Com isso podemos concluir que as propriedades da água se manteram constantes, mudando somente a entalpia")
det=2*dit
print("O diâmetro externo será", det)
dht=det-dit
hit=Nudi*ki/dht
het=Nude*ke/dht
print("A nova entalpia interna=", hit)
print("A nova entalpia externa=", het)
Ut=(hit*het)/(hit+het)
print("O novo coeficiente global de transferência de calor será U=",U, "W/(m**2*K)")
r=Ut/U
print("Fazendo a razão entre os coeficiente globais temos que r=", r)
print("Ou seja 'U' varia é inversamente proporcional ao diâmetro. No entando ambos os tubos estão em paralelo.")
U=Ut*Ut/(Ut+Ut)
print("Ou seja o coeficiente global se manterá constante=",U)
print("Ou seja, nada muda exceto o diâmetro do tubo e a quantidade dele.")
print("Para mantermos o escolament idela faremos com que o tamanho dos tubos sejam iguais á seu comprimento")
n= round(de/L)
print("O número de tubos utilizados será", n)
det=de/n
det=(round(det*10000))/10000
dit=det/2
print("O diâmetro externo de cada tubo será", det*1000, "mm")
print("O diâmetro interno de cada tubo será", dit*1000, "mm")
print("Como demonstramos todas as propriedades se mantiveram constantes. Ou seja todos os coeficiente já foram calculados")
print("Iremos considerar um fator de empacotamento dos tubos de 0.5")
D=(2*n*det**2)**(1/2)
D=int((D*1000)+1)/1000
pack=(det**2*n)/D**2
L=(A/n)/(2*pi*det)
print("O diâmtro interno total do trocador será",D*1000,"mm e recalculado um fator de empacotamento de", round(pack,3))
print("O trocador de calor terá uma chapa de aço de 1mm de espessura totalizando", (D*1000)+2,"mm")
print("O comprimento do trocador recalculado será",L*1000,"mm")
print("Para suportar as tensões o material usado será grafeno industrial")
print()
print()
print("item b")
print()
print("No programa serão somente mudadas as variaveis das propriedades do fluido quente, em todo resto será tudo igual")
print("No caso iremos considerar vapor de água saturada nas mesmas condições de temperatura e pressão")
cpf=4.179
print("calor específico da água",cpf)
cpq=(7*2.291+3*2.369)/10
print("calor específico do vapor de água",cpq)
mq=0.22
Tqin=250+273.15
Tqout=50+273.15
Tfin=40+273.15
Tfout=44.9+273.15
print("Consideraremos que Cmin será igual á Cq")
Cq=cpq*mq
Cmin=Cq
print("Cmin=Cq=",Cq,"W/K")
qmax=Cmin*(Tqin-Tfin)
print("qmax=",qmax,"W")
q=mq*cpq*(Tqin-Tqout)
print("A troca de calor do sistema é:",q,"W")
mf=q/(cpf*(Tfout-Tfin))
print("a vazão massica do fluído frio é:",mf)
print()
print("Consideraremos que Cmin será igual á Cq")
Cf=mf*cpf*(Tfout-Tfin)
Cmax=Cf
print("Cmax=Cf=",Cf,"W/K")
Cr=Cmin/Cmax
print("Cr=",Cr)
epsilion=q/qmax
print("Com isso aproximamos Cr para 0, e temos que NUT=ln*(1-epsilion)")
print("efetividade do sitema=",epsilion)
nut=-math.log(1-epsilion)
print("NUT=", nut)
print("Dado que Red=4*mdot/pi*d*mi, e sabendo que para escoamento turbulento Red>2300")
print("Para fins de calculo consideraremos Red=3000, para que possamos estabelecer certas relações com equações que exigem que renolds seja superior a 3000")
Redi=3000
miq=(7*13.79*10**-6+3*14.14*10**-6)/10
print("viscosidade do óleo=", miq, "N*s/m**2")
dci=4*mq/(Redi*pi*miq)
print(dci)
print("O valor máximo em milímetros dos tubos para serem turbulentos são:",dci*1000,"mm")
di=(int((dci*1000)))/1000
print("Para questões de projeto os tubos escolhidos terão como dimensão interna",di*1000,"mm")   
print()
print("Apartir disso podemos calcular a entalpia do interna, mas antes será calculado o novo Red interno")
Redi=4*mq/(di*pi*miq)
print("Red interno=", Redi)
print("Será calculado o coeficiente de atrito 'fi'")
fi=(0.790*math.log(Redi)-1.64)**-2
print("f interno=", fi)
print("Pr será determinado pela tabela")
Pri=(7*1.075+3*1.1)/10
print("Pr interno=", Pri)
print("Com isso podemos determinar o Nud")
Nudi=((fi/8)*(Redi-1000)*Pri)/(1+12.7*(fi/8)**2*(Pri**(2/3)-1))
print("Nud interno=", Nudi)
print("k será determinado pela tabela")
ki=(7*29.8*10**-3+3*3-.4*10**-3)/10
print("k interno=", ki)
print()
print("Para determinarmos a entalpia interna necessitamos do 'dh', que é dado  tanto em função do diâmetro interno(di) como do externo(de). Para isso calcularemos primeiramento o 'de'")
Rede=3000
mif=631*10**-6
print("viscosidade da agua=", mif, "N*s/m**2")
dce=4*mf/(Rede*pi*mif)
print(dce)
print("O valor máximo em milímetros dos tubos para serem turbulentos são:",dce*1000,"mm")
print("Ou seja, o tubo pode ter o tamanho que se desejar, para tal usaremos que o diâmetro externo é o dobro do interno")
de=2*di
print("A dimensão externa do tudo será=",int(de*1000),"mm")
Rede=4*mf/(de*pi*mif)
print("Red externo=", Rede)
print("Será calculado o coeficiente de atrito 'fe'")
fe=(0.790*math.log(Rede)-1.64)**-2
print("f externo=", fe)
print("'Pr' externo será determinado pela tabela")
Pre=4.16
print("Pr externo=", Pre)
print("Com isso podemos determinar o Nud")
Nude=0.3+((0.62*Rede**(1/2)*Pre**1/3)/(1+(0.4/Pre)**(2/3)**(1/4)))*(1+(Rede/282000)**(5/8))**(4/5)
print("Nud externo=", Nude)
print("k externo será determinado pela tabela")
ke=634*10**-3
print("k externo=", ke)
dh=de-di
print("dh=", int(dh*1000), "mm")
hi=Nudi*ki/dh
he=Nude*ke/dh
print("entalpia interna=", hi)
print("entalpia externa=", he)
print("Temos que 1/U=1/hi+1/he")
U=(hi*he)/(hi+he)
print("U=",U, "W/(m**2*K)")
A=Cmin*nut/U
print("Assim temos que a área transversal do trocador de calor será=",A, "m**2")
L=A/(2*pi*de)
print("O comprimento do tubo será(L)=", L*1000,"mm")
print("Como podemos observar, o comprimento L é bem menor em relação ao diâmetro externo. Para isso refazeremos os calculos dividindo em tubos o projeto")

print("Para mantermos o escolament ideal faremos com que o tamanho dos tubos sejam iguais á seu comprimento")
n= round(de/L)
print("O número de tubos utilizados será", n)
det=de/n
det=(round(det*1000))/1000
dit=det/2
print("O diâmetro externo de cada tubo será", det*1000, "mm")
print("O diâmetro interno de cada tubo será", dit*1000, "mm")
print("Como demonstramos todas as propriedades se mantiveram constantes. Ou seja todos os coeficiente já foram calculados")
print("Iremos considerar um fator de empacotamento dos tubos de 0.5")
D=(2*n*det**2)**(1/2)
D=int((D*1000)+1)/1000
pack=(det**2*n)/D**2
L=(A/n)/(2*pi*det)
print("O diâmtro interno total do trocador será",D*1000,"mm e recalculado um fator de empacotamento de", round(pack,3))
print("O trocador de calor terá uma chapa de aço de 10mm de espessura totalizando", (D*1000)+20,"mm de diâmetro")
print("O comprimento do trocador recalculado será",L*1000,"mm")
print("O material utilizado será aço 1020")
print()
print()
print("item c")
print()
print("Será considerada água saturada no estado de vapor")
cpf=(1.951+1.993)/2
print("calor específico da óleo",cpf)
cpq=(7*0.425+3*0.331)/10
print("calor específico da água",cpq)
mq=0.22
Tqin=250+273.15
Tqout=50+273.15
Tfin=40+273.15
Tfout=44.9+273.15
print("Consideraremos que Cmin será igual á Cq")
Cq=cpq*mq
Cmin=Cq
print("Cmin=Cq=",Cq,"W/K")
qmax=Cmin*(Tqin-Tfin)
print("qmax=",qmax,"W")
q=mq*cpq*(Tqin-Tqout)
print("A troca de calor do sistema é:",q,"W")
mf=q/(cpf*(Tfout-Tfin))
print("a vazão massica do fluído frio é:",mf)
print()
print("Consideraremos que Cmin será igual á Cq")
Cf=mf*cpf*(Tfout-Tfin)
Cmax=Cf
print("Cmax=Cf=",Cf,"W/K")
Cr=Cmin/Cmax
print("Cr=",Cr)
epsilion=q/qmax
print("Com isso aproximamos Cr para 0, e temos que NUT=ln*(1-epsilion)")
print("efetividade do sitema=",epsilion)
nut=-math.log(1-epsilion)
print("NUT=", nut)
print("Dado que Red=4*mdot/pi*d*mi, e sabendo que para escoamento turbulento Red>2300")
print("Para fins de calculo consideraremos Red=3000, para que possamos estabelecer certas relações com equações que exigem que renolds seja superior a 3000")
Rede=3000
mif=(25.3*10**-2+14.1*10**-2)/2
print("viscosidade da óleo=", mif, "N*s/m**2")
dce=4*mf/(Rede*pi*mif)
print(dce)
print("O valor máximo em milímetros dos tubos para serem turbulentos são:",dce*1000,"mm")
de=int(1000*dce)/1000
print("A dimensão externa do tudo será=",int(de*1000),"mm")
Rede=4*mf/(de*pi*mif)
print("Red externo=", Rede)
print("Será calculado o coeficiente de atrito 'fe'")
fe=(0.790*math.log(Rede)-1.64)**-2
print("f externo=", fe)
print("'Pr' externo será determinado pela tabela")
Pre=(3400+1965)/2
print("Pr externo=", Pre)
print("Com isso podemos determinar o Nud")
Nude=0.3+((0.62*Rede**(1/2)*Pre**1/3)/(1+(0.4/Pre)**(2/3)**(1/4)))*(1+(Rede/282000)**(5/8))**(4/5)
print("Nud=", Nude)
print("k externo será determinado pela tabela")
ke=(145*10**-3+143*10**-3)/2
print("k externo=", ke)
print("Ou seja, o tubo pode ter o tamanho que se desejar, para tal usaremos que o diâmetro externo é o dobro do interno")
di=de/2
miq=(7*13.79*10**-6+3*14.14*10**-6)/10
print("viscosidade do água=", miq, "N*s/m**2")
print("Para questões de projeto os tubos escolhidos terão como dimensão interna",di*1000,"mm")   
print()
print("Apartir disso podemos calcular a entalpia do interna, mas antes será calculado o novo Red interno")
Redi=4*mq/(di*pi*miq)
print("Red interno=", Redi)
print("Será calculado o coeficiente de atrito 'fi'")
fi=(0.790*math.log(Redi)-1.64)**-2
print("f interno=", fi)
print("Pr será determinado pela tabela")
Pri=(7*1.075+3*1.1)/10
print("Pr interno=", Pri)
print("Com isso podemos determinar o Nud")
Nudi=((fi/8)*(Redi-1000)*Pri)/(1+12.7*(fi/8)**2*(Pri**(2/3)-1))
print("Nud interno=", Nudi)
print("k será determinado pela tabela")
ki=(7*29.8*10**-3+3*3-.4*10**-3)/10
print("k interno=", ki)
print()
print("Para determinarmos a entalpia interna necessitamos do 'dh', que é dado  tanto em função do diâmetro interno(di) como do externo(de). Para isso calcularemos primeiramento o 'de'")
dh=de-di
print("dh=", int(dh*1000), "mm")
hi=Nudi*ki/dh
he=Nude*ke/dh
print("entalpia interna=", hi)
print("entalpia externa=", he)
print("Temos que 1/U=1/hi+1/he")
U=(hi*he)/(hi+he)
print("U=",U, "W/(m**2*K)")
A=Cmin*nut/U
print("Assim temos que a área transversal do trocador de calor será=",A, "m**2")
L=A/(2*pi*de)
print("O comprimento do tubo será(L)=", L*1000,"mm")
print("Como podemos observar, o comprimento L é bem menor em relação ao diâmetro externo. Para isso refazeremos os calculos dividindo em tubos o projeto")
print("Para mantermos o escolament ideal faremos com que o tamanho dos tubos sejam iguais á seu comprimento")
n= round(de/L)
print("O número de tubos utilizados será", n)
det=de/n
det=(round(det*1000000))/1000000
dit=det/2
print("O diâmetro externo de cada tubo será", det*1000, "mm")
print("O diâmetro interno de cada tubo será", dit*1000, "mm")
print("Como demonstramos todas as propriedades se mantiveram constantes. Ou seja todos os coeficiente já foram calculados")
print("Iremos considerar um fator de empacotamento dos tubos de 0.5")
D=(2*n*det**2)**(1/2)
D=int((D*100000)+1)/100000
pack=(det**2*n)/D**2
L=(A/n)/(2*pi*det)
print("O diâmtro interno total do trocador será",D*1000,"mm e recalculado um fator de empacotamento de", round(pack,3))
espessura=0.1
Dt=D+2*espessura/1000
print("O trocador de calor terá uma chapa de aço de 0.1mm de espessura totalizando", Dt*1000,"mm de diâmetro")
print("O comprimento do trocador recalculado será",L*1000,"mm")
print("Para suportar as tensões o material do tubo será grafeno feito em laboratório, os tubos interno serão de gráfeno da mais alta qualidade arranjados a nível atómico")
print()
print()
print("item d")
print()
print("As perdas de calor na superfície se darão por convecção")
print("Será considerado que a temperatura na vizinhança como 277K")
print("O ar incidirá sobre a superfície externa do cilindro num escoamento cruzado á 10 m/s")
print("Será considerado que o escoamento do ar será parelelo seções da base do cilindro, considerando que suas perdas seriam despreziveis")
print("Propriedades do ar á 325k")
Tv=277
Ts=373
V=10
var=(15.59*10**-6+20.92*10**-6)/2
kar=(26.3*10**-3+30.0*10**-3)/2
Prar=(0.707+0.700)/2
Redar=V*Dt/var
print("O valor do Renolds do ar é ",Redar)
Nudar=0.3+((0.62*Redar**(1/2)*Prar**1/3)/(1+(0.4/Prar)**(2/3)**(1/4)))*(1+(Redar/282000)**(5/8))**(4/5)
print("O valor do Nud do ar é ",)
h=Nudar*kar/Dt
print("A eltalpia do ar é ",h,"W/m**2*K")
q=Dt*L*h*(Ts-Tv)
print("A perda de calor é ", q ,"W")