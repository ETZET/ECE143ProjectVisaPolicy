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

A) Terrorism and GDP Analysis:
1. Install the third party modules.
2. All the required data is already present under the `data` folder.
3. Run `terrorism-GDP.py` present under the `src` folder to obtain the results.
4. To run the file:
   ```
    python src/terrorism_GDP.py --config config/config_src.yaml
   ```

B) Covid Analysis:
1. Install the third party modules.
2. Download the COVID dataset from the below mentioned link and put it under the `data` folder.  (The file was too huge to be uploaded in the Repo) :
   https://drive.google.com/file/d/1gso0Zl5SMqhewanPa9PndkT79lsTZ7BS/view?usp=sharing
3. Save the downloaded file under the `data` folder, and save it with the same name with which it has been downloaded.
4. Run `covid.py` present under the `src` folder to obtain the results.
5. To run the file:
   ```
    python src/covid.py --config config/config_src.yaml
   ```


C) Siddharth:
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

D) Data Downloading Preprocessing and EDA:
1. Install the listed third-party modules.
2. Run `data_download.py` to obtain the data.
3. Run `data_prep.py` to obtain the preprocessed data.
4. Run `eda.py` to generate all figures for explorative data anaysis
5. Reference viusalization and the slide to review all figures generated
from eda.py

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
- yaml
- argparser

They can be install by the following command:
`pip install -r requirements.txt`


Reference:
- **Main Data Source:** [Passport Index](https://www.passportindex.org)
  - Contains comprehensive data for visa policy for 199 countries

- **Auxiliary Data Source 1:** [Countries of the World](https://www.kaggle.com/datasets/fernandol/countries-of-the-world)
  - Contains data for basic information for countries, such as population, GDP, literacy.

- **Auxiliary Data Source 2:** [World Freedom Index](https://www.kaggle.com/datasets/sujaykapadnis/world-freedom-index)
  - Contains data for global political rights and civil liberties statistics for 195 countries

- **Auxiliary Data Source 3:** [Global Terrorism Index 2023](https://www.kaggle.com/datasets/ddosad/global-terrorism-index-2023)
  - Contains data for terrorism activities, such as terrorism rank, number of incidents, fatalities…