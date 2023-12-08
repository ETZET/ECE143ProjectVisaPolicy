# ECE143ProjectVisaPolicy

## Files
```
data_prep.py - Dataset Pre-processing Script
eda.py - Explorative Data Analysis Script
data_download.py - Scrapping Data from Passportindex.com
migration_&_political_freedom.py - Exploring how migration and political freedom impact travel visa-free scores
covid.py - Explores Covid-19 impact visa policy in a temporal dimension
terrorism-GDP.py - Explores Terrorism Activities, GDP impact visa policy in a temporal dimension
Reciprocity_Asymmetry.py - Analyzing whether visa-free access is always reciprocated between countries
visualization_final.ipynb - All the visualizations generated for the presentation
config_file.yaml - config file to define path and name variables for geoviews_gif.py and geoviews_tools.py
geoviews_gif.py - python script to generate the gif of outgoing and incoming visa free travel across different years
geoviews_tools.py - python script to generate a visual interactive tool of outgoing and incoming visa free travel across different years
utils.py - helper functions to run geoviews_gif.py and geoviews_tools.py
```


## How to run the scripts
1. Install the listed third-party modules.
2. Run `data_download.py` to obtain the data.
3. Run `data_prep.py` to obtain the preprocessed data.
4. Run all other scripts to obtain analysis result.
5. Change the paths and file names in the config_file.yaml to run geoviews_gif.py and geoviews_tools.py
6. To run the geoviews_gif.py:
```
python geoviews_gif.py --config config_file.yaml
```
7. To run the geoviews_tools.py:
```
python geoviews_tools.py --config config_file.yaml
```

## Third-Party Modules
- pandas
- numpy
- matplotlib
- seaborn
- geopandas
- geoviews
- os
- tqdm
- cv2
- warnings
- moviepy
- holoviews

They can be install by the following command:
`pip install -r requirements.txt`
