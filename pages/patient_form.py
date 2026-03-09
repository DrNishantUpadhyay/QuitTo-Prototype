import streamlit as st

st.set_page_config(page_title="QuitTo - Patient", page_icon="https://raw.githubusercontent.com/DrNishantUpadhyay/QuitTo-Prototype/main/icon.png.png", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    .stApp { background: linear-gradient(180deg, #EBF8FF 0%, #FFFFFF 45%); font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 3.5rem !important; max-width: 950px; }
    #MainMenu, footer {visibility: hidden;}

    .form-container { background: white; border-radius: 16px 16px 0 0; padding: 40px 40px 10px 40px; border: 1px solid rgba(229,231,235,0.6); border-bottom: none; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08); max-width: 650px; margin: 0 auto; }
    .form-header { color: #1A56DB; font-size: 1.8rem; font-weight: 700; display: flex; align-items: center; gap: 10px; margin-bottom: 5px; }
    .form-header span { color: #059669; }
    .form-subtext { color: #6B7280; font-size: 0.95rem; margin-bottom: 10px; }
    
    .back-btn div.stButton > button { background: transparent !important; color: #4B5563 !important; width: auto !important; height: auto !important; padding: 0 !important; font-size: 1.5rem !important; margin-bottom: 15px; border: none; }
    
    /* Submit Button Gradient */
    .submit-btn div.stButton > button { background: linear-gradient(90deg, #1A56DB 0%, #059669 100%) !important; color: white !important; margin-top: 20px; border-radius: 8px; height: 48px; font-weight: 600; width: 100%; border: none; transition: 0.3s;}
    .submit-btn div.stButton > button:hover { box-shadow: 0 4px 12px rgba(5, 150, 105, 0.4); }
    </style>
""", unsafe_allow_html=True)

spacer1, center_col, spacer2 = st.columns([1, 2, 1])

with center_col:
    # Back Button
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("←", key="back_btn"):
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Top half of the white card
    st.markdown("""
        <div class="form-container">
            <div class="form-header">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1A56DB" stroke-width="3"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 0C1.46 6.7 1.33 10.28 4 13l8 8 8-8c2.67-2.72 2.54-6.3.42-8.42z"></path><polyline points="12 6 12 11 15 14"></polyline></svg>
                Start Your <span>Journey</span>
            </div>
            <p class="form-subtext">Let's create your personalized 12-week recovery plan</p>
        </div>
    """, unsafe_allow_html=True)

    # Bottom half of the white card (Inputs + Button)
    with st.container():
        st.markdown('<div style="background: white; padding: 0 40px 40px 40px; border-radius: 0 0 16px 16px; border: 1px solid rgba(229,231,235,0.6); border-top: none; max-width: 650px; margin: 0 auto; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);">', unsafe_allow_html=True)
        
        name = st.text_input("Full Name", placeholder="Enter your name")
        addiction_type = st.selectbox("What are you looking to quit?", ["Smoking (Cigarettes)", "Alcohol", "Chewing Tobacco"])
        usage = st.text_input("Current daily usage", placeholder="e.g., 10 cigarettes")
        cost = st.text_input("Cost per pack/unit (₹)", placeholder="e.g., 150")
        st.caption("This helps calculate your savings over time")
        
        st.markdown('<div class="submit-btn">', unsafe_allow_html=True)
        if st.button("Create My Plan", use_container_width=True):
            # Form ka data save karke Dashboard par bhej rahe hain
            st.session_state['patient_name'] = name
            st.session_state['patient_usage'] = usage
            st.switch_page("pages/dashboard.py")
        st.markdown('</div></div>', unsafe_allow_html=True)
      
