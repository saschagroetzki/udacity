# Udacity Project 1 | Writing a Data Scientist Blog Post
Repository to store the relvant files for the Udacity Project: Writing a Data Scientist Blog Post

# Table of contents
1. [Installation](#installation)
2. [Motivation](#motivation)
3. [File Description](#file-description)
4. [Results](#results)
5. [References](#references)


# Installation <a name='installation'></a>
Use the `requirements.txt` to install all the necessary libraries based on Python 3.x.

# Motivation <a name='motivation'></a>
I used a dataset with information about Airbnb activities in Seattle provided on Kaggle (https://www.kaggle.com/datasets/airbnb/seattle/data) to answer the following questions:
1) Which property types are available?
2) How is the price per accomodate distributed? 
3) Are there price fluctuation over the year?
4) Can a linear regression model be used to model the price per accomodate? 

# File Description <a name='file-description'></a>
The data analysis is shown in the jupyter notebook `main.ipynb`. Additional functions are implemented in the file `utils.py`.
<br>
To be able to embed Plolty Charts on Medium a Ploly Chart account is necessary. <br>
The credentials are saved in a `config.yaml` file.

# Results <a name='results'></a>
The main findings can be found in this [Medium post](https://medium.com/@s.groetzki/analysing-an-airbnb-dataset-for-seattle-7375f9c87831).

# References <a name='references'></a>
The data used can be found on Kaggle, see the link above. <br>
Besides this I enriched the dataset through geographic data <br>
https://github.com/OpenDataDE/State-zip-code-GeoJSON/tree/master <br> 
Download the file `wa_washington_zip_codes_geo.min.json` and save it in the `/data` folder:

In addition, I found some inspiration on this blogpost: <br>
https://medium.com/@felix.dulys/data-driven-neighborhood-hunting-in-seattle-a-how-to-guide-in-python-d2c899a037ab <br>

Further, here is a medium post that describes how to embed interactive plotly figures on medium: <br>
https://jennifer-banks8585.medium.com/how-to-embed-interactive-plotly-visualizations-on-medium-blogs-710209f93bd