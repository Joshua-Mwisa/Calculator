from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class Josh(GridLayout):
    Window.size = 360, 500

    def calculated(self, calculate):
        if calculate:
            try:
                self.display.text = str(eval(calculate))
            except Exception:
                self.display.text = 'Error'
                pass


class Calc (App):
    def build(self):
        return Josh()


Calc().run()
