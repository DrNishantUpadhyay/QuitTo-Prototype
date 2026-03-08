import streamlit as st

st.set_page_config(page_title="QuitTo - Dashboard", page_icon="💙", layout="wide")

# Get saved data from session state (with fallbacks if directly opened)
name = st.session_state.get('patient_name', 'Raj Kapur')
usage = st.session_state.get('patient_usage', '10')

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    .stApp { background: linear-gradient(180deg, #EBF8FF 0%, #FFFFFF 45%); font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 2rem !important; max-width: 1050px; }
    #MainMenu, footer {visibility: hidden;}

    /* Header styling */
    .dash-header { color: #1A56DB; font-size: 2.5rem; font-weight: 700; margin-bottom: 5px; }
    .dash-header span { color: #059669; }
    .dash-subtext { color: #6B7280; font-size: 1rem; margin-bottom: 30px; }

    /* Top Cards Styling */
    .metric-card {
        border-radius: 16px;
        padding: 25px;
        height: 100%;
        border: 1px solid rgba(229,231,235,0.6);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
    }
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
    
    /* Progress Bar Hack */
    .progress-bar-bg { background-color: rgba(0,0,0,0.1); border-radius: 10px; height: 6px; width: 100%; }
    .progress-bar-fill { background-color: currentColor; border-radius: 10px; height: 6px; width: 5%; }

    /* Full Width Buttons */
    .gradient-btn div.stButton > button {
        background: linear-gradient(90deg, #1A56DB 0%, #059669 100%) !important;
        color: white !important;
        border-radius: 8px;
        height: 50px;
        font-weight: 600;
        border: none;
        margin-top: 20px;
    }
    .white-btn div.stButton > button {
        background: white !important;
        color: #4B5563 !important;
        border-radius: 8px;
        height: 50px;
        font-weight: 600;
        border: 1px solid #E5E7EB !important;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Top Bar (Header & Logout)
col_head, col_btn = st.columns([4, 1])
with col_head:
    st.markdown(f'<div class="dash-header">Welcome back, <span>{name}!</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="dash-subtext">Week 1 of 12</div>', unsafe_allow_html=True)
with col_btn:
    st.markdown('<div style="text-align: right; margin-top: 10px;">', unsafe_allow_html=True)
    if st.button("🚪 Logout"):
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Top Metrics Cards
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
        <div class="metric-card card-blue">
            <div class="card-title">📉 Current Progress</div>
            <div class="card-value">{usage} units/day</div>
            <div class="card-desc">Down from {usage} units/day</div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="color: #1D4ED8;"></div></div>
            <div style="font-size: 0.75rem; color: #6B7280; margin-top: 8px;">0% reduction achieved</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="metric-card card-green">
            <div class="card-title">💲 Money Saved</div>
            <div class="card-value">₹0</div>
            <div class="card-desc">This week<br><br>Daily: ₹0 | Monthly: ₹0</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="metric-card card-purple">
            <div class="card-title">✅ Daily Tasks</div>
            <div class="card-value">0/5</div>
            <div class="card-desc">Completed today</div>
            <div class="progress-bar-bg"><div class="progress-bar-fill" style="color: #9333EA;"></div></div>
            <div style="font-size: 0.75rem; color: #6B7280; margin-top: 8px;">0% of daily goals</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Tabs Navigation
tab1, tab2, tab3, tab4 = st.tabs(["📅 Schedule", "✅ Daily Tasks", "⚕️ Health Recovery", "📊 Analytics"])

with tab1:
    st.markdown("### 12-Week Reduction Schedule")
    st.caption("Expand each week to see your tailored targets.")
    
    # Implementing the collapsible Accordion design for 12 weeks
    try:
        base_usage = int(usage)
    except:
        base_usage = 10
        
    for week in range(1, 13):
        # Fake calculation for decreasing usage (MVP purpose)
        target = max(0, base_usage - (week - 1)) 
        
        # Make Week 1 open by default, others closed
        with st.expander(f"Week {week} - Target: {target} units/day", expanded=(week==1)):
            if week == 1:
                st.info("Current Week: Focus on strictly monitoring your intake without feeling pressured.")
            st.write(f"**Goal:** Limit consumption to {target} units per day.")
            st.write("**Tip:** Drink a glass of water every time you feel a craving.")
            st.checkbox(f"I completed my targets for Week {week}", key=f"w{week}")

with tab2:
    st.write("Daily tasks feature coming soon...")

with tab3:
    st.write("Health recovery timeline coming soon...")

with tab4:
    st.write("Analytics charts coming soon...")

st.markdown("<br><hr style='opacity: 0.2;'>", unsafe_allow_html=True)

# Bottom Placeholder Buttons
st.markdown('<div class="gradient-btn">', unsafe_allow_html=True)
st.button("📞 Contact TCC - Tobacco Cessation Cell", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="white-btn">', unsafe_allow_html=True)
st.button("</> Developer Information", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
