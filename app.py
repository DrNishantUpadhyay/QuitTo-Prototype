import streamlit as st

# Page Configuration
st.set_page_config(page_title="QuitTo", page_icon="💙", layout="wide")

# Custom CSS to match Figma exactly
st.markdown("""
    <style>
    /* 1. Gradient Background for the whole app */
    .stApp {
        background: linear-gradient(180deg, #E3F2FD 0%, #FFFFFF 40%);
        font-family: 'Inter', sans-serif;
    }

    /* 2. Remove default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        max-width: 1000px;
    }

    /* 3. Title Styling */
    .main-title {
        color: #1565C0;
        font-size: 3rem !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
    }
    .tagline {
        text-align: center;
        color: #546E7A;
        font-size: 1.2rem;
        margin-top: -10px;
    }
    .sub-tagline {
        text-align: center;
        color: #90A4AE;
        font-size: 0.9rem;
        margin-bottom: 40px;
    }

    /* 4. Figma-style Cards */
    .figma-card {
        background: white;
        border-radius: 20px;
        padding: 40px 20px;
        border: 1px solid #E0E0E0;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.05);
        text-align: center;
        height: 350px;
        transition: transform 0.3s ease;
    }
    .figma-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 15px 35px rgba(21, 101, 192, 0.1);
    }

    /* 5. Icons in Cards */
    .icon-box {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px auto;
        font-size: 30px;
    }

    /* 6. Custom Buttons Styling */
    div.stButton > button {
        border-radius: 10px;
        height: 50px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s;
        border: none;
        width: 100%;
    }
    /* Patient Button (Blue) */
    .patient-btn div.stButton > button {
        background-color: #1D61F2 !important;
        color: white !important;
    }
    /* Provider Button (Green) */
    .provider-btn div.stButton > button {
        background-color: #00A651 !important;
        color: white !important;
    }

    /* 7. Bottom Feature Cards */
    .feature-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #F0F2F6;
        height: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1 class='main-title'>💙 Quit.To</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>Your journey to a healthier life through incremental harm reduction</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-tagline'>A science-backed 'Slow-Quit' method for smoking, alcohol, and tobacco cessation</p>", unsafe_allow_html=True)

# --- MAIN CARDS SECTION ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="figma-card">
            <div class="icon-box" style="background: #E3F2FD; color: #1D61F2;">👤</div>
            <h2 style="color: #263238;">I'm a Patient</h2>
            <p style="color: #78909C; font-size: 0.95rem;">Start your personalized recovery journey with a 12-week reduction schedule</p>
        </div>
    """, unsafe_allow_html=True)
    # Applying custom class to button via container
    st.markdown('<div class="patient-btn">', unsafe_allow_html=True)
    if st.button("Get Started", key="pt_btn"):
        st.write("Navigating to Patient Portal...")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="figma-card">
            <div class="icon-box" style="background: #E8F5E9; color: #00A651;">💖</div>
            <h2 style="color: #263238;">Healthcare Provider</h2>
            <p style="color: #78909C; font-size: 0.95rem;">Monitor your patients' progress and record health metrics</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="provider-btn">', unsafe_allow_html=True)
    if st.button("Provider Login", key="pr_btn"):
        st.write("Navigating to Provider Portal...")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- BOTTOM FEATURES SECTION ---
f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
        <div class="feature-card" style="border-left: 5px solid #1D61F2;">
            <p style="font-size: 20px;">🚬</p>
            <h4 style="margin-bottom:0;">12-Week Plan</h4>
            <p style="font-size: 0.8rem; color: #90A4AE;">Gradual reduction schedule tailored to your needs</p>
        </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
        <div class="feature-card" style="border-left: 5px solid #00A651;">
            <p style="font-size: 20px;">⚕️</p>
            <h4 style="margin-bottom:0;">Health Tracking</h4>
            <p style="font-size: 0.8rem; color: #90A4AE
