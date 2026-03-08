import streamlit as st

st.set_page_config(page_title="QuitTo", page_icon="💙", layout="centered")

# Advanced CSS for Figma-like depth
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main { background-color: #fcfdfe; }
    
    /* Card Styling */
    .custom-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #edf2f7;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .icon-circle {
        width: 60px;
        height: 60px;
        background: #f0f7ff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 15px auto;
        font-size: 30px;
    }
    
    /* Removing Streamlit header padding */
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center; color: #1e3a8a; font-weight: 700;'>💙 Quit.To</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.1rem;'>Your journey to a healthier life through incremental harm reduction</p>", unsafe_allow_html=True)

st.write("##") # Spacing

# Main Selection
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="custom-card">
            <div class="icon-circle" style="background: #eef2ff;">👤</div>
            <h3 style="color: #1e293b; margin-bottom: 10px;">I'm a Patient</h3>
            <p style="color: #64748b; font-size: 0.9rem;">Start your recovery journey with a 12-week schedule.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Get Started", use_container_width=True, type="primary"):
        st.session_state.page = "patient"

with col2:
    st.markdown("""
        <div class="custom-card">
            <div class="icon-circle" style="background: #f0fdf4;">💚</div>
            <h3 style="color: #1e293b; margin-bottom: 10px;">Provider</h3>
            <p style="color: #64748b; font-size: 0.9rem;">Monitor progress and record health metrics.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("Provider Login", use_container_width=True)

st.write("###")

# Features Section
st.markdown("<h4 style='text-align: center; color: #475569;'>Core Features</h4>", unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)

with f1:
    st.info("**12-Week Plan**\nTailored reduction schedule.")
with f2:
    st.success("**Health Tracking**\nReal-time milestones.")
with f3:
    st.warning("**Multiple Addictions**\nSmoking, Alcohol & more.")

