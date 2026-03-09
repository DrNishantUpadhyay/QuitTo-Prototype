import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="QuitTo - Dashboard", page_icon="💙", layout="wide")

# Get saved data
name = st.session_state.get('patient_name', 'Raj Kapur')
usage = st.session_state.get('patient_usage', '10')
cost_per_pack = st.session_state.get('patient_cost', '150')

# --- INITIALIZE SYNCED TASKS ---
# If the dentist hasn't added tasks yet, we set the default ones here too
if 'patient_tasks' not in st.session_state:
    st.session_state.patient_tasks = {
        name: [
            "Take a 5-minute walk", 
            "Drink 2L of water", 
            "Practice deep breathing for 5 minutes", 
            "Eat a healthy breakfast", 
            "Avoid triggers (identify and note them)"
        ]
    }

# Fetch the live task list for THIS specific patient
daily_tasks_list = st.session_state.patient_tasks.get(name, [])
total_tasks = len(daily_tasks_list)

# Calculate how many tasks the patient has checked off today
completed_tasks = sum([st.session_state.get(f"task_{name}_{i}", False) for i in range(total_tasks)])
progress_pct = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

# --- 1. TCC POPUP DIALOG ---
@st.dialog("TCC - Tobacco Cessation Cell", width="large")
def show_tcc_popup():
    st.markdown("""
        <style>
        .tcc-subtitle { color: #6B7280; font-size: 0.95rem; margin-bottom: 25px; margin-top: -10px; }
        .tcc-info-row { display: flex; gap: 15px; margin-bottom: 20px; align-items: flex-start; }
        .tcc-icon { font-size: 1.2rem; margin-top: 2px; }
        .tcc-label { font-size: 0.85rem; font-weight: 600; color: #111827; margin-bottom: 2px; }
        .tcc-text { font-size: 0.85rem; color: #4B5563; line-height: 1.4; }
        .dr-img { width: 100%; height: 280px; object-fit: cover; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        </style>
        <div class="tcc-subtitle">Get professional support for your recovery journey</div>
    """, unsafe_allow_html=True)

    col_info, col_img = st.columns([1.2, 1], gap="medium")

    with col_info:
        st.markdown("""
            <div class="tcc-info-row">
                <div class="tcc-icon" style="color: #3B82F6;">📍</div>
                <div>
                    <div class="tcc-label">Location</div>
                    <div class="tcc-text">Department of Oral Medicine<br>and Radiology<br>School of Dental Sciences<br>Sharda University<br>Greater Noida, UP<br>Ground Floor</div>
                </div>
            </div>
            <div class="tcc-info-row">
                <div class="tcc-icon" style="color: #10B981;">👤</div>
                <div>
                    <div class="tcc-label">TCC Incharge</div>
                    <div class="tcc-text">Dr. Hemant Sawhney</div>
                </div>
            </div>
            <div class="tcc-info-row">
                <div class="tcc-icon" style="color: #8B5CF6;">📞</div>
                <div>
                    <div class="tcc-label">Phone</div>
                    <div class="tcc-text" style="color: #1A56DB;">9560705787</div>
                </div>
            </div>
            <div class="tcc-info-row">
                <div class="tcc-icon" style="color: #EF4444;">✉️</div>
                <div>
                    <div class="tcc-label">Email</div>
                    <div class="tcc-text" style="color: #1A56DB;">tcc.omr@sharda.ac.in</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_img:
        image_url = "https://raw.githubusercontent.com/DrNishantUpadhyay/QuitTo-Prototype/main/dr_hemant.jpg.jpeg"
        st.markdown(f'<img src="{image_url}" class="dr-img">', unsafe_allow_html=True)

# --- 2. DEVELOPER POPUP DIALOG ---
@st.dialog("Developer Information", width="large")
def show_dev_popup():
    st.markdown("""
        <style>
        .dev-subtitle { color: #6B7280; font-size: 0.95rem; margin-bottom: 25px; margin-top: -10px; text-align: center; }
        .dev-card { text-align: center; padding: 20px; background: #F8FAFC; border-radius: 16px; border: 1px solid #E2E8F0; height: 100%; }
        .dev-img { width: 140px; height: 140px; object-fit: cover; border-radius: 50%; border: 4px solid white; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px; }
        .dev-name { font-size: 1.2rem; font-weight: 700; color: #1E293B; margin-bottom: 5px; }
        .dev-role { font-size: 0.9rem; color: #059669; font-weight: 600; margin-bottom: 15px; }
        .dev-email { font-size: 0.85rem; color: #4B5563; background: white; padding: 8px 12px; border-radius: 8px; border: 1px solid #E2E8F0; display: inline-block; }
        .dev-email a { color: #1A56DB; text-decoration: none; font-weight: 500; }
        </style>
        <div class="dev-subtitle">Meet the team behind the QuitTo App</div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown(f'''
            <div class="dev-card">
                <img src="https://raw.githubusercontent.com/DrNishantUpadhyay/QuitTo-Prototype/main/dr_nishant.jpg.jpeg" class="dev-img">
                <div class="dev-name">Dr. Nishant Upadhyay</div>
                <div class="dev-role">Founder & Lead Developer</div>
                <div class="dev-email">📧 <a href="mailto:nishant78913@gmail.com">nishant78913@gmail.com</a></div>
            </div>
        ''', unsafe_allow_html=True)

    with c2:
        st.markdown(f'''
            <div class="dev-card">
                <img src="https://raw.githubusercontent.com/DrNishantUpadhyay/QuitTo-Prototype/main/laxmi_sharma.jpg.jpeg" class="dev-img">
                <div class="dev-name">Laxmi Raj Sharma</div>
                <div class="dev-role">Co-Founder & UI/UX Lead</div>
                <div class="dev-email">📧 <a href="mailto:laxmirajsharma06@gmail.com">laxmirajsharma06@gmail.com</a></div>
            </div>
        ''', unsafe_allow_html=True)

# --- 3. MAIN PAGE STYLES ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    .stApp { background: linear-gradient(180deg, #EBF8FF 0%, #FFFFFF 45%); font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 2rem !important; max-width: 1050px; }
    #MainMenu, footer {visibility: hidden;}

    .dash-header { color: #1A56DB; font-size: 2.5rem; font-weight: 700; margin-bottom: 5px; }
    .dash-header span { color: #059669; }
    .dash-subtext { color: #6B7280; font-size: 1rem; margin-bottom: 30px; }

    .metric-card { border-radius: 16px; padding: 25px; height: 100%; border: 1px solid rgba(229,231,235,0.6); box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03); }
    .card-blue { background-color: #E0F2FE; }
    .card-green { background-color: #DCFCE7; }
    .card-purple { background-color: #F3E8FF; }
    
    .card-title { font-size: 0.9rem; font-weight: 600; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }
    .card-blue .card-title { color: #0369A1; }
    .card-green .card-title { color: #15803D; }
    .card-purple .card-title { color: #7E22CE; }
    
    .card-value { font-size: 2rem; font-weight: 700; margin-bottom: 5px; }
    .card-blue .card-value { color: #1D4ED8; }
    .card-green .card-value { color: #16A34A; }
    .card-purple .card-value { color: #9333EA; }
    
    .card-desc { font-size: 0.85rem; color: #6B7280; margin-bottom: 15px; }
    
    .progress-bar-bg { background-color: rgba(0,0,0,0.1); border-radius: 10px; height: 6px; width: 100%; }
    .progress-bar-fill { background-color: currentColor; border-radius: 10px; height: 6px; transition: width 0.4s ease; }

    .tcc-btn div.stButton > button { background: linear-gradient(90deg, #1A56DB 0%, #059669 100%) !important; color: white !important; border-radius: 8px; height: 50px; font-weight: 600; border: none; width: 100%; transition: 0.3s; }
    .tcc-btn div.stButton > button:hover { box-shadow: 0 4px 12px rgba(5, 150, 105, 0.4); }
    
    .white-btn div.stButton > button { background: white !important; color: #4B5563 !important; border-radius: 8px; height: 50px; font-weight: 600; border: 1px solid #E5E7EB !important; margin-top: 10px; width: 100%; transition: 0.3s; }
    .white-btn div.stButton > button:hover { background: #F8FAFC !important; border-color: #CBD5E1 !important; }
    </style>
""", unsafe_allow_html=True)

# Top Bar
col_head, col_btn = st.columns([4, 1])
with col_head:
    st.markdown(f'<div class="dash-header">Welcome back, <span>{name}!</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="dash-subtext">Week 1 of 12</div>', unsafe_allow_html=True)
with col_btn:
    st.markdown('<div style="text-align: right; margin-top: 10px;">', unsafe_allow_html=True)
    if st.button("🚪 Logout"): 
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)

try: start_usage = int(usage)
except: start_usage = 10

try: pack_cost = float(cost_per_pack)
except: pack_cost = 150.0

daily_savings = (start_usage / 20.0) * pack_cost

# Top Metrics Cards
c1, c2, c3 = st.columns(3)
with c1: 
    st.markdown(f"""
        <div class="metric-card card-blue">
            <div class="card-title">📉 Current Progress</div>
            <div class="card-value">{start_usage} units/day</div>
            <div class="card-desc">Down from {start_usage} units/day</div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="color: #1D4ED8; width: 5%;"></div></div>
            <div style="font-size: 0.75rem; color: #6B7280; margin-top: 8px;">0% reduction achieved</div>
        </div>
    """, unsafe_allow_html=True)
with c2: 
    st.markdown(f"""
        <div class="metric-card card-green">
            <div class="card-title">💲 Money Saved</div>
            <div class="card-value">₹0</div>
            <div class="card-desc">This week<br><br>Daily: ₹{int(daily_savings)} | Monthly: ₹{int(daily_savings*30)}</div>
        </div>
    """, unsafe_allow_html=True)
with c3: 
    st.markdown(f"""
        <div class="metric-card card-purple">
            <div class="card-title">✅ Daily Tasks</div>
            <div class="card-value">{completed_tasks}/{total_tasks}</div>
            <div class="card-desc">Completed today</div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="color: #9333EA; width: {progress_pct}%;"></div></div>
            <div style="font-size: 0.75rem; color: #6B7280; margin-top: 8px;">{progress_pct}% daily goals</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Tabs Navigation
tab1, tab2, tab3, tab4 = st.tabs(["📅 Schedule", "✅ Daily Tasks", "⚕️ Health Recovery", "📊 Analytics"])

with tab1:
    st.markdown("### 12-Week Reduction Schedule")
    for week in range(1, 13):
        target = max(0, start_usage - (week - 1)) 
        with st.expander(f"Week {week} - Target: {target} units/day", expanded=(week==1)):
            if week == 1: 
                st.info("Current Week: Focus on strictly monitoring your intake.")
            st.write(f"**Goal:** Limit consumption to {target} units per day.")
            st.checkbox(f"I completed my targets for Week {week}", key=f"w{week}")
            
with tab2: 
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 5px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            <h3 style="margin: 0; color: #111827;">Today's Tasks</h3>
        </div>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 25px;">Complete these daily activities to support your recovery</p>
    """, unsafe_allow_html=True)

    if not daily_tasks_list:
        st.info("You have completed all your tasks or none have been assigned yet. Great job!")
    else:
        for i, task in enumerate(daily_tasks_list):
            with st.container(border=True):
                # The key connects the checkbox to session_state automatically
                st.checkbox(task, key=f"task_{name}_{i}")
            
    st.markdown("<p style='color: #9CA3AF; font-size: 0.8rem; margin-top: 15px;'>Note: Your dentist can customize this checklist specifically for you</p>", unsafe_allow_html=True)

with tab3: 
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 5px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
            <h3 style="margin: 0; color: #111827;">Health Recovery Milestones</h3>
        </div>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 25px;">Track your body's healing progress over time</p>
    """, unsafe_allow_html=True)

    milestones = [
        {"icon": "🌬️", "time": "8 hours", "desc": "Oxygen levels returning to normal"},
        {"icon": "📉", "time": "12 hours", "desc": "Carbon monoxide levels in your blood drop to normal"},
        {"icon": "❤️", "time": "24 hours", "desc": "Risk of heart attack begins to drop"},
        {"icon": "👅", "time": "2 days", "desc": "Nerve endings start to regrow; sense of smell and taste improve"},
        {"icon": "🫁", "time": "4 days", "desc": "Nicotine is mostly out of your body; breathing becomes easier"},
        {"icon": "🧠", "time": "1 week", "desc": "Cravings begin to reduce in frequency and intensity"},
        {"icon": "💪", "time": "2 weeks", "desc": "Circulation and lung function significantly improve"},
        {"icon": "🏃", "time": "1-3 months", "desc": "Coughing, shortness of breath, and fatigue improve"},
        {"icon": "💚", "time": "1 year", "desc": "Risk of heart disease is reduced by 50%"}
    ]

    for m in milestones:
        st.markdown(f'''
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 20px; margin-bottom: 12px; display: flex; align-items: center; gap: 15px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">
                <div style="font-size: 22px; background: white; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #E2E8F0; flex-shrink: 0;">{m["icon"]}</div>
                <div>
                    <div style="font-weight: 700; color: #1E293B; font-size: 0.95rem;">{m["time"]}</div>
                    <div style="color: #4B5563; font-size: 0.85rem;">{m["desc"]}</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

with tab4: 
    with st.container(border=True):
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 5px;">
                <h3 style="margin: 0; color: #111827; font-size: 1.1rem;">Usage Trend</h3>
            </div>
            <p style="color: #6B7280; font-size: 0.85rem; margin-bottom: 25px;">Your declining usage over the 12-week period</p>
        """, unsafe_allow_html=True)

        trend_data = []
        current_u = start_usage
        for w in range(1, 13):
            trend_data.append(max(0, current_u))
            if w % 2 == 0: 
                current_u -= 2

        df = pd.DataFrame({
            "Week": [i for i in range(1, 13)],
            "Units/day": trend_data
        })

        chart = alt.Chart(df).mark_line(point=True, color="#3B82F6", strokeWidth=2).encode(
            x=alt.X('Week:O', axis=alt.Axis(labelAngle=0, grid=True)),
            y=alt.Y('Units/day:Q', title="Units/day", scale=alt.Scale(domain=[0, max(12, start_usage)]))
        ).properties(height=250)
        
        st.altair_chart(chart, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("""
            <h3 style="margin: 0; color: #111827; font-size: 1.1rem; margin-bottom: 20px;">Financial Savings Projection</h3>
        """, unsafe_allow_html=True)
        
        m1 = int(daily_savings * 30)
        m3 = int(daily_savings * 90)
        y1 = int(daily_savings * 365)
        
        st.markdown(f'''
            <div style="background: #F0F9FF; border: 1px solid #E0F2FE; border-radius: 8px; padding: 15px 20px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                <div style="color: #0369A1; font-weight: 500;">1 Month</div>
                <div style="color: #0369A1; font-weight: 700; font-size: 1.1rem;">₹{m1:,}</div>
            </div>
            <div style="background: #F0FDF4; border: 1px solid #DCFCE7; border-radius: 8px; padding: 15px 20px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                <div style="color: #15803D; font-weight: 500;">3 Months</div>
                <div style="color: #15803D; font-weight: 700; font-size: 1.1rem;">₹{m3:,}</div>
            </div>
            <div style="background: #FAF5FF; border: 1px solid #F3E8FF; border-radius: 8px; padding: 15px 20px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                <div style="color: #7E22CE; font-weight: 500;">1 Year</div>
                <div style="color: #7E22CE; font-weight: 700; font-size: 1.1rem;">₹{y1:,}</div>
            </div>
        ''', unsafe_allow_html=True)

st.markdown("<br><hr style='opacity: 0.2;'>", unsafe_allow_html=True)

# --- 4. BOTTOM BUTTONS (Triggers) ---
st.markdown('<div class="tcc-btn">', unsafe_allow_html=True)
if st.button("📞 Contact TCC - Tobacco Cessation Cell", use_container_width=True):
    show_tcc_popup()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="white-btn">', unsafe_allow_html=True)
if st.button("</> Developer Information", use_container_width=True):
    show_dev_popup()
st.markdown('</div>', unsafe_allow_html=True)
