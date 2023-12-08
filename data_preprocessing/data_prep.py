# %%
import pandas as pd
import numpy as np

# %%
# Read Data
passport_idx = pd.read_csv('data/passport-index-tidy.csv')
countries = pd.read_csv('data/countries of the world.csv')
freedom = pd.read_csv('data/freedom.csv', encoding='utf-8')
terrorism = pd.read_excel('data/Global Terrorism Index 2023.xlsx', \
                        sheet_name='Combined raw')

# remove columns where passport = destination
passport_idx = passport_idx[passport_idx['Passport'] != passport_idx['Destination']]

# preprocessing the countries attribute
countries['Country'] = countries['Country'].str.strip().str.replace('&', 'and')
countries['Region'] = countries['Region'].str.strip()
countries['Country'] = countries['Country'].replace({'Bolivia (Plurinational State of)':'Bolivia'})

# preprocess the freedom database
filtered_freedom = freedom[freedom['year']==2020]
filtered_freedom = filtered_freedom.drop(columns=['year','Region_Code'])
# rename some columns
filtered_freedom.rename(columns={'Region_Name': 'Region_Simplified', \
                                 'is_ldc': 'is_Developed_Country', \
                                 'Status': 'Freedom_Status', \
                                'CL': 'Civil_Liberties', \
                                'PR': 'Political_rights'}, inplace=True)
country_mapping = {
    'Cape Verde': 'Cabo Verde',
    'The Gambia': 'Gambia',
    'Democratic Republic of the Congo': 'DR Congo',
    "Côte d'Ivoire": 'Ivory Coast',
    'Republic of Kosovo': 'Kosovo',
    'Kingdom of Eswatini': 'Eswatini',
    'East Timor': 'Timor-Leste',
    "Democratic People's Republic of Korea": 'North Korea',
    'Republic of North Macedonia': 'North Macedonia',
    'Vatican City': 'Vatican',
    'Vietnam': 'Viet Nam',
    'Bolivia (Plurinational State of)': 'Bolivia',
    'Brunei Darussalam': 'Brunei',
    'Czechia': 'Czech Republic',
    'Iran (Islamic Republic of)': 'Iran',
    "Lao People's Democratic Republic": "Laos",
    'Micronesia (Federated States of)': 'Micronesia',
    "Republic of Korea": 'South Korea',
    'Republic of Moldova': 'Moldova',
    'Russian Federation': 'Russia',
    'Syrian Arab Republic': 'Syria',
    'United Republic of Tanzania': 'Tanzania',
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
    'United States of America': 'United States',
    'Venezuela (Bolivarian Republic of)': 'Venezuela'
}
filtered_freedom['country'] = filtered_freedom['country'].replace(country_mapping)
freedom = filtered_freedom.reset_index(drop=True)

# clean terrorism entries
country_mapping = {
    'DR Congo': 'Democratic Republic of the Congo',
    'Ivory Coast': "Cote d' Ivoire",
    'Kosovo': 'Republic of Kosovo',
    'Macedonia (FYR)': 'North Macedonia'
}
terrorism['Country'] = terrorism['Country'].replace(country_mapping)
terrorism = terrorism[terrorism['Year']==2020]
terrorism = terrorism.drop(columns=['Year','iso3c']).reset_index(drop=True)

# %%
column_prefixes = [
    'Population',
    'Area (sq. mi.)',
    'Pop. Density (per sq. mi.)',
    'Coastline (coast/area ratio)',
    'Net migration',
    'Infant mortality (per 1000 births)',
    'GDP ($ per capita)',
    'Literacy (%)',
    'Phones (per 1000)',
    'Arable (%)',
    'Crops (%)',
    'Other (%)',
    'Climate',
    'Birthrate',
    'Deathrate',
    'Agriculture',
    'Industry',
    'Service'
]
for col in column_prefixes:
    if countries[col].dtype == 'object':
        countries[col] = countries[col].str.replace(',', '.').astype(float)
        # countries[col] = pd.to_numeric(countries[col], errors='coerce')

# %%
# Merge Terrorism 
# for attribute in terrorism.columns.drop('Country'):
#     passport_idx = passport_idx.merge(terrorism[['Country',attribute]], \
#                                     left_on='Passport',right_on='Country', how='left')
#     passport_idx.rename(columns={attribute: f'Passport_{attribute}'}, inplace=True)
    
#     passport_idx = passport_idx.merge(terrorism[['Country',attribute]], \
#                                     left_on='Destination',right_on='Country', how='left')
#     passport_idx.rename(columns={attribute: f'Destination_{attribute}'}, inplace=True)
#     passport_idx.drop(columns=['Country_x', 'Country_y'], inplace=True)
# from itertools import product
# ij = ['Passport', 'Destination']
# fill_zeros = ['Incidents', 'Fatalities', 'Injuries', 'Hostages','Score']
# fill_zeros = [f"{place}_{attribute}" for place, attribute in list(product(ij, fill_zeros))]
# passport_idx[fill_zeros] = passport_idx[fill_zeros].fillna(0)
# passport_idx[['Passport_Rank','Destination_Rank']] = passport_idx[['Passport_Rank','Destination_Rank']].fillna(105)

# Merge the countries and passport idx
for attribute in countries.columns.drop('Country'):
    passport_idx = passport_idx.merge(countries[['Country',attribute]], \
                                    left_on='Passport',right_on='Country', how='left')
    passport_idx.rename(columns={attribute: f'Passport_{attribute}'}, inplace=True)
    
    passport_idx = passport_idx.merge(countries[['Country',attribute]], \
                                    left_on='Destination',right_on='Country', how='left')
    passport_idx.rename(columns={attribute: f'Destination_{attribute}'}, inplace=True)
    passport_idx.drop(columns=['Country_x', 'Country_y'], inplace=True)

# Merge Freedom
# for attribute in freedom.columns.drop('country'):
#     passport_idx = passport_idx.merge(freedom[['country',attribute]], \
#                                     left_on='Passport',right_on='country', how='left')
#     passport_idx.rename(columns={attribute: f'Passport_{attribute}'}, inplace=True)
    
#     passport_idx = passport_idx.merge(freedom[['country',attribute]], \
#                                     left_on='Destination',right_on='country', how='left')
#     passport_idx.rename(columns={attribute: f'Destination_{attribute}'}, inplace=True)
#     passport_idx.drop(columns=['country_x', 'country_y'], inplace=True)

# %%
countries

# %%
passport_idx

# %%
# create one_hot columns
def is_visa_free(value):
    value = str(value)
    if value.isdigit():
        return True
    else:
        return value in ['visa free', 'visa on arrival']
def is_travel_permitted(value):
    value = str(value)
    return value not in ['covid ban', 'no admission']
passport_idx['Is_Visa_Free'] = passport_idx['Requirement'].apply(is_visa_free)
passport_idx['Is_Travel_Permitted'] = passport_idx['Requirement'].apply(is_travel_permitted)

# %%
passport_idx
# instead of internal/external
# basic attributes GDP, populations, fertility...
# advanced attributes, terrosrism, skilled worker, ... 

# %%
# passport_idx.to_csv('data/passport-index-merged.csv')
passport_idx.to_csv('data/passport-index-basic.csv')
countries.to_csv('data/countries-preprocessed.csv')


