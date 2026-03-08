import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# Page Config (Mobile-first look)
st.set_page_config(page_title="QuitTo", page_icon="💙", layout="centered")

# Custom CSS for Figma Styles
st.markdown("""
    <style>
    .main { background-color: #f8faff; }
    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {
        text-align: center;
    }
    .tagline {
        color: #666;
        font-size: 18px;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Logo and Header
st.markdown("<h1 style='text-align: center; color: #1a73e8;'>💙 Quit.To</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>Your journey to a healthier life through incremental harm reduction</p>", unsafe_allow_html=True)

# 2. Main Selection Cards (Patient vs Provider)
col1, col2 = st.columns(2)

with col1:
    with stylable_container(
        key="patient_container",
        css_styles="""{ border: 1px solid #e0e0e0; border-radius: 15px; padding: 20px; background: white; text-align: center; }""",
    ):
        st.markdown("👤")
        st.subheader("I'm a Patient")
        st.write("Start your personalized recovery journey.")
        if st.button("Get Started", key="btn_patient", use_container_width=True):
            st.session_state.page = "patient_form"

with col2:
    with stylable_container(
        key="provider_container",
        css_styles="""{ border: 1px solid #e0e0e0; border-radius: 15px; padding: 20px; background: white; text-align: center; }""",
    ):
        st.markdown("💚")
        st.subheader("Healthcare Provider")
        st.write("Monitor your patients' progress.")
        st.button("Provider Login", key="btn_provider", use_container_width=True)

# 3. Features Section (Bottom Row)
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1:
    st.info("**12-Week Plan**\nTailored reduction schedule.")
with f2:
    st.success("**Health Tracking**\nReal-time milestones.")
with f3:
    st.warning("**Multiple Addictions**\nSmoking, Alcohol & more.")
