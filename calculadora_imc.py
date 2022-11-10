from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# criando janela
jan = Tk()
jan.title ("Bem vindo à calculadora de IMC")
jan.geometry("310x200")
jan.configure(background="coral")
jan.resizable(width="false", height="false") 
jan.attributes("-alpha", 0.96)

# Widgets

LeftFrame = Frame(jan, width=100, height=200, bg="tan1", relief="raise")         #Frame lado esquerdo
LeftFrame.pack(side=LEFT)                                                            

RightFrame = Frame(jan, width=210, height=200, bg="khaki1", relief="raise")           #frame lado direito
RightFrame.pack(side=RIGHT)

NomeLabel = Label(LeftFrame, text="Nome:", font=("Open sans", 12), bg="tan1", fg="grey1" )
NomeLabel.place(x=(45), y=20)

NomeEntry = Entry(RightFrame, width= 30)
NomeEntry.place(x=10, y=20)

PesoLabel = Label(LeftFrame, text="Peso:", font=("Open sans", 12), bg="tan1", fg="grey1")
PesoLabel.place(x=(50), y=60)

PesoEntry = Entry(RightFrame, width=30)
PesoEntry.place(x=10, y=60)

AlturaLabel = Label(LeftFrame, text="Altura:", font=("Open sans", 12), bg="tan1", fg="grey1")
AlturaLabel.place(x=47, y=100)

AlturaEntry = ttk.Entry(RightFrame, width=30)
AlturaEntry.place(x=10, y=100)

#criando botão

def Calcular():
    
    nome = NomeEntry.get()
    peso = float(PesoEntry.get())
    altura = float(AlturaEntry.get())
    Imc = (peso / ((altura) * (altura)))
    messagebox.showinfo(title="calculo imc", message=(nome, ', seu imc é:', Imc))

BotaoCalcular = ttk.Button(RightFrame, text="Calcular", width=20, command=Calcular)
BotaoCalcular.place(x=50, y=150)

jan.mainloop()