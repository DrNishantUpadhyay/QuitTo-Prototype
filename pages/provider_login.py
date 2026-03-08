import streamlit as st
import time

st.set_page_config(page_title="QuitTo - Provider Login", page_icon="💚", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    .stApp { background: linear-gradient(180deg, #EBF8FF 0%, #FFFFFF 45%); font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 3.5rem !important; max-width: 950px; }
    #MainMenu, footer {visibility: hidden;}

    .form-container { background: white; border-radius: 16px 16px 0 0; padding: 40px 40px 10px 40px; border: 1px solid rgba(229,231,235,0.6); border-bottom: none; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08); max-width: 450px; margin: 0 auto; }
    .form-header { font-size: 1.8rem; font-weight: 700; display: flex; align-items: center; gap: 10px; margin-bottom: 5px; justify-content: center; }
    .form-subtext { color: #6B7280; font-size: 0.95rem; margin-bottom: 10px; text-align: center; }
    
    .back-btn div.stButton > button { background: transparent !important; color: #4B5563 !important; width: auto !important; height: auto !important; padding: 0 !important; font-size: 1.5rem !important; margin-bottom: 15px; border: none; }
    
    /* Submit Button Gradient: Green to Blue */
    .login-btn div.stButton > button { background: linear-gradient(90deg, #059669 0%, #1A56DB 100%) !important; color: white !important; margin-top: 20px; border-radius: 8px; height: 48px; font-weight: 600; width: 100%; border: none; transition: 0.3s;}
    .login-btn div.stButton > button:hover { box-shadow: 0 4px 12px rgba(5, 150, 105, 0.4); }
    
    .demo-text { text-align: center; color: #6B7280; font-size: 0.85rem; margin-top: 25px; line-height: 1.6; }
    .demo-text code { background: #F3F4F6; padding: 2px 6px; border-radius: 4px; color: #374151; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

spacer1, center_col, spacer2 = st.columns([1, 2, 1])

with center_col:
    # Back button to return to the home page
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("←", key="back_btn"):
        st.switch_page("app.py")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="form-container">
            <div class="form-header">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="3"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.78-.77-.78a5.4 5.4 0 0 0-7.65 0C1.46 6.7 1.33 10.28 4 13l8 8 8-8c2.67-2.72 2.54-6.3.42-8.42z"></path><polyline points="12 6 12 11 15 14"></polyline></svg>
                <span style="color: #059669;">Healthcare</span>&nbsp;<span style="color: #1A56DB;">Provider</span>
            </div>
            <p class="form-subtext">Login to access patient records and monitoring tools</p>
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="background: white; padding: 0 40px 40px 40px; border-radius: 0 0 16px 16px; border: 1px solid rgba(229,231,235,0.6); border-top: none; max-width: 450px; margin: 0 auto; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);">', unsafe_allow_html=True)
        
        st.write("**Username**")
        username = st.text_input("Username", label_visibility="collapsed", placeholder="Enter your username")
        
        st.write("**Password**")
        password = st.text_input("Password", label_visibility="collapsed", placeholder="Enter your password", type="password")
        
        st.markdown('<div class="login-btn">', unsafe_allow_html=True)
        if st.button("Login", use_container_width=True):
            if username == "dentist" and password == "admin123":
                st.success("Login successful! Redirecting to dashboard...")
                time.sleep(1) # Small delay to show the success message
                st.switch_page("pages/provider_dashboard.py") 
            else:
                st.error("Incorrect credentials. Please use the demo login.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="demo-text">
                Demo credentials:<br>
                Username: <code>dentist</code><br>
                Password: <code>admin123</code>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
