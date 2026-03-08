import streamlit as st
import time

st.set_page_config(page_title="QuitTo - Provider Dashboard", page_icon="💚", layout="wide")

# Get the newly registered patient from session state, or use a default
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

# Initialize dynamic tasks in session state if they don't exist yet
if 'patient_tasks' not in st.session_state:
    st.session_state.patient_tasks = {
        new_patient_name: [
            "Take a 5-minute walk", 
            "Drink 2L of water", 
            "Practice deep breathing for 5 minutes", 
            "Eat a healthy breakfast", 
            "Avoid triggers (identify and note them)"
        ],
        "Rahul Sharma": ["Chew sugar-free gum when craving hits", "Drink 2L of water", "10-minute meditation"],
        "Priya Patel": ["Keep mouth busy with mints", "Avoid friends who chew tobacco today"]
    }

# --- 1. RECORD CO READING DIALOG ---
@st.dialog("Record CO Reading")
def show_co_dialog(default_name=None):
    st.write("Add a new Carbon Monoxide meter reading for the patient")
    default_idx = patient_names.index(default_name) if default_name in patient_names else 0
    
    st.selectbox("Select Patient", options=patient_names, index=default_idx, key="co_select")
    st.text_input("CO Reading (ppm)", placeholder="e.g., 15")
    st.text_area("Notes (optional)", placeholder="Any additional observations...")
    
    st.markdown("""
        <style>
        .save-co-btn div.stButton > button { background: linear-gradient(90deg, #059669 0%, #1A56DB 100%) !important; color: white !important; border-radius: 8px; font-weight: 600; width: 100%; border: none; transition: 0.3s; }
        .save-co-btn div.stButton > button:hover { box-shadow: 0 4px 12px rgba(5, 150, 105, 0.4); }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="save-co-btn">', unsafe_allow_html=True)
    if st.button("💾 Save Reading", use_container_width=True):
        st.success("CO Reading saved successfully!")
        time.sleep(1)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. RECORD CASE HISTORY DIALOG ---
@st.dialog("Record Case History", width="large")
def show_history_dialog(default_name=None):
    st.write("Add detailed case history for the patient")
    default_idx = patient_names.index(default_name) if default_name in patient_names else 0
    
    st.selectbox("Select Patient", options=patient_names, index=default_idx, key="hist_select")
    st.text_area("Diagnosis *", placeholder="Enter diagnosis details...", height=100)
    st.text_area("Treatment Plan *", placeholder="Enter treatment plan...", height=100)
    st.text_area("Additional Notes", placeholder="Any additional information...", height=80)
    
    st.markdown("""
        <style>
        .save-hist-btn div.stButton > button { background: linear-gradient(90deg, #7E22CE 0%, #3B82F6 100%) !important; color: white !important; border-radius: 8px; font-weight: 600; width: 100%; border: none; transition: 0.3s; }
        .save-hist-btn div.stButton > button:hover { box-shadow: 0 4px 12px rgba(126, 34, 206, 0.4); }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="save-hist-btn">', unsafe_allow_html=True)
    if st.button("📋 Save Case History", use_container_width=True):
        st.success("Case history saved successfully!")
        time.sleep(1)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. MANAGE DAILY TASKS DIALOG ---
@st.dialog("Manage Patient Tasks", width="large")
def show_task_dialog():
    st.write("Customize the daily checklist your patient will see.")
    
    selected_pt = st.selectbox("Select Patient to Manage", options=patient_names, key="task_select")
    
    st.markdown(f"**Current active tasks for {selected_pt}:**")
    
    # Display current tasks with a Remove button
    current_tasks = st.session_state.patient_tasks.get(selected_pt, [])
    
    if not current_tasks:
        st.info(f"No tasks currently assigned to {selected_pt}.")
    else:
        for i, task in enumerate(current_tasks):
            col_text, col_btn = st.columns([5, 1])
            with col_text:
                st.markdown(f"✅ {task}")
            with col_btn:
                # Button to remove the specific task
                if st.button("❌ Remove", key=f"del_btn_{selected_pt}_{i}"):
                    st.session_state.patient_tasks[selected_pt].pop(i)
                    st.rerun()
    
    st.markdown("---")
    
    # Add new task section
    st.markdown("**Assign a New Task:**")
    new_task_input = st.text_input("Task Description", placeholder="e.g., Go for a 10-minute jog", label_visibility="collapsed")
    
    st.markdown("""
        <style>
        .add-task-btn div.stButton > button { background-color: #1A56DB !important; color: white !important; border-radius: 6px; font-weight: 600; width: 100%; border: none; }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="add-task-btn">', unsafe_allow_html=True)
    if st.button("➕ Add Task to List", use_container_width=True):
        if new_task_input.strip() != "":
            if selected_pt not in st.session_state.patient_tasks:
                st.session_state.patient_tasks[selected_pt] = []
            st.session_state.patient_tasks[selected_pt].append(new_task_input)
            st.rerun()
        else:
            st.error("Please enter a task description.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. MAIN PAGE STYLES ---
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

    /* Patient Card */
    .patient-card { background: white; border-radius: 12px; padding: 20px; border: 1px solid #E2E8F0; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); display: flex; align-items: center; justify-content: space-between; }
    .patient-name { font-size: 1.1rem; font-weight: 700; color: #1E293B; margin-bottom: 4px; }
    .patient-details { font-size: 0.85rem; color: #6B7280; }
    
    .action-btn div.stButton > button { background: #F8FAFC !important; color: #4B5563 !important; border: 1px solid #E2E8F0 !important; font-weight: 600; border-radius: 6px; }
    .action-btn div.stButton > button:hover { background: #F1F5F9 !important; border-color: #CBD5E1 !important; color: #0F172A !important; }

    /* Tab Specific Styles */
    .add-reading-btn div.stButton > button, .add-task-main-btn div.stButton > button { background-color: #1A56DB !important; color: white !important; border-radius: 6px; font-weight: 600; border: none; }
    .add-history-btn div.stButton > button { background-color: #9333EA !important; color: white !important; border-radius: 6px; font-weight: 600; border: none; }
    .empty-state { text-align: center; color: #9CA3AF; padding: 40px 0; font-size: 0.95rem; }
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
with c1: st.markdown(f'<div class="metric-card card-blue"><div class="card-title">👥 Total Patients</div><div class="card-value">{len(patients)}</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="metric-card card-green"><div class="card-title">📉 CO Readings Recorded</div><div class="card-value">0</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="metric-card card-purple"><div class="card-title">📄 Case Histories</div><div class="card-value">0</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 5. INTERACTIVE TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["Patients", "CO Readings", "Case History", "Daily Tasks"])

with tab1:
    st.markdown('<div style="color: #1A56DB; font-weight: 700; font-size: 1.1rem; margin-top: 10px; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">👥 Patient List</div>', unsafe_allow_html=True)

    for p in patients:
        with st.container():
            st.markdown(f"""
                <div style="background: white; border-radius: 12px 12px 0 0; padding: 20px 20px 0 20px; border: 1px solid #E2E8F0; border-bottom: none;">
                    <div class="patient-name">{p['name']}</div>
                    <div class="patient-details">Type: {p['type']} | {p['week']}<br>Current usage: {p['usage']}</div>
                </div>
            """, unsafe_allow_html=True)
            
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

with tab2:
    with st.container(border=True):
        col_title, col_btn = st.columns([4, 1])
        with col_title:
            st.markdown('<div style="font-weight: 700; color: #111827; font-size: 1.1rem; padding-top: 8px;">〽️ Carbon Monoxide Readings</div>', unsafe_allow_html=True)
        with col_btn:
            st.markdown('<div class="add-reading-btn">', unsafe_allow_html=True)
            if st.button("➕ Add Reading", use_container_width=True):
                show_co_dialog() 
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<hr style="margin: 10px 0; border-color: #E2E8F0; opacity: 0.5;">', unsafe_allow_html=True)
        st.markdown('<div class="empty-state">No CO readings recorded yet</div>', unsafe_allow_html=True)

with tab3:
    with st.container(border=True):
        col_title, col_btn = st.columns([4, 1])
        with col_title:
            st.markdown('<div style="font-weight: 700; color: #111827; font-size: 1.1rem; padding-top: 8px;">📄 Patient Case Histories</div>', unsafe_allow_html=True)
        with col_btn:
            st.markdown('<div class="add-history-btn">', unsafe_allow_html=True)
            if st.button("➕ Add Case History", use_container_width=True):
                show_history_dialog() 
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<hr style="margin: 10px 0; border-color: #E2E8F0; opacity: 0.5;">', unsafe_allow_html=True)
        st.markdown('<div class="empty-state">No case histories recorded yet</div>', unsafe_allow_html=True)

with tab4:
    with st.container(border=True):
        col_title, col_btn = st.columns([4, 1])
        with col_title:
            st.markdown('<div style="font-weight: 700; color: #111827; font-size: 1.1rem; padding-top: 8px;">📄 Manage Daily Tasks for Patients</div>', unsafe_allow_html=True)
            st.markdown('<div style="color: #6B7280; font-size: 0.85rem; margin-bottom: 5px;">Customize daily checklist that patients will see</div>', unsafe_allow_html=True)
        with col_btn:
            st.markdown('<div class="add-task-main-btn">', unsafe_allow_html=True)
            if st.button("➕ Add Task", use_container_width=True):
                show_task_dialog()
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<hr style="margin: 10px 0; border-color: #E2E8F0; opacity: 0.5;">', unsafe_allow_html=True)
        
        # Display the active tasks grouped by patient
        for p_name, tasks in st.session_state.patient_tasks.items():
            if tasks:
                with st.expander(f"Active Tasks Configured for: {p_name} ({len(tasks)} tasks)"):
                    for t in tasks:
                        st.markdown(f"- {t}")
