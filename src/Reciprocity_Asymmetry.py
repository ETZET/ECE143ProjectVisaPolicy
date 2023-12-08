# %% [markdown]
# ## Reciprocity and Asymmetry
# Is visa-free access always reciprocated between countries, or are there instances of one-way visa-free access?
# 
# Since visa free access can be either limited by a certain number of days or unlimited, we make a sorted list where the value of a given two countries is the difference in days of visa-free travel, then analyze the resulting list where one end is most reciprocated and other end is most asymmetrical.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
data = pd.read_csv('passport-index-tidy-iso2.csv')
data.head()


# %%
#convert dataframe to dictionary for quick lookup
lookup_requirement = {}
for index, row in data.iterrows():
    a = row['Passport']
    b = row['Destination']
    lookup_requirement[(a,b)] = row['Requirement']

#add columns for flipped requirement
#remove used values at the same time
print(data.shape)
for index, row in data.iterrows():
    a = row['Passport']
    b = row['Destination']
    if a == b:
        data.drop(index, inplace=True)
        continue
    visa2 = lookup_requirement[(b,a)]
    if visa2:
        data.at[index, 'Requirement 2'] = visa2
        lookup_requirement[(a,b)] = None
    else:
        data.drop(index, inplace=True)

print(data.shape)

print(data.head())

# %%
#add column specifying days without visa allowed
def days_without_visa(column):
    def days_without_visa(row):
        label = row[column] 
        #requires a visa for entry, automatically 0 days without visa
        if label == 'e-visa' or label == 'visa required' or label == 'visa on arrival':
            return 0
        #for the sake of pointing out asymmetry, we set this to a negative value
        #since this is clearly worse than needing a visa
        if label == 'no admission':
            return -1
        #days of travel without visa is not listed, so we give it an arbitray large value > 360
        #(360 days is maximum travel without visa worldwide when it is listed)
        if label == 'visa free':
            return 365
        #number of days of travel without visa
        return float(label)
    return days_without_visa

data['Days Without Visa'] = data.apply(days_without_visa('Requirement'), axis=1)
data['Days Without Visa 2'] = data.apply(days_without_visa('Requirement 2'), axis=1)
data.head()

# %%
data['Asymmetry'] = abs(data['Days Without Visa'] - data['Days Without Visa 2'])
data = data.sort_values(by=['Asymmetry'], ascending=False)
data.head()

# %% [markdown]
# ## Asymmetry
# Here we see that there are just two instances of maximum possible Asymmetry, no admission vs visa free.
# 
# Between The State of Palestine (PS) and The Syrian Arab Republic (SY)
# SY does not allow anyone with PS passport, while PS does not require visa from SY.  
# 
# Between Kyrgyzstan (KG) and Tajikistan (TJ)
# KG does not allow anyone with TJ passport, while TJ does not require visa from KG.  

# %%
data['Asymmetry'].value_counts()

# %%
reciprocity = data['Asymmetry'].value_counts()
reciprocity.sort_index(inplace=True)
data = data.sort_values(by=['Asymmetry'], ascending=True)
barplot = data.Asymmetry.value_counts()[data.Asymmetry.unique()].plot.bar(title='Asymmetry Between Two Countries',xlabel='Difference in Days Allowed without Visa', ylabel='Count', figsize=(10,5))

# %% [markdown]
# ## Reciprocity
# We see that there are 14222 cases where visa requirements match out of 19702 different connections, meaning that the world is 72% fully reciprocated.
# 
# We also see that the most common asymmetry is at 90 days without Visa and 30 days

# %% [markdown]
# 


