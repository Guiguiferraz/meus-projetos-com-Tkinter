import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random 

def escolheu_pedra():
    jokenpo(escolha_usuario='pedra')

def escolheu_papel():
    jokenpo(escolha_usuario='papel')

def escolheu_tesoura():
    jokenpo(escolha_usuario='tesoura')

def jokenpo(escolha_usuario):
    escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])

    if escolha_usuario == escolha_computador:
        mensagem = f'''
            Voce: {escolha_usuario.upper()}
            Eu: {escolha_computador.upper()}

            Resultado: EMPATE!
        '''
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') \
            or (escolha_usuario == 'papel' and escolha_computador == 'pedra') \
            or(escolha_usuario == 'tesoura' and escolha_computador == 'papel'): 
        mensagem = f'''
            Voce: {escolha_usuario.upper()}
            Eu: {escolha_computador.upper()}

            Resultado: VOCE GANHOU!

        '''
    else:
        mensagem = f'''
            Voce: {escolha_usuario.upper()}
            Eu: {escolha_computador.upper()}

            Resultado: EU VENCI!
        '''
    resultado.config(text=mensagem)

janela = tk.Tk()

frame = LabelFrame(janela, text='Qual voce escolhe?', padx=10, pady=10)
frame.pack()





icone_pedra = PhotoImage(file='images/pedra.png')
icone_papel = PhotoImage(file='images/papel.png')
icone_tesoura = PhotoImage(file='images/tesoura.png')

Button(frame, text='Pedra', command=escolheu_pedra, image=icone_pedra, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='Papel', command=escolheu_papel, image=icone_papel, compound=tk.LEFT).grid(column=2, row=1)
Button(frame, text='Tesoura', command=escolheu_tesoura, image=icone_tesoura, compound=tk.LEFT).grid(column=3, row=1)



resultado = Label(frame, padx=10, pady=10, justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=3)

janela.title('Pedra, Papel e Tesoura')
janela.geometry('500x200+700+200')
janela.mainloop()