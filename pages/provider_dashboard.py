import streamlit as st
import time

st.set_page_config(page_title="QuitTo - Provider Dashboard", page_icon="💚", layout="wide")

# Get the newly registered patient from session state, or use a default if opened directly
new_patient_name = st.session_state.get('patient_name', 'Raj Kapur')
new_patient_addiction = st.session_state.get('patient_addiction', 'Smoking')
new_patient_usage = st.session_state.get('patient_usage', '10')

# Combined Patient List (Dynamic + Static Mock Data)
patients = [
    {"name": new_patient_name, "type": new_patient_addiction, "week": "Week 1/12", "usage": f"{new_patient_usage} units/day"},
    {"name": "Rahul Sharma", "type": "Smoking", "week": "Week 4/12", "usage": "7 units/day"},
    {"name": "Priya Patel", "type": "Chewing Tobacco", "week": "Week 6/12", "usage": "4 units/day"}
]

patient_names = [p["name"] for p in patients]

# --- 1. RECORD CO READING DIALOG ---
@st.dialog("Record CO Reading")
def show_co_dialog(default_name):
    st.write("Add a new Carbon Monoxide meter reading for the patient")
    default_idx = patient_names.index(default_name) if default_name in patient_names else 0
    
    st.selectbox("Select Patient", options=patient_names, index=default_idx)
    st.text_input("CO Reading (ppm)", placeholder="e.g., 15")
    st.text_area("Notes (optional)", placeholder="Any additional observations...")
    
    st.markdown("""
        <style>
        .save-co-btn div.stButton > button { background: linear-gradient(90deg, #1A56DB 0%, #3B82F6 100%) !important; color: white !important; border-radius: 8px; font-weight: 600; width: 100%; border: none; }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="save-co-btn">', unsafe_allow_html=True)
    if st.button("💾 Save Reading", use_container_width=True):
        st.success("CO Reading saved successfully!")
        time.sleep(1)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. RECORD CASE HISTORY DIALOG ---
@st.dialog("Record Case History")
def show_history_dialog(default_name):
    st.write("Add detailed case history for the patient")
    default_idx = patient_names.index(default_name) if default_name in patient_names else 0
    
    st.selectbox("Select Patient", options=patient_names, index=default_idx)
    st.text_area("Diagnosis *", placeholder="Enter diagnosis details...")
    st.text_area("Treatment Plan *", placeholder="Enter treatment plan...")
    st.text_area("Additional Notes", placeholder="Any additional information...")
    
    st.markdown("""
        <style>
        .save-hist-btn div.stButton > button { background: linear-gradient(90deg, #7E22CE 0%, #9333EA 100%) !important; color: white !important; border-radius: 8px; font-weight: 600; width: 100%; border: none; }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="save-hist-btn">', unsafe_allow_html=True)
    if st.button("📋 Save Case History", use_container_width=True):
        st.success("Case history saved successfully!")
        time.sleep(1)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. MAIN PAGE STYLES ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    .stApp { background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 40%); font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 2rem !important; max-width: 1100px; }
    #MainMenu, footer {visibility: hidden;}

    .dash-header { font-size: 2.2rem; font-weight: 800; margin-bottom: 5px; }
    .dash-subtext { color: #6B7280; font-size: 1rem; margin-bottom: 30px; }

    /* Top Cards Styling */
    .metric-card { border-radius: 12px; padding: 25px; height: 100%; border: 1px solid rgba(229,231,235,0.6); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); }
    .card-blue { background-color: #EBF8FF; }
    .card-green { background-color: #F0FDF4; }
    .card-purple { background-color: #FAF5FF; }
    
    .card-title { font-size: 0.95rem; font-weight: 600; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }
    .card-blue .card-title { color: #1A56DB; }
    .card-green .card-title { color: #059669; }
    .card-purple .card-title { color: #7E22CE; }
    
    .card-value { font-size: 2.5rem; font-weight: 800; }
    .card-blue .card-value { color: #1A56DB; }
    .card-green .card-value { color: #059669; }
    .card-purple .card-value { color: #9333EA; }

    /* Fake Tabs Menu */
    .fake-tabs { display: flex; justify-content: space-between; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; color: #6B7280; font-weight: 600; font-size: 0.95rem; }
    .fake-tab-active { color: #111827; border-bottom: 3px solid #1A56DB; padding-bottom: 8px; margin-bottom: -12px; }

    /* Patient Card */
    .patient-card { background: white; border-radius: 12px; padding: 20px; border: 1px solid #E2E8F0; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); display: flex; align-items: center; justify-content: space-between; }
    .patient-name { font-size: 1.1rem; font-weight: 700; color: #1E293B; margin-bottom: 4px; }
    .patient-details { font-size: 0.85rem; color: #6B7280; }
    
    .action-btn div.stButton > button { background: #F8FAFC !important; color: #4B5563 !important; border: 1px solid #E2E8F0 !important; font-weight: 600; border-radius: 6px; }
    .action-btn div.stButton > button:hover { background: #F1F5F9 !important; border-color: #CBD5E1 !important; color: #0F172A !important; }
    </style>
""", unsafe_allow_html=True)

# Top Bar
col_head, col_btn = st.columns([4, 1])
with col_head:
    st.markdown('<div class="dash-header"><span style="color: #059669;">Healthcare Provider</span> <span style="color: #1A56DB;">Dashboard</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="dash-subtext">Monitor and support your patients\' recovery</div>', unsafe_allow_html=True)
with col_btn:
    st.markdown('<div style="text-align: right; margin-top: 10px;">', unsafe_allow_html=True)
    if st.button("🚪 Logout"): 
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Top Metrics Cards
c1, c2, c3 = st.columns(3)
with c1: 
    st.markdown(f'<div class="metric-card card-blue"><div class="card-title">👥 Total Patients</div><div class="card-value">{len(patients)}</div></div>', unsafe_allow_html=True)
with c2: 
    st.markdown('<div class="metric-card card-green"><div class="card-title">📉 CO Readings Recorded</div><div class="card-value">0</div></div>', unsafe_allow_html=True)
with c3: 
    st.markdown('<div class="metric-card card-purple"><div class="card-title">📄 Case Histories</div><div class="card-value">0</div></div>', unsafe_allow_html=True)

# Fake Navigation Tabs (Visual only to match Figma)
st.markdown("""
    <div class="fake-tabs">
        <div class="fake-tab-active">Patients</div>
        <div>CO Readings</div>
        <div>Case History</div>
        <div>Daily Tasks</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div style="color: #1A56DB; font-weight: 700; font-size: 1.1rem; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">👥 Patient List</div>', unsafe_allow_html=True)

# Generate the Patient List dynamically
for p in patients:
    with st.container():
        # Using Streamlit columns to layout the card exactly like Figma
        st.markdown(f"""
            <div style="background: white; border-radius: 12px 12px 0 0; padding: 20px 20px 0 20px; border: 1px solid #E2E8F0; border-bottom: none;">
                <div class="patient-name">{p['name']}</div>
                <div class="patient-details">Type: {p['type']} | {p['week']}<br>Current usage: {p['usage']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Action Buttons Row
        st.markdown('<div style="background: white; border-radius: 0 0 12px 12px; padding: 10px 20px 20px 20px; border: 1px solid #E2E8F0; border-top: none; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">', unsafe_allow_html=True)
        btn_col1, btn_col2, empty_col = st.columns([1.5, 1.5, 3])
        
        with btn_col1:
            st.markdown('<div class="action-btn">', unsafe_allow_html=True)
            if st.button("Add CO Reading", key=f"co_{p['name']}", use_container_width=True):
                show_co_dialog(p['name'])
            st.markdown('</div>', unsafe_allow_html=True)
            
        with btn_col2:
            st.markdown('<div class="action-btn">', unsafe_allow_html=True)
            if st.button("Add Case History", key=f"hist_{p['name']}", use_container_width=True):
                show_history_dialog(p['name'])
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
