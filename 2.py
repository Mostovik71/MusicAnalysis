import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

import chart_studio.plotly as py
#import plotly.graph_objs as go
import seaborn as sns
music=pd.read_csv('mybest2020')
#musiclowvalence=music[music['valence']<0.5] - вывод песен,в которых параметр valence имеет значение <0.5
print(tabulate(music,headers='keys',tablefmt='psql'))# - вывод всего плейлиста
#print(music.iloc[0])-данные о конкретной песне



#f, axes = plt.subplots(1, 8, sharey=True, figsize=(15, 4))
'''
fig = plt.figure(figsize=(11,9))
ax_1 = fig.add_subplot(4, 4, 1)
ax_2 = fig.add_subplot(4, 4, 2)
ax_3 = fig.add_subplot(4, 4, 3)
ax_4 = fig.add_subplot(4, 4, 4)
ax_5 = fig.add_subplot(4, 4, 9)
ax_6 = fig.add_subplot(4, 4, 10)
ax_7 = fig.add_subplot(4, 4, 11)
ax_8 = fig.add_subplot(4, 4, 12)
sns.distplot(music['valence'], ax=ax_1)
sns.distplot(music['danceability'], ax=ax_2)
sns.distplot(music['loudness'], ax=ax_3)
sns.distplot(music['energy'], ax=ax_4)
sns.distplot(music['liveness'], ax=ax_5)
sns.distplot(music['speechiness'], ax=ax_6)
sns.distplot(music['instrumentalness'], ax=ax_7)
sns.distplot(music['tempo'], ax=ax_8)
plt.legend()
plt.show()
'''

