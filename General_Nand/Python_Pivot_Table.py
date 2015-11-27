__author__ = '20093'
import pandas as pd
import numpy as np
import wx
# import seaborn as sns



file_path='X:\personals\Jinqiang\MAPS_Data\S3E_16D\PB-outliers\MAPS_Nov25_10h57m05s(BitFlips4KHistogramByChip).csv'
Histo_4K = pd.read_csv(file_path)

import matplotlib.pyplot as plt
# sns.set()  # use seaborn styles
Histo_4K.pivot_table('Count', index=['BitFlip'], columns=['Lot','Level'], aggfunc='sum').plot()
plt.ylabel('total Histo_4K per year')
plt.yscale('log')
plt.show()