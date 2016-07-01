import csv

import numpy as np
import matplotlib.pyplot as plt
from pylab import show
from numpy import recfromcsv

price_demand = []
# price_demand = recfromcsv('price_demand.csv', delimiter=',', dtype=(int, float, int))

with open('price_demand.csv','r') as dest_f:
    data_iter = csv.reader(dest_f,
                           delimiter=",",
                           quotechar='"')
    price_demand = [data for data in data_iter]

for p in price_demand:
    print(p)

#    price_demand = np.asarray(price_demand, dtype=(int, float, int))

for p in price_demand:
    print(p)

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(price_demand, )

show()

