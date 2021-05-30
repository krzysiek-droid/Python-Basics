import kivy
from kivy.config import value

import sorting_algorithms_database as sad
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import filechooser
import os.path

# requirement for kivy version
kivy.require("2.0.0")

# Prime window character
Window.size = (750, 500)

def path_normalization(path):
    separated_path = path.split("'\'")
    return separated_path


# first screen popping up when app initialized
class Welcome_screen(Screen):
    def open_filechooser(self):
        # initialized filechooser of Windows type (thanks to plyer lib.)
        path = filechooser.open_file(title="Pick a .csv file",
                                     filters=[("Comma-separated values", "*.csv")])
        #file_opened = pd.read_csv(path[0], sep=";")

        return path


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
    sorting_time = ''
    data_array = None
    pass


def load_values_from_csv(filepath, column_name):
    file_opened = pd.read_csv(filepath[0], sep=";")  # check if file is seperated by ";"
    values = file_opened.get(column_name)
    print(values)
    values = list(values)
    try:
        if type(values) == list:
            return values
        else:
            raise ValueError
    except ValueError:
        print(f"Imported Values are not of list type, {type(values)}"
              f"Check if a proper separator is given to the method load_values_from_csv.")


class Histogram_screen(Screen):

    def __init__(self):
        super().__init__()
        self.sorting_time = value
        self.sorted = value


    def sort_values(self, filepath, selected_algorithm):

        values = load_values_from_csv(filepath, "Circ.")

        # Data preparation - removing repeated values (for histogram purposes)
        values = set(values)
        values = list(values)

        if selected_algorithm == "bubble_sort":
            t0 = time.time()
            print(f"t0 = {t0}")
            sorted_values = sad.bubble_sort(values)
        elif selected_algorithm == "merge_sort":
            t0 = time.time()
            print(f"t0 = {t0}")
            sorted_values = sad.merge_sort(values)
        elif selected_algorithm == "insertion_sort":
            t0 = time.time()
            print(f"t0 = {t0}")
            sorted_values = sad.insertion_sort(values)
        else:
            t0 = time.time()
            print(f"t0 = {t0}")
            sorted_values = sad.selection_sort(values)

        t1 = time.time()
        print(f"t1 = {t1}")
        sorting_time = t1 - t0
        self.sorting_time = round(sorting_time, 5)
        self.sorted = sorted_values

        return self.sorting_time

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
