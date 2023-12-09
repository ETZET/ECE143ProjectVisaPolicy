# ECE143ProjectVisaPolicy

## Introduction

Our final project for ECE143 @UCSD focused on gathering and analyzing data and statistics related to passport visa. Using primary data from https://www.passportindex.org/ and a few other sources, we hoped to answer the following questions regarding visas worldwide.

- Visa Generosity: Which countries are the most and least generous in terms of offering visa-free access and visa-free days?
- Correlation with Country Attributes: Do visa policies correlate with various country attributes, such as GDP, population, literacy rates, or skilled migration indices?
- Long-Term Trends: By analyzing historical data back to 2019, how have visa policies evolved over the years?
- COVID-19 Impact: How has the COVID-19 pandemic influenced visa policies? 
- Outliers in Visa Policies: Are there specific countries that deviate significantly from global trends in their visa policies?
- Reciprocity and Asymmetry: Is visa-free access always reciprocated between countries, or are there instances of one-way visa-free access? 

After analysis of the data, we came across interesting results such as developed nations being the most restrictive with their visa policies while having the most freedom to visit other countries, that visa policies have become more permissive over the years as terrorism drops, that COVID had no impact on visas themselves, and that 72% of countries have fully reciprocated visa policies with each other. We also created a tool to help visualize the visa data on an actual map.

The rest of this text covers how to reproduce our graphs and results.



## Setting up the environment
We use conda for all package management in this repository. To install all library dependencies, create the conda environment from `conda_env_generate_config.yml` using the following command (`ece143_grp6_env` is the name of the conda environment):

```
conda env create -f conda_env_generate_config.yml
conda activate ece143_grp6_env
```

## Config Files

- ```config_visualization.py``` :  change the paths in this config file for the visualization codes (geoviews_gif.py and geoviews_tools.py)

   - output_folder: path to the folder where all the results will be saved (if directory does not exist, it will be created automatically when you run the code)
   - video_name_outgoing: name of the video file for outgoing visa free travel animation (just the name, not the path)
   - video_name_incoming: name of the video file for incoming visa free travel animation (just the name, not the path)


- ```config_src.py``` :  The paths for running Terrorism, GDP and Covid Analysis is present in this file.


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
    python terrorism_GDP.py --config config/config_src.yaml
   ```

B) Covid Analysis:
1. Install the third party modules.
2. Download the COVID dataset from the below mentioned link and put it under the `data` folder.  (The file was too huge to be uploaded in the Repo) :
   https://drive.google.com/file/d/1gso0Zl5SMqhewanPa9PndkT79lsTZ7BS/view?usp=sharing
3. Save the downloaded file under the `data` folder, and save it with the same name with which it has been downloaded.
4. Run `covid.py` present under the `src` folder to obtain the results.
5. To run the file:
   ```
    python covid.py --config config/config_src.yaml
   ```


C) Visualization gif and interactive tool:

1. Change the paths and file names in the config_visualization.yaml (as defined above) to run geoviews_gif.py and geoviews_tools.py

2. To run the geoviews_gif.py:
```
python visualization/geoviews_gif.py --config config/config_visualization.yaml
```
3. To run the geoviews_tools.py:
```
python visualization/geoviews_tools.py --config config/config_visualization.yaml
```

## Final Visualization Notebook

The final visualization notebook is `visualization_final.ipynb` under the `visualization` folder. It contains all the visualizations generated for the presentation.
