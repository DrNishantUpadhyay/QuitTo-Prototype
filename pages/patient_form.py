import streamlit as st

st.set_page_config(page_title="QuitTo - Patient", page_icon="💙", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    .stApp { background: linear-gradient(180deg, #EBF8FF 0%, #FFFFFF 45%); font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 3.5rem !important; max-width: 950px; }
    #MainMenu, footer {visibility: hidden;}

    .form-container { background: white; border-radius: 16px; padding: 40px; border: 1px solid rgba(229,231,235,0.6); box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08); max-width: 650px; margin: 0 auto; }
    .form-header { color: #1A56DB; font-size: 1.8rem; font-weight: 700; display: flex; align-items: center; gap: 10px; margin-bottom: 5px; }
    .form-header span { color: #059669; }
    .form-subtext { color: #6B7280; font-size: 0.95rem; margin-bottom: 30px; }
    
    .back-btn div.stButton > button { background: transparent !important; color: #4B5563 !important; width: auto !important; height: auto !important; padding: 0 !important; font-size: 1.5rem !important; margin-bottom: 15px; border: none; }
    .submit-btn div.stButton > button { background: linear-gradient(90deg, #1A56DB 0%, #059669 100%) !important; color: white !important; margin-top: 15px; border-radius: 8px; height: 48px; font-weight: 600; width: 100%; border: none; }
    </style>
""", unsafe_allow_html=True)

spacer1, center_col, spacer2 = st.columns([1, 2, 1])

with center_col:
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("←", key="back_btn"):
        st.switch_page("app.py") # Wapas Home par bhejne ka code
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="form-container">
            <div class="form-header">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1A56DB" stroke-width="3"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 0C1.46 6.7 1.33 10.28 4 13l8 8 8-8c2.67-2.72 2.54-6.3.42-8.42z"></path><polyline points="12 6 12 11 15 14"></polyline></svg>
                Start Your <span>Journey</span>
            </div>
            <p class="form-subtext">Let's create your personalized 12-week recovery plan</p>
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="submit-btn">', unsafe_allow_html=True)
        if st.button("Create My Plan", use_container_width=True):
            # Data save kar rahe hain session_state mein
            st.session_state.patient_name = name
            st.session_state.patient_addiction = addiction_type
            st.session_state.patient_usage = usage
            st.session_state.patient_cost = cost
            
            # Dashboard par bhej rahe hain
            st.switch_page("pages/dashboard.py")
        st.markdown('</div></div>', unsafe_allow_html=True)
      
