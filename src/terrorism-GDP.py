#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import seaborn as sns
import dateutil 


# In[2]:


data = np.genfromtxt("Terrorism-GDP data.csv", delimiter=',', dtype=str, skip_header=1)


# In[3]:


#OUTGOING


# In[4]:


country_out_2022 = defaultdict(int)

passport_data_2022 = np.genfromtxt('passport-index-matrix-iso3-2022.csv', delimiter=',', dtype=str, skip_header=1)

for i in passport_data_2022:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_out_2022[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_out_2022[coun] += 1
            
country_visa_outgoing_2022 = dict(sorted(country_out_2022.items(), key=lambda item: item[1], reverse= True))


# In[5]:


country_out_2021 = defaultdict(int)

passport_data_2021 = np.genfromtxt('passport-index-matrix-iso3-2021.csv', delimiter=',', dtype=str, skip_header=1)

for i in passport_data_2021:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_out_2021[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_out_2021[coun] += 1
            
country_visa_outgoing_2021 = dict(sorted(country_out_2021.items(), key=lambda item: item[1], reverse= True))


# In[6]:


country_out_2020 = defaultdict(int)

passport_data_2020 = np.genfromtxt('passport-index-matrix-iso3-2020.csv', delimiter=',', dtype=str, skip_header=1)

for i in passport_data_2020:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_out_2020[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_out_2020[coun] += 1
            
country_visa_outgoing_2020 = dict(sorted(country_out_2020.items(), key=lambda item: item[1], reverse= True))


# In[ ]:





# In[7]:


#INCOMING


# In[8]:


df_2022 = np.genfromtxt('passport-index-matrix-iso3-transposed-2022.csv', delimiter=',', dtype=str, skip_header=1)


# In[9]:


df_2021 = np.genfromtxt('passport-index-matrix-iso3-transposed-2021.csv', delimiter=',', dtype=str, skip_header=1)


# In[10]:


df_2020 = np.genfromtxt('passport-index-matrix-iso3-transposed-2020.csv', delimiter=',', dtype=str, skip_header=1)


# In[11]:


country_in_2022 = defaultdict(int)
country_in_2021 = defaultdict(int)
country_in_2020 = defaultdict(int)


# In[12]:


for i in df_2022:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_in_2022[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_in_2022[coun] += 1
            
country_visa_incoming_2022 = dict(sorted(country_in_2022.items(), key=lambda item: item[1], reverse= True))


# In[13]:


for i in df_2021:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_in_2021[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_in_2021[coun] += 1
            
country_visa_incoming_2021 = dict(sorted(country_in_2021.items(), key=lambda item: item[1], reverse= True))


# In[14]:


for i in df_2020:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_in_2020[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_in_2020[coun] += 1
            
country_visa_incoming_2020 = dict(sorted(country_in_2020.items(), key=lambda item: item[1], reverse= True))


# In[15]:


#country_in["IND"]


# In[16]:


scores_2022 = defaultdict(int)
scores_2021 = defaultdict(int)
scores_2020 = defaultdict(int)


# In[17]:


for i in data:
    #print(i)
    coun = i[1]
    scores_2022[coun] = i[12]
    scores_2021[coun] = i[11]
    scores_2020[coun] = i[10]
    
    
scores_country_2022 = dict(sorted(scores_2022.items(), key=lambda item: item[1], reverse= True))
scores_country_2021 = dict(sorted(scores_2021.items(), key=lambda item: item[1], reverse= True))
scores_country_2020 = dict(sorted(scores_2020.items(), key=lambda item: item[1], reverse= True))


# In[18]:


#scores_2022


# In[19]:


GDP_2022 = defaultdict(int)
GDP_2021 = defaultdict(int)
GDP_2020 = defaultdict(int)


# In[20]:


for i in data:
    #print(i)
    coun = i[1]
    GDP_2022[coun] = i[23]
    GDP_2021[coun] = i[22]
    GDP_2020[coun] = i[21]
   
    
GDP_country_2022 = dict(sorted(GDP_2022.items(), key=lambda item: item[1], reverse= True))
GDP_country_2021 = dict(sorted(GDP_2021.items(), key=lambda item: item[1], reverse= True))
GDP_country_2020 = dict(sorted(GDP_2020.items(), key=lambda item: item[1], reverse= True))


# In[23]:


# Create DataFrames from dictionaries
incoming_df_2022 = pd.DataFrame(list(country_visa_incoming_2022.items()), columns=['Country', 'Incoming'])
outgoing_df_2022 = pd.DataFrame(list(country_visa_outgoing_2022.items()), columns=['Country', 'Outgoing'])
gdp_df_2022 = pd.DataFrame(list(GDP_2022.items()), columns=['Country', '2022 GDP'])
scores_df_2022 = pd.DataFrame(list(scores_2022.items()), columns=['Country', '2022 Terrorism Score'])

incoming_df_2021 = pd.DataFrame(list(country_visa_incoming_2021.items()), columns=['Country', 'Incoming'])
outgoing_df_2021 = pd.DataFrame(list(country_visa_outgoing_2021.items()), columns=['Country', 'Outgoing'])
gdp_df_2021 = pd.DataFrame(list(GDP_2021.items()), columns=['Country', '2021 GDP'])
scores_df_2021 = pd.DataFrame(list(scores_2021.items()), columns=['Country', '2021 Terrorism Score'])

incoming_df_2020 = pd.DataFrame(list(country_visa_incoming_2020.items()), columns=['Country', 'Incoming'])
outgoing_df_2020 = pd.DataFrame(list(country_visa_outgoing_2020.items()), columns=['Country', 'Outgoing'])
gdp_df_2020 = pd.DataFrame(list(GDP_2020.items()), columns=['Country', '2020 GDP'])
scores_df_2020 = pd.DataFrame(list(scores_2020.items()), columns=['Country', '2020 Terrorism Score'])


# In[24]:


# Merge the DataFrames on 'Country'
merged_df_2022 = pd.merge(incoming_df_2022, outgoing_df_2022, on='Country')
merged_df_2022 = pd.merge(merged_df_2022, gdp_df_2022, on='Country')
merged_df_2022 = pd.merge(merged_df_2022, scores_df_2022, on='Country')


merged_df_2021 = pd.merge(incoming_df_2021, outgoing_df_2021, on='Country')
merged_df_2021 = pd.merge(merged_df_2021, gdp_df_2021, on='Country')
merged_df_2021 = pd.merge(merged_df_2021, scores_df_2021, on='Country')


merged_df_2020 = pd.merge(incoming_df_2020, outgoing_df_2020, on='Country')
merged_df_2020 = pd.merge(merged_df_2020, gdp_df_2020, on='Country')
merged_df_2020 = pd.merge(merged_df_2020, scores_df_2020, on='Country')


# In[25]:


merged_df_2022['2022 GDP'] = pd.to_numeric(merged_df_2022['2022 GDP'].str.replace(',', ''), errors='coerce')
merged_df_2022['2022 Terrorism Score'] = pd.to_numeric(merged_df_2022['2022 Terrorism Score'].str.replace(',', ''), errors='coerce')

merged_df_2021['2021 GDP'] = pd.to_numeric(merged_df_2021['2021 GDP'].str.replace(',', ''), errors='coerce')
merged_df_2021['2021 Terrorism Score'] = pd.to_numeric(merged_df_2021['2021 Terrorism Score'].str.replace(',', ''), errors='coerce')

merged_df_2020['2020 GDP'] = pd.to_numeric(merged_df_2020['2020 GDP'].str.replace(',', ''), errors='coerce')
merged_df_2020['2020 Terrorism Score'] = pd.to_numeric(merged_df_2020['2020 Terrorism Score'].str.replace(',', ''), errors='coerce')


# In[26]:


merged_df_create_2022 = merged_df_2022[['Country', 'Incoming', 'Outgoing', '2022 GDP', '2022 Terrorism Score']]
merged_df_create_2021 = merged_df_2021[['Country', 'Incoming', 'Outgoing', '2021 GDP', '2021 Terrorism Score']]
merged_df_create_2020 = merged_df_2020[['Country', 'Incoming', 'Outgoing', '2020 GDP', '2020 Terrorism Score']]


# In[27]:


correlation_matrix_2022 = merged_df_create_2022.corr()
print("Correlation Matrix 2022:")
print(correlation_matrix_2022)
    
# Set up the matplotlib figure
plt.figure(figsize=(10, 8))
    
# Create a heatmap using seaborn
sns.heatmap(correlation_matrix_2022, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Customize the plot
plt.title('Correlation Matrix Heatmap')
plt.show()
    


correlation_matrix_2021 = merged_df_create_2021.corr()
print("Correlation Matrix 2021:")
print(correlation_matrix_2021)
    
# Set up the matplotlib figure
plt.figure(figsize=(10, 8))
    
# Create a heatmap using seaborn
sns.heatmap(correlation_matrix_2021, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Customize the plot
plt.title('Correlation Matrix Heatmap')
plt.show()


correlation_matrix_2020 = merged_df_create_2020.corr()
print("Correlation Matrix 2020:")
print(correlation_matrix_2020)
    
# Set up the matplotlib figure
plt.figure(figsize=(10, 8))
    
# Create a heatmap using seaborn
sns.heatmap(correlation_matrix_2020, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Customize the plot
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[28]:


#Heatmap for Year-on-Year Analysis

# Set up the matplotlib figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(20, 8))

# Create heatmaps using seaborn and display them in subplots
sns.heatmap(correlation_matrix_2022, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=axes[0])
axes[0].set_title('Correlation Matrix 2022')

sns.heatmap(correlation_matrix_2021, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=axes[1])
axes[1].set_title('Correlation Matrix 2021')

sns.heatmap(correlation_matrix_2020, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=axes[2])
axes[2].set_title('Correlation Matrix 2020')

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()


# In[29]:


#Line graphs to analyse year-on-year trend for Incoming vs GDP

# Calculate correlation coefficients between outgoing and GDP for each year
correlation_outgoing_gdp_2022 = merged_df_create_2022[['Outgoing', '2022 GDP']].corr().iloc[0, 1]
correlation_outgoing_gdp_2021 = merged_df_create_2021[['Outgoing', '2021 GDP']].corr().iloc[0, 1]
correlation_outgoing_gdp_2020 = merged_df_create_2020[['Outgoing', '2020 GDP']].corr().iloc[0, 1]

# Create a line chart
plt.figure(figsize=(10, 6))
years = ['2020', '2021', '2022']
correlations = [correlation_outgoing_gdp_2020, correlation_outgoing_gdp_2021, correlation_outgoing_gdp_2022]

plt.plot(years, correlations, marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Correlation between Outgoing and GDP for Different Years')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.grid(True)

# Show the plot
plt.show()


# In[30]:


#Line graphs to analyse year-on-year trend for Terrorism vs GDP

# Calculate correlation coefficients between outgoing and GDP for each year
correlation_terrorism_gdp_2022 = merged_df_create_2022[['2022 Terrorism Score', '2022 GDP']].corr().iloc[0, 1]
correlation_terrorism_gdp_2021 = merged_df_create_2021[['2021 Terrorism Score', '2021 GDP']].corr().iloc[0, 1]
correlation_terrorism_gdp_2020 = merged_df_create_2020[['2020 Terrorism Score', '2020 GDP']].corr().iloc[0, 1]

# Create a line chart
plt.figure(figsize=(10, 6))
years = ['2020', '2021', '2022']
correlations = [correlation_terrorism_gdp_2020, correlation_terrorism_gdp_2021, correlation_terrorism_gdp_2022]

plt.plot(years, correlations, marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Correlation between Terrorism Score and GDP for Different Years')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.grid(True)

# Show the plot
plt.show()


# In[31]:


#Line graphs to analyse year-on-year trend for Terrorism vs Incoming

# Calculate correlation coefficients between outgoing and GDP for each year
correlation_terrorism_incoming_2022 = merged_df_create_2022[['2022 Terrorism Score', 'Incoming']].corr().iloc[0, 1]
correlation_terrorism_incoming_2021 = merged_df_create_2021[['2021 Terrorism Score', 'Incoming']].corr().iloc[0, 1]
correlation_terrorism_incoming_2020 = merged_df_create_2020[['2020 Terrorism Score', 'Incoming']].corr().iloc[0, 1]

# Create a line chart
plt.figure(figsize=(10, 6))
years = ['2020', '2021', '2022']
correlations = [correlation_terrorism_incoming_2020, correlation_terrorism_incoming_2021, correlation_terrorism_incoming_2022]

plt.plot(years, correlations, marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Correlation between Terrorism Score and Incoming for Different Years')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.grid(True)

# Show the plot
plt.show()


# In[32]:


#Line graphs to analyse year-on-year trend for Terrorism vs Outgoing

correlation_terrorism_outgoing_2022 = merged_df_create_2022[['2022 Terrorism Score', 'Outgoing']].corr().iloc[0, 1]
correlation_terrorism_outgoing_2021 = merged_df_create_2021[['2021 Terrorism Score', 'Outgoing']].corr().iloc[0, 1]
correlation_terrorism_outgoing_2020 = merged_df_create_2020[['2020 Terrorism Score', 'Outgoing']].corr().iloc[0, 1]

# Create a line chart
plt.figure(figsize=(10, 6))
years = ['2020', '2021', '2022']
correlations = [correlation_terrorism_outgoing_2020, correlation_terrorism_outgoing_2021, correlation_terrorism_outgoing_2022]

plt.plot(years, correlations, marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Correlation between Terrorism Score and Outgoing for Different Years')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.grid(True)

# Show the plot
plt.show()


# In[33]:


# Calculate correlation coefficients between outgoing and GDP for each year
correlation_incoming_gdp_2022 = merged_df_create_2022[['Incoming', '2022 GDP']].corr().iloc[0, 1]
correlation_incoming_gdp_2021 = merged_df_create_2021[['Incoming', '2021 GDP']].corr().iloc[0, 1]
correlation_incoming_gdp_2020 = merged_df_create_2020[['Incoming', '2020 GDP']].corr().iloc[0, 1]

# Create a line chart
plt.figure(figsize=(10, 6))
years = ['2020', '2021', '2022']
correlations = [correlation_incoming_gdp_2020, correlation_incoming_gdp_2021, correlation_incoming_gdp_2022]

plt.plot(years, correlations, marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Correlation between Incoming and GDP for Different Years')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.grid(True)

# Show the plot
plt.show()


# In[39]:


sum(merged_df_2020['2020 GDP']), sum(merged_df_2021['2021 GDP']), sum(merged_df_2022['2022 GDP'])


# In[40]:


sum(merged_df_2020['2020 Terrorism Score']), sum(merged_df_2021['2021 Terrorism Score']), sum(merged_df_2022['2022 Terrorism Score'])


# In[41]:


sum(merged_df_2020['Outgoing']), sum(merged_df_2021['Outgoing']), sum(merged_df_2022['Outgoing'])


# In[42]:


sum(merged_df_2020['Incoming']), sum(merged_df_2021['Incoming']), sum(merged_df_2022['Incoming'])


# In[ ]:




