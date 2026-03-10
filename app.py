import streamlit as st

# Replace your old st.set_page_config line with this one:
st.set_page_config(page_title="QuitTo", page_icon="https://raw.githubusercontent.com/DrNishantUpadhyay/QuitTo-Images/main/icon.png.png", layout="wide")

# CSS to hide default sidebar and add Figma styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    [data-testid="collapsedControl"] { display: none; } /* Hides Sidebar Menu */
    [data-testid="stSidebar"] { display: none; }
    
    .stApp { background: linear-gradient(180deg, #EBF8FF 0%, #FFFFFF 45%); font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 3.5rem !important; max-width: 950px; }
    #MainMenu, footer {visibility: hidden;}

    .header-container { text-align: center; margin-bottom: 50px; }
    .main-logo { color: #1A56DB; font-size: 3.2rem; font-weight: 800; display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 15px; }
    .tagline { color: #4B5563; font-size: 1.1rem; font-weight: 500; margin-bottom: 8px; }
    .sub-tagline { color: #9CA3AF; font-size: 0.9rem; }
    
    .card-container { background: white; border-radius: 16px; padding: 40px 30px; border: 1px solid rgba(229,231,235,0.6); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); text-align: center; height: 100%; transition: 0.3s; }
    .card-container:hover { transform: translateY(-3px); box-shadow: 0 10px 25px -5px rgba(0,0,0,0.08); }
    .icon-wrapper-blue { background: #1A56DB; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px auto; color: white; box-shadow: 0 8px 16px rgba(26,86,219,0.25); }
    .icon-wrapper-green { background: #059669; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px auto; color: white; box-shadow: 0 8px 16px rgba(5,150,105,0.25); }
    .card-title { color: #111827; font-size: 1.4rem; font-weight: 700; margin-bottom: 12px; }
    .card-text { color: #6B7280; font-size: 0.9rem; margin-bottom: 30px; }
    
    div.stButton > button { border-radius: 8px; height: 48px; font-weight: 600; width: 100%; border: none; }
    .patient-btn div.stButton > button { background-color: #1A56DB !important; color: white !important; }
    .provider-btn div.stButton > button { background-color: #059669 !important; color: white !important; }
    
    .feature-box { background: white; border-radius: 12px; padding: 24px 20px; text-align: center; border: 1px solid rgba(229,231,235,0.6); }
    .feature-icon { font-size: 26px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <div class="main-logo">
            <svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 0C1.46 6.7 1.33 10.28 4 13l8 8 8-8c2.67-2.72 2.54-6.3.42-8.42z"></path><polyline points="12 6 12 11 15 14"></polyline></svg>
            QuitTo
        </div>
        <div class="tagline">Your journey to a healthier life through incremental harm reduction</div>
        <div class="sub-tagline">A science-backed "Slow-Quit" method for smoking, alcohol, and tobacco cessation</div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="card-container"><div class="icon-wrapper-blue"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></div><div class="card-title">I\'m a Patient</div><div class="card-text">Start your personalized recovery journey with a 12-week reduction schedule</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="patient-btn">', unsafe_allow_html=True)
    if st.button("Get Started", key="pt_btn"):
        st.switch_page("pages/patient_form.py") # Naye page par bhejne ka code
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card-container"><div class="icon-wrapper-green"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 0C1.46 6.7 1.33 10.28 4 13l8 8 8-8c2.67-2.72 2.54-6.3.42-8.42z"></path></svg></div><div class="card-title">Healthcare Provider</div><div class="card-text">Monitor your patients\' progress and record health metrics</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="provider-btn">', unsafe_allow_html=True)
    if st.button("Provider Login", key="pr_btn"):
        st.switch_page("pages/provider_login.py")
    st.markdown('</div>', unsafe_allow_html=True)
    
st.markdown("<br>", unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
with f1: st.markdown('<div class="feature-box"><div class="feature-icon">🚬</div><div class="feature-title">12-Week Plan</div><div class="feature-desc">Gradual reduction schedule</div></div>', unsafe_allow_html=True)
with f2: st.markdown('<div class="feature-box"><div class="feature-icon">⚕️</div><div class="feature-title">Health Tracking</div><div class="feature-desc">Monitor recovery milestones</div></div>', unsafe_allow_html=True)
with f3: st.markdown('<div class="feature-box"><div class="feature-icon">🍷</div><div class="feature-title">Multiple Addictions</div><div class="feature-desc">Smoking, tobacco, alcohol</div></div>', unsafe_allow_html=True)
