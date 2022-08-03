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
janela.geometry("250x333")
janela.config(bg=cor1)


# Criando os frames
frame_tela = Frame(janela, width=250, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=250, height=300)
frame_corpo.grid(row=1, column=0)


#
# Criando os Botões da calculadora

b_1 = Button(frame_corpo, text="C", width=14, height=3, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)  # Clear/Limpar

b_2 = Button(frame_corpo, text="%", width=6, height=3, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)  # Resto da divisão

b_3 = Button(frame_corpo, text="/", width=6, height=3, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE)
b_3.place(x=182, y=0)  # Divisão

#

b_4 = Button(frame_corpo, text="7", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)  # Sete

b_5 = Button(frame_corpo, text="8", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=53)  # Oito

b_6 = Button(frame_corpo, text="9", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=53)  # Nove

b_7 = Button(frame_corpo, text="*", width=6, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE)
b_7.place(x=182, y=53)  # Asterisco

#

b_8 = Button(frame_corpo, text="6", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)  # Seis

b_9 = Button(frame_corpo, text="5", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=106)  # Cinco

b_10 = Button(frame_corpo, text="4", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=106)  # Quatro

b_11 = Button(frame_corpo, text="-", width=6, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE)
b_11.place(x=182, y=106)  # Menos

#

b_12 = Button(frame_corpo, text="1", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=159)  # Um

b_13 = Button(frame_corpo, text="2", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=159)  # Dois

b_14 = Button(frame_corpo, text="3", width=6, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=159)  # Três

b_15 = Button(frame_corpo, text="+", width=6, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE)
b_15.place(x=182, y=159)  # Mais

#

b_16 = Button(frame_corpo, text="0", width=14, height=3, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=212)  # Zero

b_17 = Button(frame_corpo, text=".", width=6, height=3, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=212)  # Ponto

b_18 = Button(frame_corpo, text="=", width=6, height=3, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE)
b_18.place(x=182, y=212)  # Igual



janela.mainloop()
