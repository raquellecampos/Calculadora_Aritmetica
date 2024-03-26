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

btn4 = Button(frame_corpo, text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn4.place(x=0, y=52)
btn5 = Button(frame_corpo, text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn5.place(x=59, y=52)
btn6 = Button(frame_corpo, text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn6.place(x=118, y=52)
btn7 = Button(frame_corpo, text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn7.place(x=177, y=52)

btn8 = Button(frame_corpo, text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn8.place(x=0, y=52)
btn9 = Button(frame_corpo, text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn9.place(x=59, y=52)
btn10 = Button(frame_corpo, text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn10.place(x=118, y=52)
btn11 = Button(frame_corpo, text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn11.place(x=177, y=52)

btn12 = Button(frame_corpo, text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn12.place(x=0, y=52)
btn13 = Button(frame_corpo, text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn13.place(x=59, y=52)
btn14 = Button(frame_corpo, text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn14.place(x=118, y=52)
btn15 = Button(frame_corpo, text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn15.place(x=177, y=52)

btn16 = Button(frame_corpo, text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn16.place(x=0, y=0) # x verical y horizontal
btn17 = Button(frame_corpo, text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn17.place(x=118, y=0)
btn18 = Button(frame_corpo, text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn18.place(x=177, y=0)

janela.mainloop()