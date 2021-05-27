import kivy
import sorting_algorithms_database as sad
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
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
        # initialized filechooser of Windows type (thanks to plyer lib.)
        path = filechooser.open_file(title="Pick a .csv file",
                                     filters=[("Comma-separated values", "*.csv")])
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
    chosen_algorithm = ''
    pass


def load_values_from_csv(filepath):
    fopen = pd.read_csv(filepath, sep=",")
    values = fopen.get("Circ.")
    values = list(values)

    return values


class Histogram_screen(Screen):
    def __init__(self):
        super(Histogram_screen, self).__init__()
        self.sorting_time = None
        self.data = None

    def sort_values(self, filepath, selected_algorithm):

        values = load_values_from_csv(filepath)
        print(values)

        if selected_algorithm == "bubble_sort":
            t0 = time.time()
            sorted_values = sad.bubble_sort(values)
        elif selected_algorithm == "merge_sort":
            t0 = time.time()
            sorted_values = sad.merge_sort(values)
        elif selected_algorithm == "insertion_sort":
            t0 = time.time()
            sorted_values = sad.insertion_sort(values)
        else:
            t0 = time.time()
            sorted_values = sad.selection_sort(values)

        t1 = time.time()
        sorting_time = t1 - t0
        self.sorting_time = round(sorting_time, 5)
        self.data = sorted_values


    # App logic
class PorosityApp(App):
    def build(self):
        screen_manager = WindowManager()

        screen_manager.add_widget(screen=Welcome_screen(name='welcome_screen'))

        algorithm = sorting_algorithms()
        screen_manager.add_widget(screen=algorithm)

        histogram = Histogram_screen()
        screen_manager.add_widget(screen=histogram)

        return screen_manager


# main
if __name__ == '__main__':
    PorosityApp().run()
