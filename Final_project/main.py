import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.filechooser import FileChooserController
kivy.require("2.0.0")

#Odczyt pliku layout opisującego wygląd aplikacji
#Builder.load_file('Porosity.kv')

class PorosityLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            pass

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # self.add_widget(Label(text="Wczytaj dane"))
        # self.LoadButton = Button(text="Load Data from csv")
        # self.LoadButton.bind(on_click=self.LoadData)
        # self.add_widget(self.LoadButton)

    #def LoadData(self, instance):

class Porosity(App):
    def build(self):
        return PorosityLayout()



if __name__ == '__main__':
    Porosity().run()
