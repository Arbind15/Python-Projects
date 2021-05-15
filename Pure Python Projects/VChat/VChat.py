from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout

class VChat(App):
    def build(self):
        f=FloatLayout()
        s=Scatter()
        l=Label(text="Arbind Mehta",font_size=100)
        f.add_widget(s)
        s.add_widget(l)
        return f
