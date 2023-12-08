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

## Config Files

- ```config_visualization.py``` :  change the paths in this config file for the visualization codes (geoviews_gif.py and geoviews_tools.py)

   - output_folder: path to the folder where all the results will be saved (if directory does not exist, it will be created automatically when you run the code)
   - video_name_outgoing: name of the video file for outgoing visa free travel animation (just the name, not the path)
   - video_name_incoming: name of the video file for incoming visa free travel animation (just the name, not the path)

- ```config_visualization.py``` : (Jaya)

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
python geoviews_gif.py --config config_visualization.yaml
```
3. To run the geoviews_tools.py:
```
python geoviews_tools.py --config config_visualization.yaml
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
- yaml
- argparser

They can be install by the following command:
`pip install -r requirements.txt`
