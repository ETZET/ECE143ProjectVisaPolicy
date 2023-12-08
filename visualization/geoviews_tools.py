import pandas as pd
import geopandas as gpd
import geoviews as gv
import matplotlib.pyplot as plt
import pickle as pkl
import numpy as np
import os
from tqdm import tqdm
from collections import defaultdict
from moviepy.editor import VideoFileClip
import numpy as np
import holoviews as hv
import yaml
import argparse

hv.extension('bokeh')
gv.extension('bokeh', 'matplotlib')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config_file.yaml")
    args = parser.parse_args()

    config_file = args.config
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    output_folder = os.path.join(config["output_folder"], "tools/")

    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    subdirs = ['2020-11-19', '2021-12-14', '2022-12-21', '2023-10-11']
    legacy_dir = os.path.join(config["legacy_data_path"], "legacy/")
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    world_year_data = gpd.GeoDataFrame(columns=['name', 'continent', 'iso_a3', 'geometry', 'pop_est', 'gdp_md_est', 
                                                    'visa_incoming', 'visa_outgoing', 'date'], geometry='geometry')


    for subdir in tqdm(subdirs):
        date = subdir
        csv_path = os.path.join(legacy_dir, subdir, 'passport-index-matrix-iso3.csv')

        if not os.path.exists(csv_path): 
            continue
        passport_data = pd.read_csv(csv_path)
        country_outgoing = defaultdict(int)
        country_incoming = defaultdict(int)

        for i in passport_data.values:
            coun = i[0]
            country_outgoing[coun] = 0
            for j in range(1, len(i)):
                if i[j] =="visa on arrival" or i[j] =="visa free" or str(i[j]).isdigit():
                    country_outgoing[coun] += 1

        country_visa_outgoing = dict(sorted(country_outgoing.items(), key=lambda item: item[1], reverse= True))

        for column in passport_data.columns:
            if column == 'Passport':
                continue
            coun = column
            for visa_type in passport_data[coun]:
                if visa_type =="visa on arrival" or visa_type =="visa free" or str(visa_type).isdigit():
                    country_incoming[coun] += 1

        country_visa_incoming = dict(sorted(country_incoming.items(), key=lambda item: item[1], reverse= True))
        
        
        for country, visa_count in country_visa_outgoing.items():
            if country in world['iso_a3'].values:
                country_data = world[world['iso_a3'] == country]

                if len(country_data) == 0:
                    continue
                
                country_data['visa_outgoing'] = visa_count
                if country not in country_visa_incoming:
                    country_visa_incoming[country] = 0
                country_data['visa_incoming'] = country_visa_incoming[country]
                country_data['date'] = date
                world_year_data = world_year_data.append(country_data)
        
    world_year_data_reset = world_year_data.reset_index(drop=True)

    outgoing_grouped = gv.Polygons(world_year_data_reset, vdims=['visa_outgoing', 'continent', 'date', 'name'], label = 'Outgoing visa free travel: ').groupby(['date', 'continent'])
    incoming_grouped = gv.Polygons(world_year_data_reset, vdims=['visa_incoming', 'continent', 'date', 'name'], label = 'Incoming visa free travel: ').groupby(['date', 'continent'])

    outgoing_tool_html = outgoing_grouped.opts(width=1300, height=850, tools=['hover'], cmap = "plasma", infer_projection=True)
    incoming_tool_html = incoming_grouped.opts(width=1300, height=850, tools=['hover'], cmap = "plasma", infer_projection=True)


    outgoing_tool_path = os.path.join(output_folder, 'outgoing_tool.html')
    incoming_tool_path = os.path.join(output_folder, 'incoming_tool.html')

    hv.save(outgoing_tool_html, outgoing_tool_path)
    hv.save(incoming_tool_html, incoming_tool_path)

if __name__ == "__main__":
    main()