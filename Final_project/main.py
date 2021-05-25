import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.event import EventDispatcher

# requirement for kivy version
kivy.require("2.0.0")

# referance to the application design file (.kv)
# Builder.load_file('Porosity.kv')

# Prime window character
Window.size = (750, 500)


# screen with filechooser
class Filechooser(Screen):
    def __init__(self):
        super().__init__()
        self.file_path = ' filechooser_path '

    def select(self, *args):
        try:
            self.ids.filename.text = args[1][0]
        except:
            pass

    def save_path(self):
        self.file_path = self.ids.filename.text


# Screen with algorithm chose
class sorting_algorithms(Screen):
    def __init__(self, ):
        super().__init__()
        self.filepath = ' initialized path '


    def set_filepath(self, value):
        self.filepath = value
        self.ids.filepath.text = value

    def show_path(self):
        self.ids.filepath.text = "sorting_algorithm"


class WindowManager(ScreenManager):
    filepath = ''
    pass


# first screen poping up when initilized
class First_window(Screen):
    pass


class PorosityApp(App):
    def build(self):
        screen_manager = WindowManager()
        screen_manager.add_widget(First_window(name='first_window'))

        file_chooser = Filechooser()
        screen_manager.add_widget(file_chooser)

        algorithm = sorting_algorithms()
        screen_manager.add_widget(algorithm)

        return screen_manager


if __name__ == '__main__':
    PorosityApp().run()
