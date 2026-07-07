"""
User dashboard for Skills Without Borders
"""
import streamlit as st
from utils.skills import SkillsManager, SkillsTaxonomy

def dashboard_page():
    user = st.session_state.user or {"id": "demo_user", "full_name": "Demo User"}
    skills_manager = SkillsManager(user['id'])
    st.markdown("""
    <div style="padding: 20px 0;">
        <h1 style="font-size: 2.5rem; color: #1a73e8;">📊 Dashboard</h1>
        <p style="color: #666; font-size: 1.1rem;">Track your skills, verification status, and opportunities</p>
    </div>
    """, unsafe_allow_html=True)
    passport = skills_manager.get_passport()
    score = {"total": 0, "breakdown": {}}
    try:
        score = skills_manager.calculate_skill_score()
    except Exception:
        pass
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1a73e8, #0d47a1); padding: 20px; border-radius: 10px; color: white; text-align: center;">
            <div style="font-size: 0.9rem; opacity: 0.8;">Profile Completion</div>
            <div style="font-size: 2.5rem; font-weight: bold;">{int(score.get('total',0))}%</div>
            <div style="font-size: 0.8rem; opacity: 0.8;">Skills documented</div>
        </div>
        """, unsafe_allow_html=True)
    st.info('This is a minimal dashboard page for the prototype')
