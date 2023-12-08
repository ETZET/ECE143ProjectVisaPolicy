import pandas as pd
import geoviews as gv
import os
from collections import defaultdict
import warnings
import yaml
from utils import plot_choropleth_maps, make_gif
import argparse

gv.extension('bokeh', 'matplotlib')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config_file.yaml")
    args = parser.parse_args()

    config_file = args.config
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    legacy_dir = os.path.join(config["legacy_data_path"], "legacy/")
    images_folder_outgoing = os.path.join(config["output_folder"], "images/outgoing")
    images_folder_incoming = os.path.join(config["output_folder"], "images/incoming")
    video_folder = os.path.join(config["output_folder"], "final_videos")

    if not os.path.isdir(images_folder_outgoing):
        os.makedirs(images_folder_outgoing)
    if not os.path.isdir(images_folder_incoming):
        os.makedirs(images_folder_incoming)
    if not os.path.isdir(video_folder):
        os.makedirs(video_folder)

    subdirs_1 = [f.path.split('/')[-1] for f in os.scandir(legacy_dir) if f.is_dir() ]
    subdirs_1.sort()

    warnings.filterwarnings('ignore')

    for subdir in subdirs_1[6:]:
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
        plot_choropleth_maps(country_visa_outgoing, subdir, images_folder_outgoing)

        for column in passport_data.columns:
            if column == 'Passport':
                continue
            coun = column
            for visa_type in passport_data[coun]:
                if visa_type =="visa on arrival" or visa_type =="visa free" or str(visa_type).isdigit():
                    country_incoming[coun] += 1

        country_visa_incoming = dict(sorted(country_incoming.items(), key=lambda item: item[1], reverse= True))
        plot_choropleth_maps(country_visa_incoming, subdir, images_folder_incoming)

    make_gif(images_folder_outgoing, subdirs_1, config["video_name_outgoing"], video_folder)
    make_gif(images_folder_incoming, subdirs_1, config["video_name_incoming"], video_folder)

if __name__ == "__main__":
    main()

