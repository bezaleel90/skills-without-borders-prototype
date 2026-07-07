"""
Skills management utilities for Skills Without Borders
"""
import streamlit as st
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
from utils.supabase_client import execute_query

class SkillsManager:
    def __init__(self, user_id: str):
        self.user_id = user_id
    def create_passport(self, data: Dict) -> Dict:
        passport_data = {
            "user_id": self.user_id,
            "qualifications": json.dumps(data.get("qualifications", [])),
            "competencies": json.dumps(data.get("competencies", [])),
            "work_experience": json.dumps(data.get("work_experience", [])),
            "apprenticeships": json.dumps(data.get("apprenticeships", [])),
            "entrepreneurship": json.dumps(data.get("entrepreneurship", {})),
            "informal_learning": json.dumps(data.get("informal_learning", [])),
            "certifications": json.dumps(data.get("certifications", [])),
            "verification_status": "pending",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        result = execute_query("skills_passports", "insert", passport_data)
        if result["success"]:
            return {"success": True, "data": result["data"][0] if result["data"] else None}
        return {"success": False, "error": result["error"]}
    def get_passport(self) -> Dict:
        result = execute_query("skills_passports", "select", filters={"user_id": self.user_id})
        if result["success"] and result["data"]:
            passport = result["data"][0]
            try:
                passport["qualifications"] = json.loads(passport.get("qualifications", "[]"))
                passport["competencies"] = json.loads(passport.get("competencies", "[]"))
            except Exception:
                # If values are already lists, ignore
                pass
            return {"success": True, "data": passport}
        return {"success": False, "data": None}
    def update_passport(self, data: Dict) -> Dict:
        data["updated_at"] = datetime.now().isoformat()
        for field in ["qualifications", "competencies", "work_experience", "apprenticeships", "informal_learning", "certifications"]:
            if field in data and isinstance(data[field], (list, dict)):
                data[field] = json.dumps(data[field])
        result = execute_query("skills_passports", "update", data, filters={"user_id": self.user_id})
        if result["success"]:
            return {"success": True, "data": result["data"][0] if result["data"] else None}
        return {"success": False, "error": result["error"]}
    def add_skill(self, skill: Dict) -> Dict:
        passport = self.get_passport()
        if not passport["success"]:
            return {"success": False, "error": "Passport not found"}
        skills = passport["data"].get("competencies", [])
        skills.append(skill)
        return self.update_passport({"competencies": skills})

class SkillsTaxonomy:
    SKILLS_CATEGORIES = {
        "Technical Skills": [
            "Solar Installation", "Electrical Systems", "Mechanical Repair",
            "Construction", "Plumbing", "Carpentry", "Welding",
            "ICT Support", "Software Development", "Data Analysis",
            "Digital Marketing", "Graphic Design", "Video Production"
        ],
        "Agricultural Skills": [
            "Crop Farming", "Livestock Management", "Agro-processing",
            "Irrigation Systems", "Soil Management", "Pest Control",
            "Sustainable Farming", "Value Addition"
        ],
        "Business Skills": [
            "Entrepreneurship", "Business Planning", "Financial Management",
            "Marketing", "Sales", "Customer Service", "Project Management",
            "Supply Chain", "Inventory Management", "Accounting"
        ],
        "Soft Skills": [
            "Communication", "Leadership", "Problem Solving",
            "Teamwork", "Adaptability", "Time Management",
            "Critical Thinking", "Emotional Intelligence", "Creativity"
        ],
        "Digital Skills": [
            "Digital Literacy", "Data Analytics", "AI Fundamentals",
            "Cybersecurity", "Cloud Computing", "Mobile App Development",
            "E-commerce", "Social Media Management", "Content Creation"
        ]
    }
    @classmethod
    def get_all_skills(cls) -> List[str]:
        skills = []
        for _, items in cls.SKILLS_CATEGORIES.items():
            skills.extend(items)
        return skills
    @classmethod
    def get_category(cls, skill: str) -> Optional[str]:
        for category, skills in cls.SKILLS_CATEGORIES.items():
            if skill in skills:
                return category
        return None
