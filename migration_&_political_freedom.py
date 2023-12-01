import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""## Load the data"""

countries = pd.read_csv('data/countries-preprocessed.csv')
freedom = pd.read_csv('data/freedom.csv', encoding='utf-8')
terrorism = pd.read_excel('data/Global Terrorism Index 2023.xlsx', \
                        sheet_name='Combined raw')

# preprocessing the countries attribute
countries['Country'] = countries['Country'].str.strip().str.replace('&', 'and')
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

data = pd.read_csv('data/passport-index-basic.csv')
passport_grouped = data.groupby(by='Passport')['Is_Visa_Free'].sum().reset_index()
passport_grouped.rename(columns={'Is_Visa_Free':'Score'},inplace=True)
country_grouped = passport_grouped.rename(columns={"Passport":"country"})
merge_freedom = pd.merge(freedom, country_grouped, on='country', how='inner')
df = pd.read_csv("data/passport-index-merged.csv")

"""## Can improved political freedom lead to a country achieving visa-free status?

The heatmap reveals a positive correlation between the indicators of political freedom ('Civil_Liberties,' 'Political_rights', 'is_Developed_Country', 'Freedom_Status') and the score of visa freedom. However, the relationship is relatively weak. This suggests that an increase in political freedom may correspond to a slight increase in visa freedom scores, or vice versa.
"""

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df['Passport_Freedom_Status_Encoded'] = label_encoder.fit_transform(df['Passport_Freedom_Status'])
df['Destination_Freedom_Status_Encoded'] = label_encoder.fit_transform(df['Destination_Freedom_Status'])
df['Passport_Region_Simplified_Encoded'] = label_encoder.fit_transform(df['Passport_Region_Simplified'])
df['Destination_Region_Simplified_Encoded'] = label_encoder.fit_transform(df['Destination_Region_Simplified'])

fig, ax = plt.subplots(figsize = (18, 14))
sns.set(style="white")
correlation_data = df[['Passport_Civil_Liberties', 'Passport_Political_rights', 'Passport_is_Developed_Country', 'Passport_Freedom_Status_Encoded', 'Passport_Region_Simplified_Encoded',
             'Destination_Civil_Liberties', 'Destination_Political_rights', 'Destination_is_Developed_Country', 'Destination_Freedom_Status_Encoded', 'Destination_Region_Simplified_Encoded',
                       'Passport_Score', 'Destination_Score']]

correlation_matrix = correlation_data.corr(numeric_only=True)

sns.heatmap(correlation_matrix,annot=True, fmt='.1f', vmin=-1, vmax=1, center= 0, cmap= 'coolwarm', mask= np.triu(correlation_matrix))
plt.title('Correlation Matrix Heatmap: Political Freedom vs. Visa-Free Score')
plt.show()

"""Based on the univariate bar chart analysis of several factors related to political freedom, several observations can be made:

- Across different regions, countries in Europe tend to have higher visa-free scores, while Africa has the lowest. When ranked in descending order based on the tendency to receive visa-free access, the regions are as follows: Europe, Americas, Oceania, Asia, and Africa.

- When categorized by freedom status, countries or regions classified as "Free" exhibit higher visa-free scores, followed by "Partially Free," and lastly, "Not Free." There is a positive correlation between the level of freedom in a country or region and its visa-free score.

- Developed countries or regions have higher visa-free scores compared to those that are not developed. There is a positive correlation between visa-free scores and the level of development of a country or region.

- The better the civil liberties in a country or region, the higher their visa-free score. There is a positive correlation between visa-free scores and civil liberties.

- Countries or regions exhibiting stronger political rights generally experience higher visa-free scores. Nevertheless, the results indicate the presence of an outlier.
"""

sns.set(style="white")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(x='Region_Simplified', y='Score', data=merge_freedom, ax=axes[0], palette="plasma_r",
           errcolor='#DB7093', errwidth=2, alpha=0.3)
axes[0].set_title('Region vs. Visa-Free Score')
axes[0].set_xlabel('Region')
axes[0].set_ylabel('Score')

sns.barplot(x='Freedom_Status', y='Score', data=merge_freedom, ax=axes[1], palette="plasma_r",
           errcolor='#DB7093', errwidth=2, alpha=0.3)
axes[1].set_title('Freedom Status vs. Visa-Free Score')
axes[1].set_xlabel('Freedom Status')
axes[1].set_ylabel('Score')

sns.barplot(x='is_Developed_Country', y='Score', data=merge_freedom, ax=axes[2], palette="plasma_r",
           errcolor='#DB7093', errwidth=2, alpha=0.3)
axes[2].set_title('Development vs. Visa-Free Score')
axes[2].set_xticklabels(['Developed Country', 'Not Developed Country'])
axes[2].set_xlabel('Development')
axes[2].set_ylabel('Score')

sns.despine(left=True,bottom =True)
plt.tight_layout()

plt.show()

sns.set(style="white")
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

sns.barplot(x='Civil_Liberties', y='Score', data=merge_freedom, ax=axes[0], palette="plasma_r",
           errcolor='#DB7093', errwidth=2, alpha=0.3)
axes[0].set_title('Civil Liberties vs. Visa-Free Score')
axes[0].set_xlabel('Civil Liberties')
axes[0].set_ylabel('Score')

sns.barplot(x='Political_rights', y='Score', data=merge_freedom, ax=axes[1], palette="plasma_r",
           errcolor='#DB7093', errwidth=2, alpha=0.3)
axes[1].set_title('Political rights vs. Visa-Free Score')
axes[1].set_xlabel('Political rights')
axes[1].set_ylabel('Score')


sns.despine(left=True,bottom =True)
plt.tight_layout()

plt.show()

"""A regression analysis was conducted for the features 'Civil_Liberties,' 'Political_rights,' and 'is_Developed_Country' with respect to the dependent variable "Score." In this model, the R-squared value is 0.634, indicating that the model accounts for 63.4% of the variance in the dependent variable 'Score.' The F-statistic is 107.6, and the corresponding p-value (Prob (F-statistic)) is very small, signifying the overall significance of the model. Overall, the model is statistically significant.

The relationships between 'Civil_Liberties' and 'is_Developed_Country' with 'Score' are significant, while the relationship between 'Political_rights' and 'Score' is not statistically significant. Interpreting the coefficients' signs and magnitudes, along with the p-values, provides insights into the relationships between the variables and the dependent variable. The coefficient for 'Civil_Liberties' is negative, suggesting that an increase in the value of political freedom (i.e., a decrease in freedom) tends to decrease the 'Score.' Similarly, the coefficient for 'is_Developed_Country' is negative, indicating that when a country is not developed(is_Developed_Country = 1), the 'Score' also tends to decrease.
"""

import statsmodels.api as sm

X = merge_freedom[['Civil_Liberties', 'Political_rights','is_Developed_Country']]
X = sm.add_constant(X)
y = merge_freedom['Score']
model = sm.OLS(y, X).fit()
model.summary()

"""In summary, the heatmap analysis suggests a weak positive correlation between political freedom indicators and visa freedom scores. European countries tend to have higher visa-free scores, as do 'Free' and developed nations. Regression analysis confirms these trends, with civil liberties and development status influencing visa freedom scores. The overall model is statistically significant (R-squared = 0.634, F-statistic = 107.6), while the impact of political rights on scores is not significant.

## Does migration lead to a country achieving visa-free status?
To what extent does migration contribute to the determination of a country's visa-free scores? Our investigation involves examining the relationship between migration indicators ("Passport_Net migration" and "Destination_Net migration") and visa-free scores ("Passport_Score" and "Destination_Score"). Subsequent analysis of heatmaps and Contour Plots, however, reveals a lack of significant correlation between migration dynamics and visa-free scores. The visualizations indicate that the migration factor does not play a prominent role in shaping the visa-free scores of countries.
"""

interest_columns = ['Passport_Net migration', 'Passport_Score', 'Destination_Net migration', 'Destination_Score']
correlation_matrix = df[interest_columns].corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', vmin=-1, vmax=1, center= 0, cmap= 'coolwarm', mask= np.triu(correlation_matrix))
plt.title('Correlation Heatmap: Net Migration vs. Visa-Free Score')

plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

sns.kdeplot(x='Passport_Net migration', y='Passport_Score', data=df, fill=True, cmap='Blues', levels=20, ax=axes[0])
axes[0].set_xlabel('Net migration')
axes[0].set_ylabel('Score')
axes[0].set_title('Contour Plot: Net Migration vs Outgoing Visa-Free Score')

sns.kdeplot(x='Destination_Net migration', y='Destination_Score', data=df, fill=True, cmap='Blues', levels=20, ax=axes[1])
axes[1].set_xlabel('Net migration')
axes[1].set_ylabel('Score')
axes[1].set_title('Contour Plot: Net Migration vs Incoming Visa-Free Score')
sns.despine(left=True,bottom =True)

plt.tight_layout()

plt.show()