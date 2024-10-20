# Loading in required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nobel = pd.read_csv('data/nobel.csv')
print(nobel.head())

# Q1 What is the most commonly awarded gender and birth country?
# Finding the top gender and country using mode
top_gender = nobel['sex'].mode()
print("\n The gender with the most awards is:", top_gender)


top_country = nobel['birth_country'].mode()
print("\n The country with the most awards is:", top_country)


# Q2 Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
nobel['usa_winners'] = nobel['birth_country'] == 'United States of America'
nobel['decades'] = (np.floor(nobel['year']/10) *10).astype(int)
avg_usa_winners = nobel.groupby('decades', as_index=False)['usa_winners'].mean()

max_decade_usa = avg_usa_winners[avg_usa_winners['usa_winners'] == avg_usa_winners['usa_winners'].max()]['decades'].values
print("\n The decade with the highest ratio of US winners: ", max_decade_usa)

sns.relplot(x='decades', y='usa_winners', data=avg_usa_winners, kind='line')

# Q3 Which decade and Nobel Prize category combination had the highest proportion of female laureates?
nobel['female_winners'] = nobel['sex'] == 'Female'
avg_female_winners = nobel.groupby(['decades','category'], as_index=False)['female_winners'].mean()

top_female_decade = avg_female_winners[avg_female_winners['female_winners'] == avg_female_winners['female_winners'].max()][['decades', 'category']]
print("\n Decade with most female winners: ", top_female_decade)

max_female_dict = {top_female_decade['decades'].values: top_female_decade['category'].values} 
print("\n Decade with most female winners and category of award: ", max_female_dict)

sns.relplot(x='decades', y='female_winners', hue='category', data=avg_female_winners, kind='line')

# Q4 Who was the first woman to receive a Nobel Prize, and in what category?
first_nobel_female = nobel[nobel['female_winners']]
first = first_nobel_female[first_nobel_female['year'] == first_nobel_female['year'].min()]
first_woman_name = first['full_name'].values
first_woman_category = first['category'].values
print("\n The first woman to receive a Nobel Prize is: ", first_woman_name,first_woman_category)

# Q5 Which individuals or organization have won more than one Nobel Prize throughout the years?
number = nobel['full_name'].value_counts()
returners = number[number > 1].index
repeat_list = list(returners)
print("\n People who got more than one Nobel Prizes: ", repeat_list)
