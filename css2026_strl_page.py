# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:53:15 2026

@author: Hamzat Abdulhafeez
"""

import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
chemical_data = pd.DataFrame({
    'Compound': ['Acetone', 'Ethanol', 'Water', 'Benzene', 'Toluene', 'Acetic Acid', 'Methanol', 'Hexane'],
    'Formula': ['C3H6O', 'C2H6O', 'H2O', 'C6H6', 'C7H8', 'C2H4O2', 'CH4O', 'C6H14'],
    'Molecular Weight (g/mol)': [58.08, 46.07, 18.02, 78.11, 92.14, 60.05, 32.04, 86.18],
    'Density (g/mL)': [0.791, 0.789, 1.000, 0.877, 0.867, 1.049, 0.792, 0.655],
    'Boiling Point (°C)': [56.1, 78.4, 100.0, 80.1, 110.6, 118.1, 64.7, 68.7],
    'Melting Point (°C)': [-94.7, -114.1, 0.0, 5.5, -95.0, 16.6, -97.6, -95.3],
    'CAS Number': ['67-64-1', '64-17-5', '7732-18-5', '71-43-2', '108-88-3', '64-19-7', '67-56-1', '110-54-3'],
    'Hazard Class': ['Flammable', 'Flammable', 'None', 'Flammable', 'Flammable', 'Corrosive', 'Flammable', 'Flammable']
})


# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Afeez Kareem"
    field = "Chemistry"
    institution = "University of Western Cape"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
        "https://images.unsplash.com/photo-1602052577122-f73b9710adba?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        caption="Nature (Pixabay)"
    )

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("Chemical Database")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Chemical database"]
    )
    
    # ALL THE FOLLOWING CODE MUST BE INDENTED TO BE INSIDE THIS ELIF BLOCK
    
    st.dataframe(chemical_data, use_container_width=True)

    st.subheader("Search Chemicals")
    search_term = st.text_input("Search by name or formula:")
    if search_term:
        filtered = chemical_data[chemical_data['Compound'].str.contains(search_term, case=False) | 
                                chemical_data['Formula'].str.contains(search_term, case=False)]
        st.dataframe(filtered)
    else:
        st.dataframe(chemical_data)

    # Interactive filtering
    st.subheader("Filter by Properties")
    col1, col2 = st.columns(2)
    with col1:
        min_bp = st.slider("Minimum Boiling Point (°C)", -120, 300, 0)
        max_bp = st.slider("Maximum Boiling Point (°C)", -120, 300, 200)
    with col2:
        min_mw = st.slider("Minimum Molecular Weight", 0, 500, 0)
        max_mw = st.slider("Maximum Molecular Weight", 0, 500, 200)

    filtered_data = chemical_data[
        (chemical_data['Boiling Point (°C)'] >= min_bp) &
        (chemical_data['Boiling Point (°C)'] <= max_bp) &
        (chemical_data['Molecular Weight (g/mol)'] >= min_mw) &
        (chemical_data['Molecular Weight (g/mol)'] <= max_mw)
    ]

    st.write(f"Found {len(filtered_data)} compounds")
    st.dataframe(filtered_data)

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "afeez.ak@outlook.com"
    st.write(f"You can reach me at {email}.")