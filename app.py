# app.py

import streamlit as st
import pandas as pd
import sqlite3

# Function to load data from SQLite database
def load_data():
    conn = sqlite3.connect('students.db')  # Database name is specified here
    query = "SELECT * FROM students"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit app layout
st.title('Student Performance Visualization')

# Load data
data = load_data()

# Sidebar for filtering
st.sidebar.header('Filter Options')
selected_grade = st.sidebar.selectbox('Select Grade', data['grade'].unique())

# Filter data based on selected grade
filtered_data = data[data['grade'] == selected_grade]

# Display filtered data
st.write(filtered_data)

# Create visualizations
st.subheader('Performance Metrics')
st.bar_chart(filtered_data['performance_score'])