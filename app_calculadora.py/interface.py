#calculos import

from calculos import soma , multi, divi


#Interface da janela

import tkinter as tk
calculadora = tk.Tk()
calculadora.title('calculadora')
calculadora.geometry('480x600')
calculadora.configure(bg = "#7D0AAA")

calculadora.columnconfigure(0, weight=1)
calculadora.columnconfigure(1,weight=1)
for i in range(6):
    calculadora.rowconfigure(i,weight=1)

#frames
frame_titulo = tk.Frame(calculadora, bg = '#7d0aaa')
frame_titulo.grid(row=0,column=0, columnspan= 2,sticky= 'n')

mensagem = tk.Frame(calculadora, bg= '#7d0aaa')
mensagem.grid(row=1, column=0)
#frames ENTRY
frame_entry= tk.Frame(calculadora, bg = '#7d0aaa')
frame_entry.grid(row=1,column=1,sticky='w')

entry1= tk.Entry(frame_entry)
entry1.grid(row=0,column=1,sticky='w', pady=20, ipadx=20)

entry2 = tk.Entry(frame_entry)
entry2.grid(row=1,column=1, sticky= 'w', pady=20, ipadx=20) 

#frames Botões
frames_botões = tk.Frame(calculadora, bg = '#7d0aaa')
frames_botões.grid(row=2,column=0, columnspan=2, padx=40, sticky= 'we', pady=(0,0))

#Label 

Titulo = tk.Label(frame_titulo, text = 'CALCULADORA', bg= '#7d0aaa', fg = 'black', font = ("Arial",32))
Titulo.grid(row=1, column=0)

m1 = tk.Label(mensagem, text= 'Insira um numero:', font= ('arial',15), bg= '#7d0aaa', fg= 'black')
m1.grid(row=1, column=0, sticky='w', pady=10)

m2 = tk.Label(mensagem, text= 'Insira um numero:', font= ('arial',15), bg= '#7d0aaa', fg= 'black')
m2.grid(row= 2, column=0, sticky= 'w', pady=10)

Resultado = tk.Frame(calculadora, bg = '#7d0aaa')
Resultado.grid(row=3, column=0, columnspan=2,  sticky= 'n')

#LABEL DOS BOTÕES
resultado_label = tk.Label(Resultado, text= 'O resultado aparecerá aqui!',  bg= '#7d0aaa', fg = 'black', font= ('arial',15))
resultado_label.grid(row=0, column=0, padx=20, pady=5)
#função dos botões

def div_Clique():
    try:
        n1 = int(entry1.get()) #Acrescentar int para que pegue numeros
        n2 = int(entry2.get())
        resultado = divi(n1,n2)
        resultado_label.config(text = f'Resultado → {resultado}', bg= '#7d0aaa', fg = 'black', font = ('arial',20))
    except ValueError:
        resultado_label.config(text = 'Apenas numeros!')

def som_Clique():
    try:
        n1 = int(entry1.get()) #Acrescentar int para que pegue numeros
        n2 = int(entry2.get())
        resultado = soma(n1,n2)
        resultado_label.config(text = f'Resultado  → {resultado}', bg= '#7d0aaa', fg = 'black', font = ('arial',20))
    except ValueError:
        resultado_label.config(text = 'Apenas numeros!')


def multi_Clique():
    try:
        n1 = int(entry1.get()) #Acrescentar int para que pegue numeros
        n2 = int(entry2.get())
        resultado = multi(n1,n2)
        resultado_label.config(text = f'Resultado  → {resultado}', bg= '#7d0aaa', fg = 'black', font = ('arial',20))
    except ValueError:
        resultado_label.config(text = 'Apenas numeros!')
        

def limpar():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    resultado_label.config(text='')
        

#BOTÕES

div_button= tk.Button(frames_botões, text= 'Divisão', command= div_Clique, bg= 'brown', fg = 'black', width=11)
div_button.grid(row=0, column=0, padx=20)

soma_button = tk.Button(frames_botões, text= 'Soma', command=som_Clique, bg= 'brown', fg = 'black', width=11)
soma_button.grid(row=0, column=1, padx=20)

multi_button = tk.Button(frames_botões, text= 'Multitiplicação', command= multi_Clique, bg= 'brown', fg = 'black', width=11)
multi_button.grid(row=0, column=2, padx=20)

tk.Button(frames_botões,text= 'Limpar', fg = 'black', bg= 'brown', command=limpar, width=15).grid(row=3, column=0, pady=10, columnspan=3, sticky= 'n')


calculadora.mainloop()
