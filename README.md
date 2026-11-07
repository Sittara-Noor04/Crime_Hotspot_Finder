\# Crime Hotspot Finder Using DBSCAN



\## Project Overview

Crime Hotspot Finder is a Data Science project that uses the DBSCAN clustering algorithm to identify spatial clusters in a synthetic Karachi crime dataset.



The project analyzes geographical coordinates (latitude and longitude) to identify candidate hotspot areas and visualize their distribution on an interactive map.



\*\*Note:\*\* The dataset is synthetic. Therefore, the detected clusters are analytical results from simulated data and should not be interpreted as verified real-world crime hotspots.



\## Objectives

\- Explore and clean crime-related geographical data.

\- Apply DBSCAN clustering to location coordinates.

\- Identify clusters and noise points.

\- Evaluate clustering results.

\- Visualize spatial patterns using interactive maps.

\- Present findings through a Streamlit dashboard.



\## Technologies Used

\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Folium

\- Streamlit

\- Jupyter Notebook



\## Project Structure

```text

Crime\_Hotspot\_Finder/

├── app.py

├── requirements.txt

├── .gitignore

├── data/

│   └── raw/

├── note\_books/

│   └── data.ipynb

└── outputs/

&#x20;   ├── dbscan\_crime\_results.csv

&#x20;   ├── dbscan\_evaluation\_report.csv

&#x20;   ├── hotspot\_summary.csv

&#x20;   ├── parameter\_sensitivity.csv

&#x20;   ├── roc\_curve.png

&#x20;   └── maps/

&#x20;       ├── crime\_heatmap.html

&#x20;       └── crime\_hotspot\_map.html

```



\## Installation



Install the required libraries:



```bash

pip install -r requirements.txt

```



\## Run the Streamlit Dashboard



```bash

streamlit run app.py

```



\## Dataset

The project uses the Kaggle Karachi Synthetic Crime Dataset (2020–2025).



\## Algorithm

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is used to group geographically close data points and identify noise points.



\## Project Status

Data preprocessing, exploratory data analysis, DBSCAN clustering, evaluation, map visualization, and Streamlit dashboard development have been completed.



\## Disclaimer

This project is for academic and educational purposes. Results are based on synthetic data and do not represent verified crime statistics or actual public safety conditions in Karachi.

