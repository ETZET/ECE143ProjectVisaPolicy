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


#OUTGOING


# In[3]:


country_out_2023 = defaultdict(int)

passport_data_2023 = np.genfromtxt('passport-index-matrix-iso3.csv', delimiter=',', dtype=str, skip_header=1)

for i in passport_data_2023:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_out_2023[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_out_2023[coun] += 1
            
country_visa_outgoing_2023 = dict(sorted(country_out_2023.items(), key=lambda item: item[1], reverse= True))


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


df_2023 = np.genfromtxt('passport-index-iso3-transposed.csv', delimiter=',', dtype=str, skip_header=1)


# In[9]:


df_2022 = np.genfromtxt('passport-index-matrix-iso3-transposed-2022.csv', delimiter=',', dtype=str, skip_header=1)


# In[10]:


df_2021 = np.genfromtxt('passport-index-matrix-iso3-transposed-2021.csv', delimiter=',', dtype=str, skip_header=1)


# In[11]:


df_2020 = np.genfromtxt('passport-index-matrix-iso3-transposed-2020.csv', delimiter=',', dtype=str, skip_header=1)


# In[12]:


country_in_2023 = defaultdict(int)
country_in_2022 = defaultdict(int)
country_in_2021 = defaultdict(int)
country_in_2020 = defaultdict(int)


# In[13]:


for i in df_2023:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_in_2023[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_in_2023[coun] += 1
            
country_visa_incoming_2023 = dict(sorted(country_in_2023.items(), key=lambda item: item[1], reverse= True))


# In[14]:


for i in df_2022:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_in_2022[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_in_2022[coun] += 1
            
country_visa_incoming_2022 = dict(sorted(country_in_2022.items(), key=lambda item: item[1], reverse= True))


# In[15]:


for i in df_2021:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_in_2021[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_in_2021[coun] += 1
            
country_visa_incoming_2021 = dict(sorted(country_in_2021.items(), key=lambda item: item[1], reverse= True))


# In[16]:


for i in df_2020:
    coun = i[0]
    # print(coun)
    #print(len(i))
    country_in_2020[coun] = 0
    for j in range(len(i)):
        if i[j] =="visa on arrival" or i[j] =="visa free" or i[j].isdigit():
            country_in_2020[coun] += 1
            
country_visa_incoming_2020 = dict(sorted(country_in_2020.items(), key=lambda item: item[1], reverse= True))


# In[ ]:





# In[17]:


#COVID DATA 


# In[19]:


df_covid = np.genfromtxt("owid-covid-data.csv", delimiter=',', dtype=str, skip_header=1)


# In[21]:


covid_cases_2020 = defaultdict(int)
covid_cases_2021 = defaultdict(int)
covid_cases_2022 = defaultdict(int)
covid_cases_2023 = defaultdict(int)


# In[22]:


for i in df_covid:
    coun = i[0]
    if i[5] =='':
        continue
    cases = float(i[5])
    year = dateutil.parser.parse(i[3]).year
    if year == 2020:
        if covid_cases_2020[coun] < cases :
            covid_cases_2020[coun] = cases
    elif year == 2021:
        if covid_cases_2021[coun] < cases :
            covid_cases_2021[coun] = cases
    elif year == 2022:
        if covid_cases_2022[coun] < cases :
            covid_cases_2022[coun] = cases
    elif year == 2023:
        if covid_cases_2023[coun] < cases :
            covid_cases_2023[coun] = cases   


# In[23]:


covid_country_2023 = dict(sorted(covid_cases_2023.items(), key=lambda item: item[1], reverse= True))
covid_country_2022 = dict(sorted(covid_cases_2022.items(), key=lambda item: item[1], reverse= True))
covid_country_2021 = dict(sorted(covid_cases_2021.items(), key=lambda item: item[1], reverse= True))
covid_country_2020 = dict(sorted(covid_cases_2020.items(), key=lambda item: item[1], reverse= True))


# In[24]:


# Create DataFrames from dictionaries


# In[25]:


incoming_df_2023 = pd.DataFrame(list(country_visa_incoming_2023.items()), columns=['Country', 'Incoming'])
outgoing_df_2023 = pd.DataFrame(list(country_visa_outgoing_2023.items()), columns=['Country', 'Outgoing'])
covid_df_2023 = pd.DataFrame(list(covid_cases_2023.items()), columns=['Country', 'Covid Cases'])


# In[26]:


incoming_df_2022 = pd.DataFrame(list(country_visa_incoming_2022.items()), columns=['Country', 'Incoming'])
outgoing_df_2022 = pd.DataFrame(list(country_visa_outgoing_2022.items()), columns=['Country', 'Outgoing'])
covid_df_2022 = pd.DataFrame(list(covid_cases_2022.items()), columns=['Country', 'Covid Cases'])


# In[27]:


incoming_df_2021 = pd.DataFrame(list(country_visa_incoming_2021.items()), columns=['Country', 'Incoming'])
outgoing_df_2021 = pd.DataFrame(list(country_visa_outgoing_2021.items()), columns=['Country', 'Outgoing'])
covid_df_2021 = pd.DataFrame(list(covid_cases_2021.items()), columns=['Country', 'Covid Cases'])


# In[28]:


incoming_df_2020 = pd.DataFrame(list(country_visa_incoming_2020.items()), columns=['Country', 'Incoming'])
outgoing_df_2020 = pd.DataFrame(list(country_visa_outgoing_2020.items()), columns=['Country', 'Outgoing'])
covid_df_2020 = pd.DataFrame(list(covid_cases_2020.items()), columns=['Country', 'Covid Cases'])


# In[30]:


# Merge the DataFrames on 'Country' to create Heatmaps and Correlation Matrix
merged_df_2023 = pd.merge(incoming_df_2023, outgoing_df_2023, on='Country')
merged_df_2023 = pd.merge(merged_df_2023, covid_df_2023, on='Country')

merged_df_2022 = pd.merge(incoming_df_2022, outgoing_df_2022, on='Country')
merged_df_2022 = pd.merge(merged_df_2022, covid_df_2022, on='Country')

merged_df_2021 = pd.merge(incoming_df_2021, outgoing_df_2021, on='Country')
merged_df_2021 = pd.merge(merged_df_2021, covid_df_2021, on='Country')

merged_df_2020 = pd.merge(incoming_df_2020, outgoing_df_2020, on='Country')
merged_df_2020 = pd.merge(merged_df_2020, covid_df_2020, on='Country')


# In[35]:


df_continent = np.genfromtxt("country-continent.csv", delimiter=',', dtype=str, skip_header=1)


# In[36]:


country_continent = pd.DataFrame({'Country': df_continent[:, 0], 'Continent': df_continent[:, 1]})


# In[37]:


country_continent


# In[38]:


# Merge the DataFrames on 'Continent' to create Donut charts
merged_df_continent_2023 = pd.merge(incoming_df_2023, outgoing_df_2023, on='Country')
merged_df_continent_2023 = pd.merge(merged_df_continent_2023, covid_df_2023, on='Country')
merged_df_continent_2023 = pd.merge(merged_df_continent_2023, country_continent, on='Country')

merged_df_continent_2022 = pd.merge(incoming_df_2022, outgoing_df_2022, on='Country')
merged_df_continent_2022 = pd.merge(merged_df_continent_2022, covid_df_2022, on='Country')
merged_df_continent_2022 = pd.merge(merged_df_continent_2022, country_continent, on='Country')

merged_df_continent_2021 = pd.merge(incoming_df_2021, outgoing_df_2021, on='Country')
merged_df_continent_2021 = pd.merge(merged_df_continent_2021, covid_df_2021, on='Country')
merged_df_continent_2021 = pd.merge(merged_df_continent_2021, country_continent, on='Country')

merged_df_continent_2020 = pd.merge(incoming_df_2020, outgoing_df_2020, on='Country')
merged_df_continent_2020 = pd.merge(merged_df_continent_2020, covid_df_2020, on='Country')
merged_df_continent_2020 = pd.merge(merged_df_continent_2020, country_continent, on='Country')


# In[39]:


merged_df_continent_2020


# In[55]:


# Function to create a combined donut chart with legends, values, and a table
def combined_donut_chart_outgoing(data, title):
    fig, (ax, ax_table) = plt.subplots(1, 2, figsize=(14, 8), gridspec_kw={'width_ratios': [4, 1]})
    
    # Include Antarctica in the continent data if not present
    if 'Antarctica' not in data['Continent'].unique():
        data = data.append({'Country': 'Antarctica', 'Continent': 'Antarctica', 'Covid Cases 2023': 0, 'Outgoing': 0}, ignore_index=True)

    # Create inner donut (total COVID cases)
    inner_radius = 0.6
    width = 0.4
    cmap = plt.get_cmap('tab10')
    colors_inner = cmap(range(len(data['Country'].unique())))

    # Sum the COVID cases for each continent
    covid_by_continent = data.groupby('Continent')['Covid Cases'].sum()

    inner_pie, _ = ax.pie(covid_by_continent, radius=inner_radius, startangle=90, colors=colors_inner, wedgeprops=dict(width=width), labels=None)

    # Create outer donut (outgoing)
    outer_radius = inner_radius + width + 0.2
    colors_outer = cmap(range(len(data['Country'].unique())))

    # Sum the outgoing values for each continent
    outgoing_by_continent = data.groupby('Continent')['Outgoing'].sum()

    outer_pie, _ = ax.pie(outgoing_by_continent, radius=outer_radius, startangle=90, colors=colors_outer, wedgeprops=dict(width=width), labels=outgoing_by_continent.index.map(str))

    # Adding legends
    #ax.legend([inner_pie[0], outer_pie[0]], ['Total COVID Cases', 'Outgoing Visas'], loc='upper right')

    # Shifting the title up
    ax.set_title(title, pad=20)  # Adjust the pad value as needed

    # Adding a separate table for percentages
    table_data = {'Continent': outgoing_by_continent.index,
                  'Outgoing %': outgoing_by_continent / outgoing_by_continent.sum() * 100,
                  'COVID %': covid_by_continent / covid_by_continent.sum() * 100}
 
    table_data['Outgoing %'] = table_data['Outgoing %'].round(2)
    table_data['COVID %'] = table_data['COVID %'].round(2)

    table_df = pd.DataFrame(table_data)
    ax_table.axis('off')
    table = ax_table.table(cellText=table_df.values, colLabels=table_df.columns, cellLoc='center', loc='center')

    # Adjust the layout of the table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(2.5, 2.5)  # Adjust the scale as needed

    ax.set(aspect="equal")
    plt.show()


# In[59]:


# Call the function
combined_donut_chart_outgoing(merged_df_continent_2023, 'COVID Cases (Inner) vs Outgoing Visas (Outer) by Continent (2023)')
combined_donut_chart_outgoing(merged_df_continent_2022, 'COVID Cases (Inner) vs Outgoing Visas (Outer) by Continent (2022)')
combined_donut_chart_outgoing(merged_df_continent_2021, 'COVID Cases (Inner) vs Outgoing Visas (Outer) by Continent (2021)')
combined_donut_chart_outgoing(merged_df_continent_2020, 'COVID Cases (Inner) vs Outgoing Visas (Outer) by Continent (2020)')


# In[58]:


# Function to create a combined donut chart with legends, values, and a table
def combined_donut_chart_incoming(data, title):
    fig, (ax, ax_table) = plt.subplots(1, 2, figsize=(14, 8), gridspec_kw={'width_ratios': [4, 1]})
    
    # Include Antarctica in the continent data if not present
    if 'Antarctica' not in data['Continent'].unique():
        data = data.append({'Country': 'Antarctica', 'Continent': 'Antarctica', 'Covid Cases 2023': 0, 'Outgoing': 0}, ignore_index=True)

    # Create inner donut (total COVID cases)
    inner_radius = 0.6
    width = 0.4
    cmap = plt.get_cmap('tab10')
    colors_inner = cmap(range(len(data['Country'].unique())))

    # Sum the COVID cases for each continent
    covid_by_continent = data.groupby('Continent')['Covid Cases'].sum()

    inner_pie, _ = ax.pie(covid_by_continent, radius=inner_radius, startangle=90, colors=colors_inner, wedgeprops=dict(width=width), labels=None)

    # Create outer donut (outgoing)
    outer_radius = inner_radius + width + 0.2
    colors_outer = cmap(range(len(data['Country'].unique())))

    # Sum the outgoing values for each continent
    outgoing_by_continent = data.groupby('Continent')['Incoming'].sum()

    outer_pie, _ = ax.pie(outgoing_by_continent, radius=outer_radius, startangle=90, colors=colors_outer, wedgeprops=dict(width=width), labels=outgoing_by_continent.index.map(str))

    # Adding legends
    #ax.legend([inner_pie[0], outer_pie[0]], ['Total COVID Cases', 'Outgoing Visas'], loc='upper right')

    # Shifting the title up
    ax.set_title(title, pad=20)  # Adjust the pad value as needed

    # Adding a separate table for percentages
    table_data = {'Continent': outgoing_by_continent.index,
                  'Incoming %': outgoing_by_continent / outgoing_by_continent.sum() * 100,
                  'COVID %': covid_by_continent / covid_by_continent.sum() * 100}

    table_data['Incoming %'] = table_data['Incoming %'].round(2)
    table_data['COVID %'] = table_data['COVID %'].round(2)
    

    table_df = pd.DataFrame(table_data)
    ax_table.axis('off')
    table = ax_table.table(cellText=table_df.values, colLabels=table_df.columns, cellLoc='center', loc='center')

    # Adjust the layout of the table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(2.5, 2.5)  # Adjust the scale as needed

    ax.set(aspect="equal")
    plt.show()


# In[60]:


# Call the function
combined_donut_chart_incoming(merged_df_continent_2023, 'COVID Cases (Inner) vs Incoming Visas (Outer) by Continent (2023)')
combined_donut_chart_incoming(merged_df_continent_2022, 'COVID Cases (Inner) vs Incoming Visas (Outer) by Continent (2022)')
combined_donut_chart_incoming(merged_df_continent_2021, 'COVID Cases (Inner) vs Incoming Visas (Outer) by Continent (2021)')
combined_donut_chart_incoming(merged_df_continent_2020, 'COVID Cases (Inner) vs Incoming Visas (Outer) by Continent (2020)')


# In[74]:





# In[ ]:




