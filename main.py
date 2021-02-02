from tkinter.constants import TRUE
import PySimpleGUI as sg
import hashlib

class TelaMain:
    def __init__(self):
        
        layout = [
            [sg.Text('HASH:'),sg.Input(key='pass_hash')],
            [sg.Text('WordList Path:'), sg.Input(key='wordlist')],
            [sg.Output(size=(30,15))],
            [sg.Button("submit")]
            
        ]


        self.janela = sg.Window("MD5BROKEN").layout(layout)



    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.read()
            flag = 0
            pass_hash = self.values['pass_hash']
            wordlist = self.values['wordlist']
            
            try:
                pass_file = open(wordlist, "r")
            except:
                print("No file found: ")
                quit()

            for word in pass_file:
                enc_wrd = word.encode('utf8')
                digest = hashlib.md5(enc_wrd.strip()).hexdigest()

                if digest.strip() == pass_hash.strip():
                    print(self.values, "pass found" + word)
                    flag = 1
                    break
            if flag == 0 :
                print(f"password not in list")

tela = TelaMain()
tela.Iniciar()
