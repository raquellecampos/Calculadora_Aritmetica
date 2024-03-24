from tkinter import *
from tkinter import ttk

# cores
cor1 = '#3b3b3b' # preto
cor2 = '#feffff' # branco
cor3 = '#38576b' # azul
cor4 = '#ECEFF1' # cinza
cor5 = '#FFAB40' # laranja

janela = Tk()
janela.title('Calculadora')
# definir largura e comprimento
janela.geometry('235x318') 
janela.config(bg=cor1)

# criando Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando os botões
btn1 = Button(frame_corpo, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn1.place(x=0, y=0) # x verical y horizontal
btn2 = Button(frame_corpo, text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn2.place(x=118, y=0)
btn3 = Button(frame_corpo, text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn3.place(x=177, y=0)

janela.mainloop()