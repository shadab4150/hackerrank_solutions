import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


pop_M=[81,11,24,32,16,48,15,51,63,9,70]
np_pop_M=np.array(pop_M)

movie_data=pd.read_csv('F:\CSV files\MOVIE_score_comparison.csv',index_col=0)
RT=movie_data.RT_norm
RT_U=movie_data.RT_user_norm
MT=movie_data.Metacritic_norm
MT_U=movie_data.Metacritic_user_nom
IMDb=movie_data.IMDB_norm
FDS=movie_data.Fandango_Stars
FDRV=movie_data.Fandango_Ratingvalue

plt.title('Comparison on ratings of metacritic, RottenTomatoes,IMDB,Fandango')
plt.xlabel('stars')
plt.xticks([0,1,2,3,4,5],['0','*','**','***','****','*****'])

plt.hist(FDS,bins=8,histtype='stepfilled',color='red',alpha=0.8,label='Fandango stars')
plt.hist(IMDb,bins=8,histtype='stepfilled',color='yellow',alpha=0.75,label='IMDB')
plt.hist(RT,bins=8,histtype='stepfilled',color='green',alpha=0.7,label='RottenTomatoes')
plt.hist(RT_U,bins=8,histtype='stepfilled',color='orange',alpha=0.4,label='RottenTomatoes Users')
plt.hist(MT,bins=8,histtype='stepfilled',color='indigo',alpha=0.6,label='Metacritic')
plt.hist(MT_U,bins=8,histtype='stepfilled',color='pink',alpha=0.5,label='Metacritic Users')

plt.legend()
plt.show()
plt.clf()

plt.title('Comparison on ratings of metacritic, RottenTomatoes,IMDB,Fandango')
plt.xlabel('stars')
plt.xticks([0,1,2,3,4,5],['0','*','**','***','****','*****'])

plt.hist(FDS,bins=8,histtype='stepfilled',color='red',alpha=0.8,label='Fandango stars')

plt.show()
plt.clf()

sns.kdeplot(IMDb,shade=True,color='r')
sns.kdeplot(FDS,shade=True,color='g')
sns.kdeplot(RT,shade=True,color='yellow')
sns.kdeplot(RT_U,shade=True,color='black')
sns.kdeplot(MT,shade=True,color='orange')
sns.kdeplot(MT_U,shade=True,color='indigo')

plt.show()
plt.clf()

sns.kdeplot(FDS,shade=True,color='g',label='fandango prsented value')
sns.kdeplot(FDRV,shade=True,color='b',label='actual value')

plt.show()
plt.clf()

sns.kdeplot(FDS,shade=True,color='g')
plt.show()
plt.clf()

plt.title('Comparison on ratings of Fandango')
plt.xlabel('stars')
plt.xticks([0,1,2,3,4,5],['0','*','**','***','****','*****'])
plt.hist(FDS,bins=8,histtype='stepfilled',color='red',alpha=0.75,label='Fandango present stars')
plt.hist(FDRV,bins=8,histtype='stepfilled',color='skyblue',alpha=0.75,label='Actual rating value')

plt.legend()
plt.show()
plt.clf()                    
                       
                      
