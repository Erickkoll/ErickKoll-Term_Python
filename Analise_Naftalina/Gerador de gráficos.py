# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt                        
print("Aluno: Erick Cordeiro Kollross  GRR:20124195")
print("Programa criado para diciplica de transferência de Calor e massa via Python")
print("Gerador de gráficos criados a partir do Trabalho 4")
                        
def gerador_de_graficos(arquivo):                        
                                                
    x=[]
    y=[]
            
    grafico= open(arquivo,'r')
            
    for line in grafico:
        line = line.strip()
        X, Y = line.split(',')
        x.append(X)
        y.append(Y)
    
    grafico.close()
    
    return(x,y)

fig = plt.figure()
rect = fig.patch
rect.set_facecolor('white')   ##31312e

x, y = gerador_de_graficos('grafico.c.1.m.txt')
x2, y2 = gerador_de_graficos('grafico.s.10.m.txt')
x3, y3 = gerador_de_graficos('grafico.c.1.m.txt')
x4, y4 = gerador_de_graficos('grafico.c.10.m.txt')
x5, y5 = gerador_de_graficos('grafico.s.1.r.txt')
x6, y6 = gerador_de_graficos('grafico.s.10.r.txt')
x7, y7 = gerador_de_graficos('grafico.c.1.r.txt')
x8, y8 = gerador_de_graficos('grafico.c.10.r.txt')
                
                                                
ax1 = fig.add_subplot(2,4,1)
           
ax1.plot(x,y)
ax1.set_xlim(100,0)     
ax1.set_title("t x m, 1 naftalina, s/abrir amário")
ax1.set_xlabel('massa(%)')
ax1.set_ylabel('tempo(s)')
ax1.tick_params(axis='x', color='c')
ax1.tick_params(axis='y', color='c')

ax2 = fig.add_subplot(2,4,2)
ax2.set_xlim(100,0)            
ax2.plot(x2,y2)   
ax2.set_title("t x m, 10 naftalina, s/abrir amário")
ax2.set_xlabel('massa(%)')
ax2.set_ylabel('tempo(s)')
ax2.tick_params(axis='x', color='c')
ax2.tick_params(axis='y', color='c') 
                                                                                                                     
ax3 = fig.add_subplot(2,4,3)
ax3.set_xlim(100,0)            
ax3.plot(x3,y3)   
ax3.set_title("t x m, 1 naftalina, c/abrir amário")
ax3.set_xlabel('massa(%)')
ax3.set_ylabel('tempo(s)')
ax3.tick_params(axis='x', color='c')
ax3.tick_params(axis='y', color='c')

ax4 = fig.add_subplot(2,4,4)
ax4.set_xlim(100,0)            
ax4.plot(x4,y4)   
ax4.set_title("t x m, 10 naftalina, c/abrir amário")
ax4.set_xlabel('massa(%)')
ax4.set_ylabel('tempo(s)')
ax4.tick_params(axis='x', color='c')
ax4.tick_params(axis='y', color='c')

ax5 = fig.add_subplot(2,4,5)
ax5.set_xlim(100,0)
ax5.set_ylim(0,4000)             
ax5.plot(x5,y5)   
ax5.set_title("t x r, 1 naftalina, s/abrir amário")
ax5.set_xlabel('massa(%)')
ax5.set_ylabel('tempo(s)')
ax5.tick_params(axis='x', color='c')
ax5.tick_params(axis='y', color='c')

ax6 = fig.add_subplot(2,4,6)
ax6.set_xlim(100,0) 
ax6.set_ylim(0,4000)            
ax6.plot(x6,y6)   
ax6.set_title("t x r, 10 naftalina, s/abrir amário")
ax6.set_xlabel('massa(%)')
ax6.set_ylabel('tempo(s)')
ax6.tick_params(axis='x', color='c')
ax6.tick_params(axis='y', color='c')

ax7 = fig.add_subplot(2,4,7)
ax7.set_xlim(100,1)
ax7.set_ylim(0,2000)           
ax7.plot(x7,y7)   
ax7.set_title("t x r, 1 naftalina, c/abrir amário")
ax7.set_xlabel('massa(%)')
ax7.set_ylabel('tempo(s)')
ax7.tick_params(axis='x', color='c')
ax7.tick_params(axis='y', color='c')

ax8 = fig.add_subplot(2,4,8)
ax8.set_xlim(100,1)
ax8.set_ylim(0,2000)             
ax8.plot(x8,y8)   
ax8.set_title("t x r, 10 naftalina, c/abrir amário")
ax8.set_xlabel('massa(%)')
ax8.set_ylabel('tempo(s)')
ax8.tick_params(axis='x', color='c')
ax8.tick_params(axis='y', color='c')
            
plt.show()