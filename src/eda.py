# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
data = pd.read_csv('data/passport-index-basic.csv')
countries = pd.read_csv('data/countries-preprocessed.csv')
passport_grouped = data.groupby(by='Passport')['Is_Visa_Free'].sum().reset_index()
passport_grouped.rename(columns={'Is_Visa_Free':'Score'},inplace=True)
dest_grouped = data.groupby(by='Destination')['Is_Visa_Free'].sum().reset_index()
dest_grouped.rename(columns={'Is_Visa_Free':'Score'},inplace=True)

# %%
# join the table
passport_grouped = pd.merge(passport_grouped, countries,how='left',left_on='Passport',right_on='Country').drop(columns='Country')
dest_grouped = pd.merge(dest_grouped, countries,how='left',left_on='Destination',right_on='Country').drop(columns='Country')

# discreize the score column
# Define the bin edges
bins = range(0, 201, 25)
# Use pd.cut to discretize
passport_grouped['Score_Bin'] = pd.cut(passport_grouped['Score'], bins=bins, right=False, include_lowest=True)
dest_grouped['Score_Bin'] = pd.cut(dest_grouped['Score'], bins=bins, right=False, include_lowest=True)

# %% [markdown]
# ## Univariate Study of Travel Requirement
# Key Findings:
# - The distribution of incoming travel-free-countries follows a trimodal distribution
#   - First mode: (90-100), Second mode: (190-200), Third mode: (0-10)
#   - Countries that have very strict travel visa policies (0-10):
#     - Afghanistan, Algeria, Australia, Bhutan, Cameroon, Canada, DR Congo, Djibouti, Equatorial Guinea, Eritrea, India, Libya, New Zealand, North Korea, Pakistan, Papua New Guinea, South Sudan, Sri Lanka, Sudan, Turkmenistan, United States
#   - Countries that have very lenient travel visa polices (190-200):
#     - Bolivia, Burundi, Cambodia, Cape Verde, Comoros, Dominica, Guinea-Bissau, Haiti, Macao, Madagascar, Maldives, Mauritania, Micronesia, Mozambique, Palau, Rwanda, Samoa, Seychelles, Somalia, Timor-Leste, Togo, Tuvalu
# - The distribution of outgoing travel-free-countries a a completely different story, where the number is rarely at the extreme.
#   - The country that have most travel free coutries > 150: 
#     - United Arab Emirates
#   - The countries that have the least travel free countries <30:
#     - Afghanistan, Iraq, Pakistan, Syria

# %%
bins = range(0, 201, 10)

# First plot data preparation
passport_grouped['binned'] = pd.cut(passport_grouped['Score'], bins=bins, right=False, include_lowest=True)
passport_bin_counts = passport_grouped['binned'].value_counts().sort_index()

# Second plot data preparation
dest_grouped['binned'] = pd.cut(dest_grouped['Score'], bins=bins, right=False, include_lowest=True)
dest_bin_counts = dest_grouped['binned'].value_counts().sort_index()

# Set up a figure with two subplots
plt.figure(figsize=(20, 7))  # Adjust the size of the figure as needed

# First subplot for passport_grouped data
plt.subplot(1, 2, 1)  # (rows, columns, subplot number)
sns.barplot(x=passport_bin_counts.index.astype(str), y=passport_bin_counts.values)
plt.xticks(rotation=45)  # Rotate the labels for better readability
plt.xlabel('Number of Outgoing Travel-Visa-Free Countries')
plt.ylabel('Counts')
plt.title('Distribution of Number of Outgoing Travel-Visa-Free Countries')

# Second subplot for dest_grouped data
plt.subplot(1, 2, 2)  # (rows, columns, subplot number)
sns.barplot(x=dest_bin_counts.index.astype(str), y=dest_bin_counts.values)
plt.xticks(rotation=45)  # Rotate the labels for better readability
plt.xlabel('Number of Incoming Travel-Visa-Free Countries')
plt.ylabel('Counts')
plt.title('Distribution of Number of Incoming Travel-Visa-Free Countries')

# Show the figure with both subplots
plt.show()

# %%
top_three_bins = dest_grouped['binned'].value_counts().sort_values(ascending=False).head(3).index

# Step 2: Filter countries by these bins
countries_in_top_bins = []
for bin in top_three_bins:
    countries = dest_grouped[dest_grouped['binned'] == bin]['Destination'].tolist()
    countries_in_top_bins.append(countries)
for i, bin in enumerate(top_three_bins):
    print(bin, countries_in_top_bins[i])


bin_counts = passport_grouped['binned'].value_counts()
non_zero_bins = bin_counts[bin_counts > 0].sort_values(ascending=True).head(3).index

countries_in_lowest_bins = []
for bin in non_zero_bins:
    countries = passport_grouped[passport_grouped['binned'] == bin]['Passport'].tolist()
    countries_in_lowest_bins.append(countries)

for i, bin in enumerate(non_zero_bins):
    print(f"Bin: {bin}, Countries: {countries_in_lowest_bins[i]}")

# %% [markdown]
# ## Explorative data analysis with number of visa-free countries
# Key observations:
# - Countries that have lower infant mortality have more travel-visa-free countries.
# - Countries that have higher GDP have more travel-visa-free countries.
# - Countries that have higher literacy have more travel-visa-free countries.
# - Countries that have more phones per 1000 persons have more travel-visa-free countries.
# - Countires that have lower birthrate have more travel-visa-free countries.
# 
# These observations are very intuitive, since these factors are indicators of economic development, the more economic developed, the more visa-travel-free countries. 
# However, no simple observations can be made about the the number incoming-visa-free countries. Each countries incoming visa policy are more involved, rather than juding from visitors's countries basic attributes.

# %%
def plot_side_by_side_boxplots(data1, data2, attribute, use_log_scale=False):
    """
    Plots side-by-side boxplots for two specified columns from the DataFrame.

    Parameters:
    data (DataFrame): The DataFrame containing the data.
    column1 (str): The name of the first column to plot.
    group_by_column (str): The name of the column to group the data by. Defaults to 'Is_Visa_Free'.
    """
    
    plt.figure(figsize=(20, 7))  # Adjust the size of the figure as needed
    
    # First subplot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='Score_Bin', y=attribute, data=data1,)
    if use_log_scale:
        plt.yscale('log')
    plt.title(f'Boxplot of {attribute} by Number of Outgoing Visa-Free Countries')
    
    # Second subplot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='Score_Bin', y=attribute, data=data2)
    if use_log_scale:
        plt.yscale('log')
    plt.title(f'Boxplot of {attribute} by Number of Incoming Visa-Free Countries')
    
    plt.show()

# %%
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Population', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Area (sq. mi.)', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Pop. Density (per sq. mi.)', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Coastline (coast/area ratio)', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Net migration', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Infant mortality (per 1000 births)', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='GDP ($ per capita)', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Literacy (%)', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Phones (per 1000)', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Arable (%)', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Crops (%)', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Climate', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Birthrate', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Deathrate', use_log_scale=False)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Agriculture', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Industry', use_log_scale=True)
plot_side_by_side_boxplots(passport_grouped, dest_grouped, attribute='Service', use_log_scale=True)


