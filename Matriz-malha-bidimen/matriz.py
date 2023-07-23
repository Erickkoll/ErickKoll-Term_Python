# -*- coding: utf-8 -*-
print("Aluno: Erick Cordeiro Kollross  GRR:20124195")
print("Programa criado para diciplica de trnasferência de Calor e massa via Python-Trabalho 3")
import numpy as np
from numpy.linalg import inv
print("Dado que as temperaturas são dadas por T=A**-1*Ct")
L1= [-4,1,0,0,0,1,0,0,0,0,0,0,0,0,0]
L2= [1,-4,1,0,0,0,1,0,0,0,0,0,0,0,0]
L3= [0,1,-4,1,0,0,0,1,0,0,0,0,0,0,0]
L4= [0,0,1,-4,1,0,0,0,1,0,0,0,0,0,0]
L5= [0,0,0,1,-4,0,0,0,0,1,0,0,0,0,0]
L6= [1,0,0,0,0,-4,1,0,0,0,1,0,0,0,0]
L7= [0,1,0,0,0,1,-4,1,0,0,0,1,0,0,0]
L8= [0,0,1,0,0,0,1,-4,1,0,0,0,1,0,0]
L9= [0,0,0,1,0,0,0,1,-4,1,0,0,0,1,0]
L10=[0,0,0,0,1,0,0,0,1,-4,0,0,0,0,1]
L11=[0,0,0,0,0,2,0,0,0,0,-4,1,0,0,0]
L12=[0,0,0,0,0,0,2,0,0,0,1,-4,1,0,0]
L13=[0,0,0,0,0,0,0,2,0,0,0,1,-4,1,0]
L14=[0,0,0,0,0,0,0,0,2,0,0,0,1,-4,1]
L15=[0,0,0,0,0,0,0,0,0,2,0,0,0,1,-4]
A = np.array ([L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15])
print("Nossa matriz 'A' é: ")
print(A)
print()
invA =inv(A)
print("A inversa da nossa matriz 'A' é: ")
print(invA)
print()
C= np.array ([[-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0]])
Ct = np.transpose(C)
print("Nossa matriz 'Ct' é:")
print(Ct)
print()
T=np.dot(invA,Ct)
print("A matriz das temperaturas é:")
print(T)
print()
print("Os valores das temperaturas correspondentes são:")
T1 = float(T[0])
T2 = float(T[1])
T3 = float(T[2])
T4 = float(T[3])
T5 = float(T[4])
T6 = float(T[5])
T7 = float(T[6])
T8 = float(T[7])
T9 = float(T[8])
T10 = float(T[9])
T11 = float(T[10])
T12 = float(T[11])
T13 = float(T[12])
T14 = float(T[13])
T15 = float(T[14])
print(T1)
print(T2)
print(T3)
print(T4)
print(T5)
print(T6)
print(T7)
print(T8)
print(T9)
print(T10)
print(T11)
print(T12)
print(T13)
print(T14)
print(T15)
S0=0
S1=1
qlout= 2*(T1-S0) + 2*( T2-S0 ) + 2*( T3-S0 ) + 2*( T4-S0 ) + 2*( T5-S0 )+2*( T5-S0 )+2*( T10-S0 )+(T15-S0)
print("O quatidade de calor que sai da malha é: ", qlout ,"W/m") 
qli= 2*( S1 - T1 ) + 2*( S1-T6 )+ ( S1-T11 )
print("O quatidade de calor que entra malha é:  ", qli,"W/m") 
E=(qli-qlout)
print("O erro da analítica para a numérica é: ", E)