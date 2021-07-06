import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

kivy.require('1.9.1')

class Login(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 20])

        lblUser = Label(text='Username')
        txtUser = TextInput(text='Username', multiline=False)
        lblPass = Label(text='Password')
        txtPass = TextInput(text='Password', multiline=False)

        btn = Button(text='Login', size=(100, 50))

        layout.add_widget(lblUser)
        layout.add_widget(txtUser)
        layout.add_widget(lblPass)
        layout.add_widget(txtPass)
        layout.add_widget(btn)
        return layout

Login().run()
