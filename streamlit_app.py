import streamlit as st
import pandas as pd
import plotly.express as px
from data_cleaning import clean_df

# Load and clean data
df = pd.read_csv('netflix_movies (1).csv')
df = clean_df(df)

# Title for the app
st.title("Netflix Content Overview")

# Dropdown filters for content type and year
content_type_options = df['type'].unique().tolist()
selected_content_types = st.multiselect('Select Content Type', content_type_options, default=content_type_options)
year_options = sorted(df['year_added'].dropna().unique().astype(int))
selected_years = st.multiselect('Select Year(s) Added', year_options, default=year_options)

# Filter data based on selections
filtered_df = df[(df['type'].isin(selected_content_types)) & (df['year_added'].isin(selected_years))]

# Group by year and content type, then count entries
content_count = filtered_df.groupby(['year_added', 'type']).size().reset_index(name="Count")

fig1 = px.bar(
    content_count, 
    x='year_added', 
    y='Count', 
    color='type', 
    barmode='group',  # use 'stack' for a stacked chart
    title="Content Count by Year and Type",
    labels={'year_added': 'Year Added', 'Count': 'Content Count', 'type': 'Content Type'},
    color_discrete_sequence=px.colors.qualitative.Pastel
)

st.plotly_chart(fig1)

st.subheader("Content made in India (including co-productions)")

# Filter for rows that contain 'India' in the 'country' column
india_filtered_df = filtered_df[filtered_df['country'].str.contains('India', na=False)]
india_content_count = india_filtered_df.groupby(['year_added', 'type']).size().reset_index(name="Count")

fig2 = px.bar(
    india_content_count, 
    x='year_added', 
    y='Count', 
    color='type', 
    barmode='group',  # 'stack' for a stacked chart
    title="Content made in India by Year and Type",
    labels={'year_added': 'Year Added', 'Count': 'Content Count', 'type': 'Content Type'},
    color_discrete_sequence=px.colors.qualitative.Vivid
)

st.plotly_chart(fig2)

# Pie chart for content with and without "India" in the country field
india_vs_non_india_count = pd.DataFrame({
    'Country Presence': ['Made in India', 'Made Abroad'],
    'Count': [india_filtered_df.shape[0], filtered_df.shape[0] - india_filtered_df.shape[0]]
})

fig3 = px.pie(
    india_vs_non_india_count, 
    names='Country Presence', 
    values='Count',
    title="Distribution of Content made in India and not made in India",
    color_discrete_sequence=px.colors.qualitative.Vivid
)

st.plotly_chart(fig3)