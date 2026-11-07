# ==========================================
# CRIME HOTSPOT FINDER
# STREAMLIT DASHBOARD
# ==========================================

import streamlit as st
import pandas as pd
from pathlib import Path
import streamlit.components.v1 as components


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Crime Hotspot Finder",
    page_icon="📍",
    layout="wide"
)


# ==========================================
# PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
OUT_DIR = BASE_DIR / "outputs"

RESULTS_PATH = OUT_DIR / "dbscan_crime_results.csv"
HOTSPOT_PATH = OUT_DIR / "hotspot_summary.csv"
EVALUATION_PATH = OUT_DIR / "dbscan_evaluation_report.csv"
SENSITIVITY_PATH = OUT_DIR / "parameter_sensitivity.csv"
ROC_PATH = OUT_DIR / "roc_curve.png"
MAP_PATH = OUT_DIR / "maps" / "crime_hotspot_map.html"


# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():
    results = pd.read_csv(RESULTS_PATH)
    hotspots = pd.read_csv(HOTSPOT_PATH)
    evaluation = pd.read_csv(EVALUATION_PATH)
    return results, hotspots, evaluation


try:
    crime_data, hotspots, evaluation = load_data()

except FileNotFoundError as error:
    st.error(f"Required file not found: {error}")
    st.stop()


# ==========================================
# DASHBOARD HEADER
# ==========================================

st.title("📍 Crime Hotspot Finder")

st.subheader("Karachi Crime Analysis using DBSCAN")

st.write(
    "An interactive dashboard for geographical "
    "crime pattern analysis and hotspot detection."
)

st.info(
    "Dataset: Karachi Synthetic Crime Dataset (Kaggle, 2020-2025). "
    "The data is synthetic and locations are subdivision-level, so hotspots "
    "are area-level indicators and not real police records."
)

st.divider()


# ==========================================
# KEY STATISTICS
# ==========================================

total_records = len(crime_data)

total_clusters = crime_data.loc[
    crime_data["CLUSTER"] != -1, "CLUSTER"
].nunique()

noise_records = (crime_data["CLUSTER"] == -1).sum()

noise_percentage = (
    noise_records / total_records * 100
    if total_records > 0 else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", f"{total_records:,}")
col2.metric("Detected Hotspots", total_clusters)
col3.metric("Noise Records", f"{noise_records:,}")
col4.metric("Noise Percentage", f"{noise_percentage:.2f}%")

st.divider()


# ==========================================
# HOTSPOT ANALYSIS
# ==========================================

st.header("Crime Hotspot Analysis")

if not hotspots.empty:

    top_hotspots = hotspots.head(10)

    st.subheader("Top Crime Hotspots")
    st.bar_chart(top_hotspots.set_index("CLUSTER")["Crime_Records"])

    st.subheader("Hotspot Details")
    st.dataframe(top_hotspots)

else:
    st.info("No hotspots available.")

st.divider()


# ==========================================
# INTERACTIVE CRIME MAP
# ==========================================

st.header("Geographical Crime Map")

if MAP_PATH.exists():

    if hasattr(st, "iframe"):
        # Newer Streamlit versions
        st.iframe(MAP_PATH, height=600)
    else:
        # Older Streamlit versions
        with open(MAP_PATH, "r", encoding="utf-8") as file:
            map_html = file.read()
        components.html(map_html, height=600, scrolling=True)

else:
    st.warning("Crime map file not found.")

st.divider()


# ==========================================
# MODEL EVALUATION
# ==========================================

st.header("DBSCAN Model Evaluation")

st.dataframe(evaluation, hide_index=True)

st.caption(
    "Silhouette is low because DBSCAN clusters are density-based and "
    "touch each other. The hotspots are therefore validated with ROC/AUC below."
)

st.divider()


# ==========================================
# ROC CURVE AND AUC
# ==========================================

st.header("ROC Curve and AUC Validation")

st.write(
    "DBSCAN is unsupervised, so it has no labels. To validate it, hotspots "
    "found on 2020-2023 data are compared with the high-crime locations "
    "(top 25%) of 2024-2025."
)

if ROC_PATH.exists():
    st.image(str(ROC_PATH))
else:
    st.warning("ROC curve image not found.")

if SENSITIVITY_PATH.exists():
    st.subheader("eps and min_samples Sensitivity")
    st.dataframe(pd.read_csv(SENSITIVITY_PATH), hide_index=True)

st.divider()


# ==========================================
# DATASET PREVIEW
# ==========================================

st.header("Crime Dataset Preview")

st.dataframe(crime_data.head(100))


# ==========================================
# DOWNLOAD RESULTS
# ==========================================

st.header("Download Analysis Results")

csv_data = crime_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download DBSCAN Results",
    data=csv_data,
    file_name="dbscan_crime_results.csv",
    mime="text/csv"
)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption("Crime Hotspot Finder | Data Science Project | DBSCAN")