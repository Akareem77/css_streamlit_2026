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
    st.subheader("Professional experience")
    st.write("Postdoctoral Researcher at the University of the Western Cape specializing in drug design and chemical synthesis, with research interests spanning pharmaceutical sciences, teaching, and the development of novel therapeutic strategies for tuberculosis and Alzheimer’s disease.")
    st.subheader("Research Skills")
    st.write("•	Proficient in the design, synthesis and characterization of small molecules for therapeutic applications in diseases treatment.")
    st.write("•	Proficient in virtual screening methods for identifying potential small molecule inhibitors from compound libraries.")
    st.write("•	Proficient in culturing Mycobacterium smegmatis, including knowledge of appropriate growth media, incubation conditions, and aseptic techniques")
    st.write("•	Conducted and optimized GSK3B enzyme assays to evaluate compound activity, utilizing kinase activity assays to assess ATP consumption and substrate phosphorylation.")
    

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")
    #Publications
    st.write("•	Afeez I. Kareem, Erika Kapp, Jacques Joubert1Xiaoqin Zou, (2025) Dual GSK3β/SIRT1 modulators for Alzheimer’s: mechanisms, drug discovery and future perspectives. Frontiers in Pharmacology. doi.org/10.3389/fphar.2025.1662241")
    st.write("•	Kareem, A.I., Malan, S.F., Erika K., Sean S., Joubert J. (2024). Synthesis, Characterization, and Biological Evaluation of Coumarin-Nitric Oxide Donor Hybrids as Anti-Tubercular Agents. Eur. J. Med. Chem. Report. DOI: 10.1016/j.ejmcr.2024.100211")
    st.write("• Akinleye, M. O., Okonkwo, N., Amaeze, O. U., Shonekan, O. O., Kareem, A. I., Eze, E., & Ukpo, G. E. (2023). Ruzu herbal bitters altered the pharmacokinetic profile of metformin tablets in healthy Nigerian volunteers following concurrent administration. West African Journal of Pharmacy, 34(2), Article 2. doi.org/10.60787/wapcp-34-2-291")
    st.write("• Kareem, A.I., Malan, S.F., Joubert, J. (2022). Radical Releasing Anti-Tuberculosis Agents and the Treatment of Mycobacterial Tuberculosis Infections - An Overview. Mini Rev. in Med. Chem. DOI: 10.2174/1389557521666210219161045")
    
       
    
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
    email = "afeez.akcsv@outlook.com"
    st.write(f"You can reach me at {email}.")