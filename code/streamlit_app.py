import pandas as pd
import streamlit as st
import plotly.express as px
import geopandas as gpd
import folium
from streamlit_folium import folium_static

# Load salary data
@st.cache_data
def load_data():
    return pd.read_csv("cache/cleaned/salary_data.csv")

# Group data by state
@st.cache_data
def group_by_state(df):
    return df.groupby("state")["post_grad_earnings"].mean().reset_index()

# Load US States GeoJSON
@st.cache_data
def load_us_states():
    return gpd.read_file("https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json")

# Streamlit page setup
st.set_page_config(page_title="Tech Salary Explorer", layout="wide")
st.title("Tech Salary Explorer")
st.markdown("Explore tech-related post-graduation earnings across U.S. schools and majors.")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filter")
majors = sorted(df["major"].dropna().unique())
selected_major = st.sidebar.selectbox("Select Major:", ["All"] + majors)

# Filter data
filtered_df = df.copy()
if selected_major != "All":
    filtered_df = filtered_df[filtered_df["major"] == selected_major]

# Show table
st.subheader("📋 Filtered Salary Data")
st.dataframe(filtered_df)

# Bar chart
if not filtered_df.empty:
    st.subheader("Top 20 Schools by Post-Grad Earnings")
    fig = px.bar(
        filtered_df.sort_values("post_grad_earnings", ascending=False).head(20),
        x="post_grad_earnings",
        y="school",
        color="degree",
        orientation="h",
        labels={"post_grad_earnings": "Median Earnings ($)", "school": "School"},
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available for the selected filter.")

# Choropleth map (only if state column exists) -- takes a while to load
if "state" in df.columns:
    st.subheader("Average Tech Salary by State")

    states_avg = group_by_state(df)
    geo = load_us_states()
    merged = geo.merge(states_avg, left_on="name", right_on="state", how="left")

    m = folium.Map(location=[37.8, -96], zoom_start=4, tiles="cartodb positron")

    folium.Choropleth(
        geo_data=merged,
        name="choropleth",
        data=merged,
        columns=["state", "post_grad_earnings"],
        key_on="feature.properties.name",
        fill_color="YlGnBu",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Average Post-Grad Earnings ($)"
    ).add_to(m)

    folium_static(m)
