import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class Manager(ScreenManager):
    pass
class Menu(Screen):
    pass
class Game(Screen):
    pass
class GameOver(Screen):
    pass
class Application(App):
    def build(self):
        return Manager()
Application().run()
