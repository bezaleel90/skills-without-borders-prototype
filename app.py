"""
Skills Without Borders (SWB) - Main Application
A Pan-African Human Capital Mobility Framework
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Skills Without Borders",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    try:
        with open('static/css/style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# Initialize session state
def init_session():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'notifications' not in st.session_state:
        st.session_state.notifications = []

# Main navigation
def main():
    load_css()
    init_session()
    
    # Sidebar
    with st.sidebar:
        try:
            st.image('static/images/logo.png', use_column_width=True)
        except Exception:
            pass
        st.markdown("---")
        
        if st.session_state.authenticated:
            st.markdown(f"### 👋 Welcome, {st.session_state.user.get('full_name', 'User')}")
            st.markdown(f"**Role:** {st.session_state.user.get('role', 'Worker')}")
            st.markdown("---")
            
            # Navigation
            nav_options = {
                "🏠 Dashboard": "dashboard",
                "📋 My Skills Passport": "skills_passport",
                "🔒 Verification": "verification",
                "💼 Opportunities": "opportunities",
                "📚 Learning Pathways": "learning",
                "👥 Community": "community",
                "⚙️ Settings": "settings"
            }
            
            if st.session_state.user.get('role') == 'admin':
                nav_options["👑 Admin Panel"] = "admin"
            
            for label, page in nav_options.items():
                if st.button(label, use_container_width=True):
                    st.session_state.page = page
                    st.rerun()
            
            st.markdown("---")
            if st.button("🚪 Sign Out", use_container_width=True):
                from utils.auth import sign_out
                sign_out()
                st.rerun()
        else:
            st.markdown("### 🌍 Skills Without Borders")
            st.markdown("Making Skills Visible, Trusted, and Transferable")
            st.markdown("---")
            
            if st.button("🚀 Get Started", use_container_width=True):
                st.session_state.page = "signup"
                st.rerun()
            if st.button("🔑 Sign In", use_container_width=True):
                st.session_state.page = "signin"
                st.rerun()
    
    # Route to appropriate page
    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "signup":
        try:
            from pages.auth import signup_page
            signup_page()
        except Exception:
            st.info('Signup page not implemented yet')
    elif st.session_state.page == "signin":
        try:
            from pages.auth import signin_page
            signin_page()
        except Exception:
            st.info('Signin page not implemented yet')
    elif st.session_state.page == "dashboard":
        from pages.dashboard import dashboard_page
        dashboard_page()
    elif st.session_state.page == "skills_passport":
        from pages.skills_passport import skills_passport_page
        skills_passport_page()
    elif st.session_state.page == "verification":
        try:
            from pages.verification import verification_page
            verification_page()
        except Exception:
            st.info('Verification page not implemented yet')
    elif st.session_state.page == "opportunities":
        from pages.opportunities import opportunities_page
        opportunities_page()
    elif st.session_state.page == "learning":
        try:
            from pages.learning import learning_page
            learning_page()
        except Exception:
            st.info('Learning page not implemented yet')
    elif st.session_state.page == "community":
        try:
            from pages.community import community_page
            community_page()
        except Exception:
            st.info('Community page not implemented yet')
    elif st.session_state.page == "settings":
        try:
            from pages.settings import settings_page
            settings_page()
        except Exception:
            st.info('Settings page not implemented yet')
    elif st.session_state.page == "admin":
        try:
            from pages.admin import admin_page
            admin_page()
        except Exception:
            st.info('Admin page not implemented yet')

def home_page():
    """Landing page"""
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 3.5rem; color: #1a73e8;">🌍 Skills Without Borders</h1>
        <p style="font-size: 1.5rem; color: #555; margin: 20px 0;">
            Making Skills Visible, Trusted, and Transferable Across Africa
        </p>
        <p style="font-size: 1.1rem; max-width: 800px; margin: 0 auto; color: #666;">
            A Pan-African Human Capital Mobility Framework aligned with 
            <strong>AU Agenda 2063</strong> &amp; <strong>UN Sustainable Development Goals</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats
    col1, col2, col3, col4 = st.columns(4)
    
    stats = [
        {"icon": "👨‍🎓", "number": "60%", "label": "Youth Population", "color": "#1a73e8"},
        {"icon": "🏢", "number": "85%", "label": "Informal Employment", "color": "#34a853"},
        {"icon": "🌍", "number": "54", "label": "African Countries", "color": "#fbbc04"},
        {"icon": "📈", "number": "100M+", "label": "Potential Workers", "color": "#ea4335"}
    ]
    
    for idx, stat in enumerate(stats):
        with [col1, col2, col3, col4][idx]:
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 10px; 
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 2.5rem;">{stat['icon']}</div>
                <div style="font-size: 2rem; font-weight: bold; color: {stat['color']};">{stat['number']}</div>
                <div style="color: #666;">{stat['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")

    if __name__ == "__main__":
        main()
