"""
Skills Passport management page (minimal prototype)
"""
import streamlit as st
from utils.skills import SkillsManager, SkillsTaxonomy

def skills_passport_page():
    user = st.session_state.user or {"id": "demo_user"}
    skills_manager = SkillsManager(user['id'])
    st.header('My Skills Passport')
    passport = skills_manager.get_passport()
    if not passport['success']:
        st.info('No passport found. Use the Quick Start to create one.')
    else:
        st.write(passport['data'])
