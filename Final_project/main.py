import kivy
import sorting_algorithms_database as sab
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import filechooser

# requirement for kivy version
kivy.require("2.0.0")

# Prime window character
Window.size = (750, 500)


# first screen popping up when app initialized
class Welcome_screen(Screen):
    def open_filechooser(self):
        path = filechooser.open_file(title="Pick a .csv file",
                                     filtes=[("Comma-separated values", "*.csv")])
        return path[0]

# Algorithm choice screen
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
    choosen_algorithm = ''
    pass


class Histogram_screen(Screen):
    def __init__(self, filepath, algorithm):
        super(Histogram_screen, self).__init__()
        self.file = filepath
        self.selected_algorithm = algorithm

    def plot_histogram(self):
        pass


# App logic
class PorosityApp(App):
    def build(self):
        screen_manager = WindowManager()

        screen_manager.add_widget(Welcome_screen(name='welcome_screen'))

        algorithm = sorting_algorithms()
        screen_manager.add_widget(algorithm)

        return screen_manager


# main
if __name__ == '__main__':
    PorosityApp().run()
