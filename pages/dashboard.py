import streamlit as st

st.set_page_config(page_title="QuitTo - Dashboard", page_icon="💙", layout="wide")

# Get saved data from session state
name = st.session_state.get('patient_name', 'Raj Kapur')
usage = st.session_state.get('patient_usage', '10')

# --- 1. DEFINE THE POPUP DIALOG HERE ---
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
    """, unsafe_allow_html=True)

    st.markdown('<div class="tcc-subtitle">Get professional support for your recovery journey</div>', unsafe_allow_html=True)

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
        # Aapka photo wala link
        image_url = "https://raw.githubusercontent.com/DrNishantUpadhyay/QuitTo-Prototype/main/dr_hemant.jpg.jpeg"
        st.markdown(f'<img src="{image_url}" class="dr-img">', unsafe_allow_html=True)


# --- 2. MAIN PAGE STYLES ---
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
    .progress-bar-fill { background-color: currentColor; border-radius: 10px; height: 6px; width: 5%; }

    /* Button Styles */
    .tcc-btn div.stButton > button { background: linear-gradient(90deg, #1A56DB 0%, #059669 100%) !important; color: white !important; border-radius: 8px; height: 50px; font-weight: 600; border: none; width: 100%; transition: 0.3s; }
    .tcc-btn div.stButton > button:hover { box-shadow: 0 4px 12px rgba(5, 150, 105, 0.4); }
    .white-btn div.stButton > button { background: white !important; color: #4B5563 !important; border-radius: 8px; height: 50px; font-weight: 600; border: 1px solid #E5E7EB !important; margin-top: 10px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# Top Bar
col_head, col_btn = st.columns([4, 1])
with col_head:
    st.markdown(f'<div class="dash-header">Welcome back, <span>{name}!</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="dash-subtext">Week 1 of 12</div>', unsafe_allow_html=True)
with col_btn:
    st.markdown('<div style="text-align: right; margin-top: 10px;">', unsafe_allow_html=True)
    if st.button("🚪 Logout"): st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Top Metrics Cards
c1, c2, c3 = st.columns(3)
with c1: st.markdown(f'<div class="metric-card card-blue"><div class="card-title">📉 Current Progress</div><div class="card-value">{usage} units/day</div><div class="card-desc">Down from {usage} units/day</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="color: #1D4ED8;"></div></div><div style="font-size: 0.75rem; color: #6B7280; margin-top: 8px;">0% reduction achieved</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="metric-card card-green"><div class="card-title">💲 Money Saved</div><div class="card-value">₹0</div><div class="card-desc">This week<br><br>Daily: ₹0 | Monthly: ₹0</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="metric-card card-purple"><div class="card-title">✅ Daily Tasks</div><div class="card-value">0/5</div><div class="card-desc">Completed today</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="color: #9333EA;"></div></div><div style="font-size: 0.75rem; color: #6B7280; margin-top: 8px;">0% daily goals
