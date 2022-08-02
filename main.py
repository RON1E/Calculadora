# Importando Tkinter
from tkinter import *
from tkinter import ttk

# adicionando cores

cor1 = "#0f0f0f"  # PRETO


janela = Tk()
janela.title("Calculadora")
janela.geometry("250x350")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=250, height=50)
frame_tela.grid(row=0, column=0)


janela.mainloop()
