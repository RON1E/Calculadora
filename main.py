# Importando Tkinter
from tkinter import *
from tkinter import ttk

# adicionando cores

cor1 = "#0f0f0f"  # Black/ Preto
cor2 = "#feffff"  # White/ Branca
cor3 = "#38576b"  # Blue/ Azul carregado
cor4 = "#ECEFF1"  # Grey/ Cizenta
cor5 = "#FFAB40"  # Orange/ Laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("250x350")
janela.config(bg=cor1)

# Criando os frames
frame_tela = Frame(janela, width=250, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=250, height=300)
frame_corpo.grid(row=1, column=0)


# Criando os Botões da calculadora

b_1 = Button(frame_corpo, text="C", width=14, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)  # Clear/Limpar

b_2 = Button(frame_corpo, text="%", width=8, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=111, y=0)  # Resto da divisaõ

b_3 = Button(frame_corpo, text="/", width=8, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE)
b_3.place(x=180, y=0)  # Divisão


janela.mainloop()
