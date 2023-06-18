# Design a password management application that securely stores and manages user credentials. 
# Implement features like encryption, password generation, and integration with a database. 
# This project will allow you to explore concepts such as encryption algorithms, data security, and user authentication. 

import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        # LAYOUT
        sg.theme('Black')
        layout = [
            [sg.Text("Site/Software", size=(10, 1)), sg.Input(key="site", size=(20, 1))],
            [sg.Text("Email/Usuário", size=(10, 1)), sg.Input(key="usuario", size=(20,1))],
            [sg.Text("Quantidade de caracteres"), sg.Combo(values=list(range(30)), key="total_chars", default_value=1, size=(3,1))],
            [sg.Output(size=(32, 5))],
            [sg.Button("Gerar Senha")]
        ]

        # DECLARAR JANELA
        self.janela = sg.Window("Password Generator", layout)
    
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break

    def salvar_senha(self):
        pass

gen = PassGen()
gen.Iniciar()