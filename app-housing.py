import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('California Housing Data (1990) by [Zhiqian Zhang]')

df = pd.read_csv('housing.csv')

# Slider: minimal median house value
min_house_value = st.slider('Minimal Median House Value', 0, 500001, 200000)

st.subheader('See more filters in the sidebar:')

# Sidebar: multiselect to filter by location type (options come from the full dataset)
location_types = df.ocean_proximity.unique()
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    location_types,
    location_types,
)

# Sidebar: radio button to filter by income level
income_level = st.sidebar.radio('Choose income level', ('Low', 'Medium', 'High'))

# Apply the filters
df = df[df.median_house_value >= min_house_value]
df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:  # High
    df = df[df.median_income >= 4.5]

# Map of the filtered districts
st.map(df)

# Histogram of median house value (30 bins)
st.subheader('Histogram of Median House Value')
fig, ax = plt.subplots()
ax.hist(df.median_house_value, bins=30)
st.pyplot(fig)
