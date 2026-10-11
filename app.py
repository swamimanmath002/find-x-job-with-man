import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Find X Job With Man", 
    page_icon="💼", 
    layout="wide"
)

# Sidebar - Creator Info
with st.sidebar:
    st.image("https://img.icons8.com/color/96/developer.png", width=80)
    st.title("Creator Profile")
    st.markdown("### **Manmath Swami**")
    st.write("AI & ML Student & Developer")
    st.markdown("---")
    st.info("Tip: Paste your text summary to instantly analyze your skill match score!")

# Main App Header
st.title("💼 Find X Job With Man")
st.subheader("🚀 AI Resume Analyzer & Skill Suggestion Tool")
st.write("Upload your resume details below to evaluate your skill match, discover missing skills, and boost your hiring chances!")

st.divider()

# Job Role Selection
job_role = st.selectbox(
    "🎯 Select Target Job Role:",
    ["Python Developer", "Data Analyst", "AI / ML Engineer", "Web Developer"]
)

# Resume Text Input Area
resume_text = st.text_area(
    "📄 Paste your resume summary / skills text here:", 
    height=180, 
    placeholder="e.g., Proficient in Python, SQL, Git, problem-solving, and building web apps..."
)

# Analysis Button
if st.button("Analyze Resume Now ⚡"):
    if not resume_text.strip():
        st.warning("⚠️ Please paste your resume text before clicking analyze!")
    else:
        st.subheader("📊 Comprehensive Analysis Report")
        
        # Required Skills Database
        required_skills = {
            "Python Developer": ["python", "django", "flask", "sql", "git", "api"],
            "Data Analyst": ["python", "sql", "power bi", "excel", "pandas", "tableau"],
            "AI / ML Engineer": ["python", "numpy", "pandas", "scikit-learn", "tensorflow", "deep learning"],
            "Web Developer": ["html", "css", "javascript", "react", "git", "bootstrap"]
        }
        
        role_skills = required_skills.get(job_role, [])
        found_skills = [skill for skill in role_skills if skill in resume_text.lower()]
        missing_skills = [skill for skill in role_skills if skill not in resume_text.lower()]
        
        # Score Calculation
        if len(role_skills) > 0:
            score = int((len(found_skills) / len(role_skills)) * 100)
        else:
            score = 0
        
        # Display Score Meter
        st.metric(label="🎯 Resume Match Score", value=f"{score}%")
        st.progress(score)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("✅ Skills Matched:")
            if found_skills:
                for skill in found_skills:
                    st.write(f"✔️ {skill.title()}")
            else:
                st.write("No core skills found in the text.")
                
        with col2:
            st.error("❌ Missing Skills to Learn:")
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"❌ {skill.title()}")
            else:
                st.write("Fantastic! Your resume covers all core skills.")
                
        st.divider()
        st.subheader("💡 AI Suggestions & Next Steps")
        if missing_skills:
            st.info(f"To boost your score, consider learning and adding these skills: **{', '.join([s.title() for s in missing_skills])}**")
        else:
            st.success("Your resume looks exceptionally strong for this role!")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Developed with ❤️ by Manmath Swami | Find X Job With Man</p>", 
    unsafe_allow_html=True
)