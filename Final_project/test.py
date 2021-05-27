import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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




# path = filechooser.open_file(title="Pick a CSV file..",
#                              filters=[("Comma-separated Values", "*.csv")])
# print(path)

fopen = pd.read_csv('H11_PB1.1.csv', sep=";")
circ_values = fopen.get("Circ.")
circ_values = list(circ_values)
print(circ_values)
