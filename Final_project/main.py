import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import  BoxLayout

# requirement for kivy version
kivy.require("2.0.0")

# referance to the application design file (.kv)
# Builder.load_file('Porosity.kv')

# Prime window character
Window.size = (750, 500)


# Screen with algorythm chose
class Select_alg(Screen):
    def __init__(self):
        super(Select_alg, self).__init__()
        self.filepath = ' '



class WindowManager(ScreenManager):
    pass


# screen with filechooser
class Filechooser(Screen):
    def __init__(self):
        super(Filechooser, self).__init__()
        self.filepath = " "
        self.is_selected = False

    def select(self, *args):
        try:
            self.filepath = self.ids.filename.text = args[1][0]
        except:
            pass

    def save_path(self):
        try:
            self.is_selected = True
            self.filepath = self.ids.filename.text
            print(self.filepath)
        except:
            pass


# first screen poping up when initilized
class First_window(Screen):
    pass

class PorosityApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(First_window(name='first_window'))

        file_chooser = Filechooser()
        screen_manager.add_widget(file_chooser)
        filepath = file_chooser.filepath

        algorithm = Select_alg()
        # algorithm.filepath = filepath
        screen_manager.add_widget(algorithm)

        return screen_manager


if __name__ == '__main__':
    PorosityApp().run()
