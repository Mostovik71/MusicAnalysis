import pandas as pd
from tabulate import tabulate
import random
import matplotlib.pyplot as plt
import pylab
#import chart_studio.plotly as py
#import plotly.graph_objs as go
import seaborn as sns

musicdf=pd.read_csv('music')
musicdf.drop(['Unnamed: 0'], axis = 1,inplace=True)
musicdf.drop(['Unnamed: 0.1'], axis = 1,inplace=True)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#cols = music.columns.tolist()
#musiclowvalence=music[music['valence']<0.5] - вывод песен,в которых параметр valence имеет значение <0.5
#print(tabulate(musicdf.sample(10),headers='keys',tablefmt='psql'))# - вывод всего плейлиста
#print(music.iloc[0])-данные о конкретной песне
#print(cols)


matrix = musicdf.pivot_table(
    index='user',
     columns='track_name',
     values='user_score'
)
#print(tabulate(matrix,headers='keys',tablefmt='psql'))


def get_similar_tracks(track_name, n_ratings_filter=0, n_recommendations=5):
    similar = matrix.corrwith(matrix[track_name])#Находит корелляцию между данным треком и остальными

    corr_similar = pd.DataFrame(similar, columns=['correlation'])#Превращение серии в датафрейм
    corr_similar.dropna(inplace=True)#Удаление нанов(треков для которых невозможно вычислить корелляцию)


    orig = musicdf.copy()

    corr_with_track = pd.merge(
        left=corr_similar,
        right=orig,
        on='track_name')[['track_name', 'correlation', 'user_score']].drop_duplicates(subset=['track_name']).reset_index(drop=True)
    #print(tabulate(corr_with_track, headers='keys', tablefmt='psql'))
    result = corr_with_track[corr_with_track['user_score'] > n_ratings_filter].sort_values(by='correlation',
                                                                                           ascending=False)

    return result.head(n_recommendations)
df=get_similar_tracks('Iris')
print(tabulate(df,headers='keys',tablefmt='psql'))

'''
sns.kdeplot(music['duration_min'], shade=True, cut=0)
plt.xlabel("Длительность (в минутах)") # подпись оси x
plt.ylabel("Распределение (в долях)") # подпись оси y
plt.title("Распределенность аудиотеки по длительности") # подпись заголовка
plt.show()
'''


'''
# Строим 9 графиков разом
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 15))
fig.subplots_adjust(hspace=0.4, wspace=0.7)
pylab.subplot(2, 3, 1)
ac = sns.kdeplot(music['danceability'], shade=False, color="green", cut=0)

pylab.subplot(2, 3, 2)
ac = sns.kdeplot(music['energy'], shade=False, color="green", cut=0)

pylab.subplot(2, 3, 3)
ac = sns.kdeplot(music['valence'], shade=False, color="green", cut=0)

pylab.subplot(2, 3, 4)
ac = sns.kdeplot(music['popularity'], shade=False, color="green", cut=0)

pylab.subplot(2, 3, 5)
ac = sns.kdeplot(music['duration_min'], shade=False, color="green", cut=0)


plt.show()

'''
#sns.jointplot(x='duration_min',y='popularity',data=music,kind='scatter') #График "типа зависимости"
#sns.pairplot(music)#ВСЕ ЗАВИСИМОСТИ



#plt.show()

