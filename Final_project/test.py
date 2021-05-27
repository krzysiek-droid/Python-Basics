import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sorting_algorithms_database as sad
import time
from plyer import filechooser


# set mean and sd
# mu, sigma = 100, 15
#
# # create distribution of data
# x = mu + sigma*np.random.randn(10000)
#
# # build histogram
# n, bins, patches = plt.hist(x, 50)
# plt.show()

class Histogram_screen:
    def __init__(self, algorithm):
        super(Histogram_screen, self).__init__()
        # filepath to .csv file with data to be plotted
        # self.file = filepath
        # name of algorithm used for sorting of data
        self.selected_algorithm = algorithm
        self.sorting_time = time.time()

    def sort_values(self, values):
        sorted = []

        # removing repeated values
        values = set(values)
        values = list(values)

        if self.selected_algorithm == "bubble_sort":
            t0 = time.time()
            sorted = sad.bubble_sort(values)
        elif self.selected_algorithm == "merge_sort":
            t0 = time.time()
            sorted = sad.merge_sort(values)
        elif self.selected_algorithm == "insertion_sort":
            t0 = time.time()
            sorted = sad.insertion_sort(values)
        else:
            t0 = time.time()
            sorted = sad.selection_sort(values)

        t1 = time.time()
        sorting_time = t1 - t0
        self.sorting_time = round(sorting_time, 5)

        return sorted


fopen = pd.read_csv('H11_PB1.1.csv', sep=";")
circ_values = fopen.get("Circ.")

print(type(circ_values))

circ_values = set(circ_values)
circ_values = list(circ_values)

histogram = Histogram_screen("merge_sort")

print(histogram.sort_values(circ_values))
print(histogram.sorting_time)
