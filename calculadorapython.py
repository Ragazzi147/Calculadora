# importando tkinter
from tkinter import *
from tkinter import ttk

# cores 

cor1 = "#0d3c4a"  # verde bem escuro
cor2 = "#d4c00d"  # amarelo botão
cor3 = "#121209"  # preto escuro
cor4 = "#e8e8dc"  # branco cinzaa
cor5 = "#261ce6"  # azul forte

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)


# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)


frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variavel todos os valores

todos_valores = ''




# Criando Label
valor_texto = StringVar()

# Codigo/função

def entrar_valores(event):
    
    global todos_valores

    todos_valores = todos_valores + str(event)

    
    # Passando o valor para tela
    valor_texto.set(todos_valores)


# Função para calcular


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)


# Função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")




app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('ivy 18'), bg=cor1, fg=cor4)
app_label.place(x=0, y=0)


# Criando botões 1 coluna

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor2, fg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# Botões 2 coluna

b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_4 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=60, y=52)
b_4 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=120, y=52)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor2, fg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=52)

# Botões 3 coluna

b_4 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=104)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=104)
b_7 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor2, fg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=104)

# Botões 4 coluna

b_8 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=156)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=156)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=156)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor2, fg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=156)

# Botões 5 coluna

b_1 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=208)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=208)
b_3 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor2, fg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=208)




janela.mainloop()