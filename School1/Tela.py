import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.screenmanager import Screen, ScreenManager

class Adm(ScreenManager):
    pass

class Inicio(Screen):
    def click(self):

        if self.ids.txtPass.text == '':
            if self.ids.lblTeste.text != 'Hello World!':
                self.ids.lblTeste.text = 'Hello World!'
            else:
                self.ids.lblTeste.text = 'Ola'
        else:
            self.ids.lblTeste.text = self.ids.txtPass.text

    def clear(self):
        self.ids.lblTeste.text = ''

class Tela(App):
    def build(self):
        #btn = Button(text='Enter')
        return Adm()

Tela().run()
