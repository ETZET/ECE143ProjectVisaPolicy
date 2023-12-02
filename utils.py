import geopandas as gpd
import geoviews as gv
import os
import cv2
from tqdm import tqdm
from moviepy.editor import VideoFileClip
import pandas as pd
import numpy as np


FPS = 5

def plot_choropleth_maps(country_visa, subdir, plot_folder):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    world['visa_count'] = world['iso_a3'].map(country_visa)
    world['visa_count'] = pd.to_numeric(world['visa_count'], errors='coerce').fillna(0).astype(np.int64)

    plot_title = 'Number of Free Visa entries (' + subdir + ')'
    plot1 = gv.Polygons(world, vdims=['visa_count', 'name'], label=plot_title).opts(
    color='pop_est', cmap='plasma', colorbar=True, xaxis=None, yaxis=None, toolbar='above', width=1000, height=700, tools=['hover']
    )

    plot_filename = os.path.join(plot_folder, subdir + '.png')
    gv.save(plot1, plot_filename, dpi=600)


def make_gif(image_folder, subdirs_1, video_name, video_folder):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape
    video_path = os.path.join(video_folder, video_name)
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'MP4V'), FPS, (width,height))
    for subdir in tqdm(subdirs_1):
        img_path = os.path.join(image_folder, subdir + '.png')
        if not os.path.exists(img_path): 
            continue
        # print(img_path)
        img = cv2.imread(img_path)
        video.write(img)

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()

    videoClip = VideoFileClip(video_path)
    gif_name = video_name.split('.')[0]
    videoClip.write_gif(os.path.join(video_folder, gif_name + '.gif'), fps=FPS)