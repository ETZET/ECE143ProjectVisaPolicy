# This code is adapted from ilyankou @ https://github.com/ilyankou/passport-index-dataset/blob/master/Update.ipynb

# %% [markdown]
# # Generate Passport Index datasets
# * Data by Passport Index 2023: https://www.passportindex.org/
# * In both tidy and matrix formats
# * Using ISO-2, ISO-3, and full country names

# %%
import requests
import pandas as pd
import json

# %%
codes = pd.read_csv(
    'https://gist.githubusercontent.com/ilyankou/b2580c632bdea4af2309dcaa69860013/raw/420fb417bcd17d833156efdf64ce8a1c3ceb2691/country-codes',
    dtype=str
).fillna('NA').set_index('ISO2')

def fix_iso2(x):
    o = {
        'UK': 'GB',
        'RK': 'XK'
    }
    return o[x] if x in o else x

# %% [markdown]
# ## Get data from PassportIndex

# %%
# URL of the compare passport page
url = 'https://www.passportindex.org/comparebyPassport.php?p1=ro&p2=gt&p3=qa'

# Make a request to the .php page taht outputs data
result_raw = requests.post('https://www.passportindex.org/incl/compare2.php', headers={
    'Host': 'www.passportindex.org',
    'User-Agent': 'Mozilla/5.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '9',
    'Origin': 'https://www.passportindex.org',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}, data={
    'compare': '1'
})

# %% [markdown]
# ## Clean up the data

# %%
result = json.loads( result_raw.text )
obj = {}

for passport in result:
    
    # Fix ISO-2 codes
    passport = fix_iso2(passport)
    
    # Add passport to the object
    if passport not in obj:
        obj[passport] = {}
    
    # Add destinations for the given passport
    for dest in result[passport]['destination']:
        
        text = dest['text']
        res = ''
        
        # ** Visa required, incl Cuba's tourist card **
        if text == 'visa required' or text == 'tourist card':
            res = 'visa required'
        
        # ** Visa on arrival **
        elif 'visa on arrival' in text:
            res = 'visa on arrival'
            
        # ** Covid-19 ban ** 
        elif text == 'COVID-19 ban':
            res = 'covid ban'
            
        # ** Visa-free, incl. Seychelles' tourist registration **
        elif 'visa-free' in text or 'tourist registration' in text or 'visa waiver' in text:
            res = dest['dur'] if dest['dur'] != '' else 'visa free'
            
        # ** eVisas, incl eVisitors (Australia), eTourist cards (Suriname),
        # eTA (US), and pre-enrollment (Ivory Coast), or EVW (UK) **
        elif 'eVis' in text or 'eTourist' in text or text == 'eTA' or text == 'pre-enrollment' or text == 'EVW':
            res = 'e-visa'
            
        # ** No admission, including Trump ban **
        elif text == 'trump ban' or text == 'not admitted':
            res = 'no admission'
        
        # Update the result!
        obj[passport][ fix_iso2(dest['code']) ] = res if res != '' else dest['text']
        

# %% [markdown]
# ## Save

# %%
# ISO-2: Matrix
matrix = pd.DataFrame(obj).T.fillna(-1)
matrix.to_csv('passport-index-matrix-iso2.csv', index_label='Passport')

# ISO-2: Tidy
matrix.stack().to_csv(
    'passport-index-tidy-iso2.csv',
    index_label=['Passport', 'Destination'],
    header=['Requirement'])



# ISO-3: Matrix
iso2to3 =  { x:y['ISO3'] for x,y in codes.iterrows() }
matrix.rename(columns=iso2to3, index=iso2to3).to_csv('passport-index-matrix-iso3.csv', index_label='Passport')

# ISO-3: Tidy
matrix.rename(columns=iso2to3, index=iso2to3).stack().to_csv(
    'passport-index-tidy-iso3.csv',
    index_label=['Passport', 'Destination'],
    header=['Requirement'])


# Country names: Matrix
iso2name =  { x:y['Country'] for x,y in codes.iterrows() }
matrix.rename(columns=iso2name, index=iso2name).to_csv('passport-index-matrix.csv', index_label='Passport')

# Country names: Tidy
matrix.rename(columns=iso2name, index=iso2name).stack().to_csv(
    'passport-index-tidy.csv',
    index_label=['Passport', 'Destination'],
    header=['Requirement'])

# %%
# Print all values
tidy = matrix.rename(columns=iso2to3, index=iso2to3).stack()
tidy.value_counts()

# %%
tidy[ tidy == 'no admission' ]

# %% [markdown]
# ### Difference with previous run

# %%
tidy_old = pd.read_csv('legacy/2023-10-11/passport-index-tidy-iso3.csv')

# %%
# What percent of origin/destination pairs is different?

(tidy
 .to_frame()
 .reset_index()
 .merge(
     tidy_old, how='inner',
     left_on=['level_0', 'level_1'],
     right_on=['Passport', 'Destination']
 )
 .assign(
     is_different=lambda df_: df_[0].ne(df_.Requirement)
 )
 .query('is_different & (Passport != Destination)')
)

# %%



