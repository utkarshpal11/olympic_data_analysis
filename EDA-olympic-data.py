# in this file we analyse the 120 years of olympic data using python numpy and 
# pandas and other data manipulating libraries
# lets start

import numpy as an
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# set the features for showing data on console
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', None)

data_athlete = pd.read_csv('athlete_events.csv')
noc_data = pd.read_csv('noc_regions.csv')
'''
print(os.listdir())
# print basic info about the datasets
print(data_athlete)
print(data_athlete.info())
print(data_athlete.describe())

print(noc_data)
print(noc_data.info())
print(noc_data.describe())
'''
# merge the two datasets
merged = pd.merge(data_athlete, noc_data, how='left', on='NOC')     # merge with reference to NOC
print(merged)
print(merged.info())
print(merged.describe())

# distribution of the age of gold medals
goldMedals = merged[merged['Medal'] == 'Gold']
print(goldMedals)
print('nan values in goldMedals -->>\n', goldMedals['Age'].isnull().sum())

# print null values in all columns
print(merged.isnull().sum())

# to check NaN values in Age
print(merged['Age'].isnull().sum())

merged.drop(['notes'], inplace=True, axis=1)
print(merged)

# fillna values in Age by their mean groupby country
goldMedals['Age'].fillna(goldMedals.groupby('Sex')['Age'].transform('mean'), inplace=True)
goldMedals.round({'Age':1})
print(goldMedals['Age'].isnull().sum())
#
# # catplot
# plt.figure(figsize=(20, 15))
# plt.tight_layout()
# sns.countplot(goldMedals['Age'])
# plt.show()

# number of people have gold medals are older than 50
print((goldMedals['Age'] > 50).value_counts())
'''
# new dataframe(series) for sports nand age > 50
extreme = goldMedals['Sport'][goldMedals['Age'] > 50]       # to get pandas series of sports for age > 50
print(extreme)
print(type(extreme))

plt.figure(figsize=(10, 8))
sns.countplot(extreme)
plt.show()
womenSeries = pd.Series(data=(merged['Sex'] == 'F'))
print(womenSeries)
womenMedals = merged[merged['Sex'] == 'F']
print(womenMedals)

plt.figure(figsize=(20, 10))
sns.countplot(x='Year', data=womenMedals)
plt.show()

#top 5 gold medalist countries
most_medals = goldMedals.region.value_counts().sort_values(ascending=False).reset_index(name='Medals').head(5)
print(most_medals)
# print(goldMedals.region.value_counts().reset_index(name='Medal').head(5))
sns.catplot(x='index', y='Medals', data=most_medals, height=8, kind='bar', palette='muted')
plt.show()
'''
# discipline with the greatest number of gold medals

# goldmedals only for usa
usa_goldMedals = goldMedals[goldMedals['NOC'] == 'USA']
print(usa_goldMedals)

# medals per person for USA
usa_goldMedals = usa_goldMedals['Event'].value_counts().sort_values(ascending=False).reset_index(name='Medals').head(10)
print(usa_goldMedals)

# data about gold medals in basketball
usa_goldMedals_bsktbl = goldMedals[(goldMedals['Sport'] == 'Basketball') & (goldMedals['Sex'] == 'M')].sort_values(['Year'])
print(usa_goldMedals_bsktbl)

# to check who win the first medal for usa in every olympic for basketball
usa_goldMedals_bsktbl = usa_goldMedals_bsktbl.groupby(['Year']).first()
print(usa_goldMedals_bsktbl['ID'].count())
print(usa_goldMedals_bsktbl)

# to check the mean and median of height and weight of gold medal winners
# ignoring null values
goldMedals = goldMedals[(goldMedals['Height'].notnull() & goldMedals['Weight'].notnull())]
goldMedals.info()

# sns.scatterplot(x='Height', data=goldMedals, y='Weight')
# plt.show()

# weight above 160 kg
print(goldMedals[goldMedals['Weight'] > 160 ].count())

# How the number of athletes/countries varied along time ?
# How the proportion of Men/Women varied with time ?
# How about mean age, weight and height along time ?

# men in olympics
men = merged[(merged['Sex'] == 'M') & (merged['Season'] == 'Summer')]
women = merged[(merged['Sex'] == 'F') & (merged['Season'] == 'Summer')]

print(men)
print(women)

# sns.countplot(x='Year', data=men)
# plt.title('Men in Olympics')
# plt.show()
# sns.countplot(x='Year', data=women)
# plt.title('Women in Olympics')
# plt.show()
#
# # variation of age for men in all olympics
# sns.boxplot('Year', 'Age', data=men)
# plt.show()
# sns.boxplot('Year', 'Age', data=women)
# plt.show()

# variation in weight for men and women
# sns.boxplot('Year', 'Weight', data=men)
# plt.show()
# sns.boxplot('Year', 'Weight', data=women)
# plt.show()

# variation in age for italy men
itmen = men[men['region'] == 'Italy']
print(itmen.info())

# italy men data
# sns.lineplot(x='Year', data=itmen, y='Age')
# plt.show()


# Variation of height/weight along time for particular disciplines(sport)

# gymnastic
print(men['Sport'].unique())

men_in_gym = men[men['Sport'] == 'Gymnastics']
sns.boxplot('Year', 'Age', data=men_in_gym)
plt.title('Age')
plt.show()
sns.boxplot('Year', 'Weight', data=men_in_gym)
plt.title('Weight')
plt.show()
sns.boxplot('Year', 'Height', data=men_in_gym)
plt.title('Height')
plt.show()