# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 16:17:47 2026

@author: Hamzat Abdulhafeez
"""

import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Dr. Afeez Kareem - Medicinal Chemist",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #2E86AB;
        border-bottom: 2px solid #2E86AB;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .contact-info {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .highlight-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2E86AB;
        margin: 1rem 0;
    }
    .stDataFrame {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("<h1 class='main-header'>Dr. Afeez Kareem - Medicinal chemist</h1>", unsafe_allow_html=True)

# Create tabs for navigation
tab1, tab2, tab3 = st.tabs(["👨‍🔬 Researcher Profile", "📚 Publications", "🧪 Chemical Database"])

# Chemical data (keeping only relevant data)
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

# Tab 1: Researcher Profile
with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(
            "https://cdn.pixabay.com/photo/2016/11/29/05/45/astronomy-1867616_1280.jpg",
            caption="Scientific Research"
        )
    
    with col2:
        st.markdown("<h2 class='section-header'>Researcher Profile</h2>", unsafe_allow_html=True)
        
        st.markdown("<div class='highlight-card'>", unsafe_allow_html=True)
        st.write("**Name:** Dr. Afeez Kareem")
        st.write("**Field of Research:** Medicinal Chemistry")
        st.write("**Institution:** University of Western Cape")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<h3 class='section-header'>Professional Experience</h3>", unsafe_allow_html=True)
        st.write("Postdoctoral Researcher at the University of the Western Cape specializing in drug design and chemical synthesis, with research interests spanning pharmaceutical sciences, teaching, and the development of novel therapeutic strategies for tuberculosis and Alzheimer's disease.")
        
        st.markdown("<h3 class='section-header'>Research Skills</h3>", unsafe_allow_html=True)
        st.write("• Proficient in the design, synthesis and characterization of small molecules for therapeutic applications")
        st.write("• Proficient in virtual screening methods for identifying potential small molecule inhibitors")
        st.write("• Proficient in culturing Mycobacterium smegmatis with appropriate growth media and aseptic techniques")
        st.write("• Conducted and optimized GSK3B enzyme assays to evaluate compound activity")

# Tab 2: Publications
with tab2:
    st.markdown("<h2 class='section-header'>Publications</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='highlight-card'>", unsafe_allow_html=True)
    st.write("**1.** Afeez I. Kareem, Erika Kapp, Jacques Joubert, Xiaoqin Zou (2025)")
    st.write("*Dual GSK3β/SIRT1 modulators for Alzheimer's: mechanisms, drug discovery and future perspectives*")
    st.write("Frontiers in Pharmacology. doi.org/10.3389/fphar.2025.1662241")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='highlight-card'>", unsafe_allow_html=True)
    st.write("**2.** Kareem, A.I., Malan, S.F., Erika K., Sean S., Joubert J. (2024)")
    st.write("*Synthesis, Characterization, and Biological Evaluation of Coumarin-Nitric Oxide Donor Hybrids as Anti-Tubercular Agents*")
    st.write("Eur. J. Med. Chem. Report. DOI: 10.1016/j.ejmcr.2024.100211")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='highlight-card'>", unsafe_allow_html=True)
    st.write("**3.** Akinleye, M. O., Okonkwo, N., Amaeze, O. U., Shonekan, O. O., Kareem, A. I., Eze, E., & Ukpo, G. E. (2023)")
    st.write("*Ruzu herbal bitters altered the pharmacokinetic profile of metformin tablets in healthy Nigerian volunteers following concurrent administration*")
    st.write("West African Journal of Pharmacy, 34(2), Article 2. doi.org/10.60787/wapcp-34-2-291")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='highlight-card'>", unsafe_allow_html=True)
    st.write("**4.** Kareem, A.I., Malan, S.F., Joubert, J. (2022)")
    st.write("*Radical Releasing Anti-Tuberculosis Agents and the Treatment of Mycobacterial Tuberculosis Infections - An Overview*")
    st.write("Mini Rev. in Med. Chem. DOI: 10.2174/1389557521666210219161045")
    st.markdown("</div>", unsafe_allow_html=True)

# Tab 3: Chemical Database
with tab3:
    st.markdown("<h2 class='section-header'>Chemical Database Explorer</h2>", unsafe_allow_html=True)
    
    # Search functionality
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search_term = st.text_input("🔍 Search by compound name or formula:", placeholder="e.g., Ethanol or C2H6O")
    
    # Filter functionality
    with col2:
        hazard_filter = st.selectbox("Filter by hazard class:", ["All", "Flammable", "Corrosive", "None"])
    
    # Apply filters
    filtered_data = chemical_data.copy()
    
    if search_term:
        filtered_data = filtered_data[
            filtered_data['Compound'].str.contains(search_term, case=False) | 
            filtered_data['Formula'].str.contains(search_term, case=False)
        ]
    
    if hazard_filter != "All":
        filtered_data = filtered_data[filtered_data['Hazard Class'] == hazard_filter]
    
    # Property filters
    st.markdown("<h3 class='section-header'>Filter by Properties</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        bp_range = st.slider(
            "Boiling Point Range (°C):",
            min_value=int(chemical_data['Boiling Point (°C)'].min()) - 10,
            max_value=int(chemical_data['Boiling Point (°C)'].max()) + 10,
            value=(0, 150)
        )
    
    with col2:
        mw_range = st.slider(
            "Molecular Weight Range (g/mol):",
            min_value=int(chemical_data['Molecular Weight (g/mol)'].min()) - 10,
            max_value=int(chemical_data['Molecular Weight (g/mol)'].max()) + 10,
            value=(0, 100)
        )
    
    # Apply property filters
    filtered_data = filtered_data[
        (filtered_data['Boiling Point (°C)'] >= bp_range[0]) &
        (filtered_data['Boiling Point (°C)'] <= bp_range[1]) &
        (filtered_data['Molecular Weight (g/mol)'] >= mw_range[0]) &
        (filtered_data['Molecular Weight (g/mol)'] <= mw_range[1])
    ]
    
    # Display results
    st.write(f"**Found {len(filtered_data)} compounds**")
    st.dataframe(filtered_data, use_container_width=True)
    
    # Quick stats
    if not filtered_data.empty:
        st.markdown("<h3 class='section-header'>Quick Statistics</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Average MW", f"{filtered_data['Molecular Weight (g/mol)'].mean():.2f} g/mol")
        
        with col2:
            st.metric("Average BP", f"{filtered_data['Boiling Point (°C)'].mean():.1f} °C")
        
        with col3:
            st.metric("Average Density", f"{filtered_data['Density (g/mL)'].mean():.3f} g/mL")

# Contact Section at bottom
st.markdown("---")
st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
st.markdown("<h3 class='section-header'>Contact Information</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.write("📧 **Email:** afeez.akcsv@outlook.com")
with col2:
    st.write("🏛️ **Institution:** University of Western Cape")
st.markdown("</div>", unsafe_allow_html=True)