from tkinter import *
from tkinter import ttk

# cores
cor1 = '#3b3b3b' # preto
cor2 = '#feffff' # branco
cor3 = '#38576b' # azul
cor4 = 'ECEFF1' # cinza
cor5 = 'FFAB40' # laranja

janela = Tk()
janela.title('Calculadora')
# definir largura e comprimento
janela.geometry('235x318') 
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

janela.mainloop()