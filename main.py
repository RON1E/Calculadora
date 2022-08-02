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

frame_tela = Frame(janela, width=250, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=250, height=300)
frame_corpo.grid(row=1, column=0)

janela.mainloop()
