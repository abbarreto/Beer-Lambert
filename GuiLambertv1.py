#!/usr/bin/python3
#endereço do compilador para usar o executável

#import dos módulos:
import tkinter as tk
from tkinter import ttk
import serial
import numpy as np
Polynomial = np.polynomial.Polynomial
import math
import matplotlib.pyplot as plt
#---------------------
#Variáveis globais:
global portaUSB
portaUSB = ""
global azul
azul = False
global verde
verde = False
global vermelho
vermelho = False
global l
l = 0
global cor
cor = ""
global Analito
Analito = " "
global dados_c
dados_c = []
global P0
P0 = 0
global P1
P1 = 0
global P2
P2 = 0
global P3
P3 = 0
global P4
P4 = 0
global P5
P5 = 0
global P6
P6 = 0
global P7
P7 = 0
global P8
P8 = 0
global dados_P
dados_P = []
global dados_A
dados_A = []
global A0
A0 = 0
global A1
A1 = 0
global A2
A2 = 0
global A3
A3 = 0
global A4
A4 = 0
global A5
A5 = 0
global A6
A6 = 0
global A7
A7 = 0
global A8
A8 = 0
#--------------------
#Programação dos botões:
def create_porta():
    global portaUSB
    aux = temp.get()
    try:
        portaUSB = serial.Serial(aux, 9600)
        botao_Port.config(text = "Desconectar",command = close_porta)
        status_Conexao.config(text='==== CONECTADO ====')
    except:
        botao_Port.config(text = "Conectar")
        status_Conexao.config(text='==== Porta Inexistente ====')
    #if portaUSB != []:
    #    botao_Port.config(text = "Conectado!")
    #    status_Conexao.config(text='== CONECTADO ==')
    #if portaUSB == []:
    #    botao_Port.config(text = "Desconectado!")
    #    status_Conexao.config(text='== Porta Inexistente ==')

def close_porta():
    global portaUSB
    sen_command('d')
    portaUSB.close()
    botao_Port.config(text = "Conectar",command = create_porta)
    status_Conexao.config(text='==== DESCONECTADO ====')
    botaoLEDAzul.config(fg = "black", bg = "white", highlightthickness = 0)
    labelLEDAzul.config(text = "Desligado")
    botaoLEDVerde.config(fg = "black", bg = "white", highlightthickness = 0)
    labelLEDVerde.config(text = "Desligado")
    botaoLEDVermelho.config(fg = "black", bg = "white", highlightthickness = 0)
    labelLEDVermelho.config(text = "Desligado")

def sen_command(cod):
    aux = str(cod)
    portaUSB.write(aux.encode())

def comando(op):
    global azul
    global verde
    global vermelho
    global l
    global cor

    if (op == 1 and azul == False):
        #print("Led Azul Ligado")
        sen_command('b')
        botaoLEDAzul.config(fg = "white", bg = "blue", highlightthickness = 0)
        labelLEDAzul.config(text = "Ligado")
        botaoLEDVerde.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDVerde.config(text = "Desligado")
        botaoLEDVermelho.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDVermelho.config(text = "Desligado")
        vermelho = False
        verde = False 
        azul = True
        cor = 'azul'
        l = 450
    elif (op == 1 and azul == True):
        #print('Led Azul Desligado')
        sen_command('d')
        botaoLEDAzul.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDAzul.config(text = "Desligado")
        azul = False

    elif (op == 2 and verde == False):
        #print("Led Vede Ligado")
        sen_command('g')
        botaoLEDVerde.config(fg = "white", bg = "green", highlightthickness = 0)
        labelLEDVerde.config(text = "Ligado")
        botaoLEDAzul.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDAzul.config(text = "Desligado")
        botaoLEDVermelho.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDVermelho.config(text = "Desligado")
        vermelho = False
        azul = False
        verde = True
        cor = 'verde'
        l = 550
    elif (op == 2 and verde == True):
        #print('Led Verde Desligado')
        sen_command('d')
        botaoLEDVerde.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDVerde.config(text = "Desligado")
        verde = False    

    elif (op == 3 and vermelho == False):
        #print('Led Vermelho Ligado')
        sen_command('r')
        botaoLEDVermelho.config(fg = "white", bg = "red", highlightthickness = 0)
        labelLEDVermelho.config(text = "Ligado")
        botaoLEDAzul.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDAzul.config(text = "Desligado")
        botaoLEDVerde.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDVerde.config(text = "Desligado")
        verde = False  
        azul = False
        vermelho = True
        cor = 'vermelho'
        l = 700
    elif (op == 3 and vermelho == True):
        #print('Led Vermelho Desligado')
        sen_command('d')
        botaoLEDVermelho.config(fg = "black", bg = "white", highlightthickness = 0)
        labelLEDVermelho.config(text = "Desligado")
        vermelho = False
def medir(n):
    global dados_c
    global dados_P
    global dados_A
    global A0
    global A1
    global A2
    global A3
    global A4
    global A5
    global A6
    global A7
    global A8
    global P0
    global P1
    global P2
    global P3
    global P4
    global P5
    global P6
    global P7
    global P8
    if n == 0:
        c0 = float(0.00000)
        dados_c.insert(0, c0)
        sen_command('l')
        P0 = float(portaUSB.readline())
        dados_P.insert(0, P0)
        A0 = calc_A(0,0)
        dados_A.insert(0, A0)
        varTextLuminC0 = tk.StringVar()
        varTextAbsorC0 = tk.StringVar()
        varTextLuminC0.set(str("%.1f" % dados_P[0]))
        varTextAbsorC0.set(str("%.3f" % dados_A[0]))
        labelLuminC0.config(textvariable = varTextLuminC0)
        labelAbsorC0.config(textvariable = varTextAbsorC0)
    if n == 1:
        c1 = float(entryC1.get())
        dados_c.insert(1,c1)
        sen_command('l')
        P1 = float(portaUSB.readline())
        dados_P.insert(1, P1)
        A1 = calc_A(0,1)
        dados_A.insert(1,A1)
        varTextLuminC1 = tk.StringVar()
        varTextAbsorC1 = tk.StringVar()
        varTextLuminC1.set(str("%.1f" % dados_P[1]))
        varTextAbsorC1.set(str("%.3f" % dados_A[1]))
        labelLuminC1.config(textvariable = varTextLuminC1)
        labelAbsorC1.config(textvariable = varTextAbsorC1)
    if n == 2:
        c2 = float(entryC2.get())
        dados_c.insert(2,c2)
        sen_command('l')
        P2 = float(portaUSB.readline())
        dados_P.insert(2, P2)
        A2 = calc_A(0,2)
        dados_A.insert(2, A2)
        varTextLuminC2 = tk.StringVar()
        varTextAbsorC2 = tk.StringVar()
        varTextLuminC2.set(str("%.1f" % dados_P[2]))
        varTextAbsorC2.set(str("%.3f" % dados_A[2]))
        labelLuminC2.config(textvariable = varTextLuminC2)
        labelAbsorC2.config(textvariable = varTextAbsorC2)
    if n == 3:
        c3 = float(entryC3.get())
        dados_c.insert(3,c3)
        sen_command('l')
        P3 = float(portaUSB.readline())
        dados_P.insert(3, P3)
        A3 = calc_A(0,3)
        dados_A.insert(3, A3)
        varTextLuminC3 = tk.StringVar()
        varTextAbsorC3 = tk.StringVar()
        varTextLuminC3.set(str("%.1f" % dados_P[3]))
        varTextAbsorC3.set(str("%.3f" % dados_A[3]))
        labelLuminC3.config(textvariable = varTextLuminC3)
        labelAbsorC3.config(textvariable = varTextAbsorC3)
    if n == 4:
        c4 = float(entryC4.get())
        dados_c.insert(4,c4)
        sen_command('l')
        P4 = float(portaUSB.readline())
        dados_P.insert(4, P4)
        A4 = calc_A(0,4)
        dados_A.insert(4, A4)
        varTextLuminC4 = tk.StringVar()
        varTextAbsorC4 = tk.StringVar()
        varTextLuminC4.set(str("%.1f" % dados_P[4]))
        varTextAbsorC4.set(str("%.3f" % dados_A[4]))
        labelLuminC4.config(textvariable = varTextLuminC4)
        labelAbsorC4.config(textvariable = varTextAbsorC4)
    if n == 5:
        c5 = float(entryC5.get())
        dados_c.insert(5,c5)
        sen_command('l')
        P5 = float(portaUSB.readline())
        dados_P.insert(5, P5)
        A5 = calc_A(0,5)
        dados_A.insert(5, A5)
        varTextLuminC5 = tk.StringVar()
        varTextAbsorC5 = tk.StringVar()
        varTextLuminC5.set(str("%.1f" % dados_P[5]))
        varTextAbsorC5.set(str("%.3f" % dados_A[5]))
        labelLuminC5.config(textvariable = varTextLuminC5)
        labelAbsorC5.config(textvariable = varTextAbsorC5)
    if n == 6:
        c6 = float(entryC6.get())
        dados_c.insert(6,c6)
        sen_command('l')
        P6 = float(portaUSB.readline())
        dados_P.insert(6, P6)
        A6 = calc_A(0,6)
        dados_A.insert(6, A6)
        varTextLuminC6 = tk.StringVar()
        varTextAbsorC6 = tk.StringVar()
        varTextLuminC6.set(str("%.1f" % dados_P[6]))
        varTextAbsorC6.set(str("%.3f" % dados_A[6]))
        labelLuminC6.config(textvariable = varTextLuminC6)
        labelAbsorC6.config(textvariable = varTextAbsorC6)
    if n == 7:
        c7 = float(entryC7.get())
        dados_c.insert(7,c7)
        sen_command('l')
        P7 = float(portaUSB.readline())
        dados_P.insert(7, P7)
        A7 = calc_A(0,7)
        dados_A.insert(7, A7)
        varTextLuminC7 = tk.StringVar()
        varTextAbsorC7 = tk.StringVar()
        varTextLuminC7.set(str("%.1f" % dados_P[7]))
        varTextAbsorC7.set(str("%.3f" % dados_A[7]))
        labelLuminC7.config(textvariable = varTextLuminC7)
        labelAbsorC7.config(textvariable = varTextAbsorC7)
    if n == 8:
        c8 = float(entryC8.get())
        dados_c.insert(8,c8)
        sen_command('l')
        P8 = float(portaUSB.readline())
        dados_P.insert(8, P8)
        A8 = calc_A(0,8)
        dados_A.insert(8, A8)
        varTextLuminC8 = tk.StringVar()
        varTextAbsorC8 = tk.StringVar()
        varTextLuminC8.set(str("%.1f" % dados_P[8]))
        varTextAbsorC8.set(str("%.3f" % dados_A[8]))
        labelLuminC8.config(textvariable = varTextLuminC8)
        labelAbsorC8.config(textvariable = varTextAbsorC8)
def limpar():
    global dados_c
    dados_c = []
    varAnalito.delete(0, 'end')
    entryC1.delete(0, 'end')
    entryC2.delete(0, 'end')
    entryC3.delete(0, 'end')
    entryC4.delete(0, 'end')
    entryC5.delete(0, 'end')
    entryC6.delete(0, 'end')
    entryC7.delete(0, 'end')
    entryC8.delete(0, 'end')
    resetar()
    
def resetar():
    varTextLuminC0 = tk.StringVar()
    varTextLuminC0.set("aguardando")
    varTextAbsorC0 = tk.StringVar()
    varTextAbsorC0.set("aguardando")
    labelLuminC0.config(textvariable = varTextLuminC0)
    labelAbsorC0.config(textvariable = varTextAbsorC0)
    varTextLuminC1 = tk.StringVar()
    varTextLuminC1.set("aguardando")
    varTextAbsorC1 = tk.StringVar()
    varTextAbsorC1.set("aguardando")
    labelLuminC1.config(textvariable = varTextLuminC0)
    labelAbsorC1.config(textvariable = varTextAbsorC0)
    varTextLuminC2 = tk.StringVar()
    varTextLuminC2.set("aguardando")
    varTextAbsorC2 = tk.StringVar()
    varTextAbsorC2.set("aguardando")
    labelLuminC2.config(textvariable = varTextLuminC0)
    labelAbsorC2.config(textvariable = varTextAbsorC0)
    varTextLuminC3 = tk.StringVar()
    varTextLuminC3.set("aguardando")
    varTextAbsorC3 = tk.StringVar()
    varTextAbsorC3.set("aguardando")
    labelLuminC3.config(textvariable = varTextLuminC0)
    labelAbsorC3.config(textvariable = varTextAbsorC0)
    varTextLuminC4 = tk.StringVar()
    varTextLuminC4.set("aguardando")
    varTextAbsorC4 = tk.StringVar()
    varTextAbsorC4.set("aguardando")
    labelLuminC4.config(textvariable = varTextLuminC0)
    labelAbsorC4.config(textvariable = varTextAbsorC0)
    varTextLuminC5 = tk.StringVar()
    varTextLuminC5.set("aguardando")
    varTextAbsorC5 = tk.StringVar()
    varTextAbsorC5.set("aguardando")
    labelLuminC5.config(textvariable = varTextLuminC0)
    labelAbsorC5.config(textvariable = varTextAbsorC0)
    varTextLuminC6 = tk.StringVar()
    varTextLuminC6.set("aguardando")
    varTextAbsorC6 = tk.StringVar()
    varTextAbsorC6.set("aguardando")
    labelLuminC6.config(textvariable = varTextLuminC0)
    labelAbsorC6.config(textvariable = varTextAbsorC0)
    varTextLuminC7 = tk.StringVar()
    varTextLuminC7.set("aguardando")
    varTextAbsorC7 = tk.StringVar()
    varTextAbsorC7.set("aguardando")
    labelLuminC7.config(textvariable = varTextLuminC0)
    labelAbsorC7.config(textvariable = varTextAbsorC0)
    varTextLuminC8 = tk.StringVar()
    varTextLuminC8.set("aguardando")
    varTextAbsorC8 = tk.StringVar()
    varTextAbsorC8.set("aguardando")
    labelLuminC8.config(textvariable = varTextLuminC0)
    labelAbsorC8.config(textvariable = varTextAbsorC0)
def calc_A(P0,Pi):
    A = math.log10(dados_P[P0]/dados_P[Pi])
    return A
def plotar():
    subs = varAnalito.get()
    ## Variáveis globais:
    conc = []
    Absor = []
    for valorA in dados_A:
        Absor.append(valorA)
    for valorC in dados_c:
        conc.append(valorC)
    ## ----------------------------        
    cmin, cmax = min(conc), max(conc)
    pfit, stats = Polynomial.fit(conc, Absor, 1, 
                             full=True, 
                             window=(cmin, cmax),
                             domain=(cmin, cmax))
    plt.plot(conc, Absor, 'ko')
    plt.plot(conc, pfit(conc), 'r')
    ## Configuração dos eixos do gráfico
    plt.title("{}".format(subs))
    plt.grid(True)
    #ymax = float(Absor[-1]) + 0.005
    #ymin = float(Absor[0]) - 0.001 
    #xmax = float(conc[-1]) + 0.5
    #xmin = float(conc[0]) - 0.1
    #plt.ylim((ymin, ymax))
    #plt.xlim((xmin, xmax))
    plt.xlabel("Concentração molar (" r'$ \times 10^{-5}$' "mol/L)")
    plt.ylabel("Absorbância para " r'$ \lambda \approx $' "{}nm ({})".format(l, cor))
    #plt.ylabel("Absorbância ")

    plt.show()
#---------------------------------------------------
#Analito = " "    
#Inicializa a janela principal com título e tamanho:
janelaPrincipal = tk.Tk()
janelaPrincipal.title("Lei de Lambert")
janelaPrincipal.configure(bg='white')
janelaPrincipal.geometry('470x450')
janelaPrincipal.resizable(width=False, height=False)
#---------------------------------------------------

#Layout
text_Port = tk.Label(janelaPrincipal,font=("Times New Roman", 12, "bold"), text='Informe a Porta: ',fg = "black", bg = "white")
text_Port.grid(column=0,row=0)
temp = tk.StringVar()
porta = tk.Entry(janelaPrincipal, text = "aaaa",bd=2, width = 24,fg = "black", bg = "white",textvariable = temp)
porta.focus_set()
porta.grid(column=1,columnspan=3,row=0)
botao_Port = tk.Button(text='Conectar', width = 10,command = create_porta,fg = "black", bg = "white")
botao_Port.grid(column=4,row=0)

btnLimpar = tk.Button(text='Limpar', width = 10,command = limpar,fg = "black", bg = "white")
btnLimpar.grid(column=4, row=1)
status_Port = tk.Label(janelaPrincipal, text='Status da conexão: ',fg = "black", bg = "white")
status_Port.grid(column=0,row=1)

status_Conexao = tk.Label(janelaPrincipal, text='==== DESCONECTADO ====',fg = "black", bg = "white")
status_Conexao.grid(column=1,columnspan=3,row=1)

labelAnalito = tk.Label(janelaPrincipal, text = "Digite o nome da analito",fg = "black", bg = "white")
labelAnalito.grid(column=1,columnspan=3, row=2)

varAnalito = tk.Entry(janelaPrincipal, bd=2, width = 18,fg = "black", bg = "white")
varAnalito.focus_set()
varAnalito.grid(column=1,columnspan=3,row=3)

labelLED = tk.Label(janelaPrincipal, text = "Escolha a cor do LED",fg = "black", bg = "white")
labelLED.grid(column=1,columnspan=3,row=4)

botaoLEDAzul = tk.Button(janelaPrincipal,fg = "black", bg = "white",text = "Azul", width = 5, command = lambda: comando(1))
botaoLEDAzul.grid(column=1,row=5)
labelLEDAzul = tk.Label(janelaPrincipal, text = "Desligado",fg = "black", bg = "white")
labelLEDAzul.grid(column=1,row=6)

botaoLEDVerde = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Verde", width = 5,command = lambda: comando(2))
botaoLEDVerde.grid(column=2,row=5)
labelLEDVerde = tk.Label(janelaPrincipal, text = "Desligado",fg = "black", bg = "white")
labelLEDVerde.grid(column=2,row=6)


botaoLEDVermelho = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Vermelho", width = 5,command = lambda: comando(3))
botaoLEDVermelho.grid(column=3,row=5)
labelLEDVermelho = tk.Label(janelaPrincipal, text = "Desligado",fg = "black", bg = "white")
labelLEDVermelho.grid(column=3,row=6)

status_LED = tk.Label(janelaPrincipal, text ="Status do LED: ", fg = "black", bg = "White")
status_LED.grid(column = 0, row = 6)

ttk.Separator(janelaPrincipal, orient = 'horizontal').grid(column=0, columnspan = 5, row = 7, sticky = 'ew')

botaoPlotar = tk.Button(janelaPrincipal, text = "Plotar",fg = "black", bg = "white", height = 5,width = 10, command = lambda: plotar())
botaoPlotar.grid(column=4,row=2,rowspan=4)

botaoSair = tk.Button(janelaPrincipal, text = "Sair",fg = "black", bg = "white", height = 5, width = 10,command = janelaPrincipal.quit)
botaoSair.grid(column=0,row=2,rowspan=4)

labelLeituras= tk.Label(janelaPrincipal, font=("Times New Roman", 12, "bold"), text ="== MEDIDAS == ", fg = "black", bg = "White")
labelLeituras.grid(column = 0, row = 8)
labelC0 = tk.Label(janelaPrincipal, font=("Times New Roman", 12, "bold"), text="(mol/L)", fg = "black", bg = "White").grid(column = 1, row= 8)

labelLeituraBranco = tk.Label(janelaPrincipal, text="Branco", fg = "black", bg = "White")
labelLeituraBranco.grid(column = 0, row = 9)
labelC0 = tk.Label(janelaPrincipal, text="0.00000", fg = "black", bg = "White").grid(column = 1, row= 9)

labelLeituraC1 = tk.Label(janelaPrincipal, text="Concentração 1", fg = "black", bg = "White")
labelLeituraC1.grid(column = 0, row = 10)
entryC1 = tk.Entry(janelaPrincipal, width = 6)
entryC1.grid(column = 1, row= 10)

labelLeituraC2 = tk.Label(janelaPrincipal, text="Concentração 2", fg = "black", bg = "White")
labelLeituraC2.grid(column = 0, row = 11)
entryC2 = tk.Entry(janelaPrincipal, width = 6)
entryC2.grid(column = 1, row= 11)

labelLeituraC3 = tk.Label(janelaPrincipal, text="Concentração 3", fg = "black", bg = "White")
labelLeituraC3.grid(column = 0, row = 12)
entryC3 = tk.Entry(janelaPrincipal, width = 6)
entryC3.grid(column = 1, row= 12)

labelLeituraC4 = tk.Label(janelaPrincipal, text="Concentração 4", fg = "black", bg = "White")
labelLeituraC4.grid(column = 0, row = 13)
entryC4 = tk.Entry(janelaPrincipal, width = 6)
entryC4.grid(column = 1, row= 13)

labelLeituraC5 = tk.Label(janelaPrincipal, text="Concentração 5", fg = "black", bg = "White")
labelLeituraC5.grid(column = 0, row = 14)
entryC5 = tk.Entry(janelaPrincipal, width = 6)
entryC5.grid(column = 1, row= 14)

labelLeituraC6 = tk.Label(janelaPrincipal, text="Concentração 6", fg = "black", bg = "White")
labelLeituraC6.grid(column = 0, row = 15)
entryC6 = tk.Entry(janelaPrincipal, width = 6)
entryC6.grid(column = 1, row= 15)

labelLeituraC7 = tk.Label(janelaPrincipal, text="Concentração 7", fg = "black", bg = "White")
labelLeituraC7.grid(column = 0, row = 16)
entryC7 = tk.Entry(janelaPrincipal, width = 6)
entryC7.grid(column = 1, row= 16)

labelLeituraC8 = tk.Label(janelaPrincipal, text="Concentração 8", fg = "black", bg = "White")
labelLeituraC8.grid(column = 0, row = 17)
entryC8 = tk.Entry(janelaPrincipal, width = 6)
entryC8.grid(column = 1, row= 17)

btnCalibrar = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Calibrar", width = 3,command = lambda: medir(0))
btnCalibrar.grid(column = 2, row = 9)

btnResetar =tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Resetar", width = 3,command = lambda: resetar())
btnResetar.grid(column = 2, row = 8)

btnMedirC1 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(1))
btnMedirC1.grid(column = 2, row = 10)

btnMedirC2 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(2))
btnMedirC2.grid(column = 2, row = 11)

btnMedirC3 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(3))
btnMedirC3.grid(column = 2, row = 12)

btnMedirC4 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(4))
btnMedirC4.grid(column = 2, row = 13)

btnMedirC5 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(5))
btnMedirC5.grid(column = 2, row = 14)

btnMedirC6 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(6))
btnMedirC6.grid(column = 2, row = 15)

btnMedirC7 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(7))
btnMedirC7.grid(column = 2, row = 16)

btnMedirC8 = tk.Button(janelaPrincipal, fg = "black", bg = "white", text = "Medir", width = 3,command = lambda: medir(8))
btnMedirC8.grid(column = 2, row = 17)

labelLumin= tk.Label(janelaPrincipal, font=("Times New Roman", 12, "bold"),text ="Intensidades", fg = "black", bg = "White")
labelLumin.grid(column = 3, row = 8)

labelAbsor= tk.Label(janelaPrincipal, font=("Times New Roman", 12, "bold"), text ="Absorbâncias", fg = "black", bg = "White")
labelAbsor.grid(column = 4, row = 8)

labelLuminC0 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC0.grid(column = 3, row= 9)
labelAbsorC0 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC0.grid(column = 4, row= 9)

labelLuminC1 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC1.grid(column = 3, row= 10)
labelAbsorC1 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC1.grid(column = 4, row= 10)

labelLuminC2 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC2.grid(column = 3, row= 11)
labelAbsorC2 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC2.grid(column = 4, row= 11)

labelLuminC3 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC3.grid(column = 3, row= 12)
labelAbsorC3 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC3.grid(column = 4, row= 12)

labelLuminC4 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC4.grid(column = 3, row= 13)
labelAbsorC4 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC4.grid(column = 4, row= 13)

labelLuminC5 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC5.grid(column = 3, row= 14)
labelAbsorC5 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC5.grid(column = 4, row= 14)

labelLuminC6 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC6.grid(column = 3, row= 15)
labelAbsorC6 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC6.grid(column = 4, row= 15)

labelLuminC7 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC7.grid(column = 3, row= 16)
labelAbsorC7 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC7.grid(column = 4, row= 16)

labelLuminC8 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelLuminC8.grid(column = 3, row= 17)
labelAbsorC8 = tk.Label(janelaPrincipal, text="aguardando", fg = "black", bg = "White")
labelAbsorC8.grid(column = 4, row= 17)

#---------------------------------------------------

#Inicia e abre a janela:
janelaPrincipal.mainloop()
#---------------------------------------------------
