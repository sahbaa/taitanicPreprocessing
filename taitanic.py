from ydata_profiling import ProfileReport
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('preprocessingOnkaggle\imdb\\train.csv')
print(df.describe())
print(df.info())


report=ProfileReport(df,dark_mode=True)
report.to_file('preprocessingOnkaggle\imdb\\result.html')












































































































# pro_report=ProfileReport(df)
# pro_report.to_file('preprocessingOnkaggle\imdb\\result.html')


# colors=['#1211fe','#f043ee','#fe1100']
# plt.subplot(1,2,1)
# sns.boxenplot(x=df['Sex'],y=df['Age'])
# plt.subplot(1,2,2)
# df['Age']=df['Age'].fillna(np.mean(df['Age']))
# plt.boxplot([df[df['Sex']=='male']['Age'],df[df['Sex']=='female']['Age']],vert=True)
# plt.show()
# print(df[df['Sex']=='male']['Age'])


# plt.subplots(1,7,width_ratios=[0.1,0.2,0.4,0.2,0.1,0.04,0.06])
# plt.subplot(1,6,1)
# sns.countplot(x='Sex',data=df)
# plt.subplot(1,6,2)
# sns.countplot(x='Survived',hue='Sex',data=df)
# plt.subplot(1,6,3)
# df['Survived'].value_counts().plot(kind='box')
# plt.subplot(1,6,4)
# sns.boxplot(df['Age'])
# plt.subplot(1,6,5)
# plt.boxplot(df['Age'])
# plt.subplot(1,6,6)

# sns.displot(df['Age'])
# plt.show()
# sns.countplot(df['Age'])
# plt.show()
# plt.hist(df['Age'])
# plt.show()