import streamlit as st
import PyPDF2
import io

# Set page config
st.set_page_config(page_title="Resume Builder & Analyzer", layout="centered")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        border-radius: 5px;
        padding: 10px 25px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stTextArea>div>div>textarea {
        border-radius: 5px;
    }
    .resume-section {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .section-title {
        color: #2c3e50;
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .skill-tag {
        background-color: #e9ecef;
        padding: 5px 10px;
        border-radius: 15px;
        margin: 5px;
        display: inline-block;
    }
    .ai-button {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    .score-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .score-high {
        color: #28a745;
    }
    .score-medium {
        color: #ffc107;
    }
    .score-low {
        color: #dc3545;
    }
    .analysis-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #2c3e50;
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    .bot-message {
        background-color: #f5f5f5;
        margin-right: 20%;
    }
    .chat-input {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px;
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📝 Resume Builder & Analyzer")

# Create tabs for different functionalities
tab1, tab2, tab3 = st.tabs(["📝 Build Resume", "🔍 Analyze Resume", "🤖 Career Guide"])

with tab1:
    # Personal Information
    st.header("1. Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
    with col2:
        phone = st.text_input("Phone Number")
        location = st.text_input("Location")

    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL (Optional)")

    # About Me Section
    st.header("2. About Me")
    about_me = st.text_area(
        "Write a brief summary about yourself",
        placeholder="Example:\nPassionate software developer with 2 years of experience in web development. Strong problem-solving skills and a keen eye for detail. Always eager to learn new technologies and contribute to innovative projects."
    )
    if st.button("🤖 Generate About Me", key="about_ai"):
        st.info("AI will help you write a professional summary based on your experience and skills.")

    # Education
    st.header("3. Education")
    education = st.text_area(
        "Add your Education",
        placeholder="Example:\nB.Sc in Computer Science\nXYZ University\n2020-2024\nGPA: 3.8/4.0"
    )
    if st.button("🤖 Enhance Education", key="edu_ai"):
        st.info("AI will help you format your education details professionally.")

    # Work Experience
    st.header("4. Work Experience")
    experience = st.text_area(
        "Describe your Work Experience",
        placeholder="Example:\nSoftware Engineer Intern\nABC Corporation\nJune 2023 - August 2023\n• Developed and maintained web applications\n• Collaborated with team members on project planning"
    )
    if st.button("🤖 Improve Experience", key="exp_ai"):
        st.info("AI will help you write impactful work experience descriptions.")

    # Skills
    st.header("5. Skills")
    skills = st.text_area(
        "List your skills",
        placeholder="Example:\nProgramming Languages: Python, Java, JavaScript\nWeb Technologies: HTML, CSS, React\nTools: Git, Docker, AWS"
    )
    if st.button("🤖 Organize Skills", key="skills_ai"):
        st.info("AI will help you categorize and format your skills effectively.")

    # Projects
    st.header("6. Projects")
    projects = st.text_area(
        "Mention Projects",
        placeholder="Example:\nPortfolio Website\n• Built a responsive personal portfolio using React and Node.js\n• Implemented dark mode and animations\n• Deployed on AWS"
    )
    if st.button("🤖 Enhance Projects", key="projects_ai"):
        st.info("AI will help you write compelling project descriptions.")

    # Generate Resume Button
    if st.button("Generate Resume"):
        if not name or not email or not phone:
            st.error("Please fill in all required fields (Name, Email, Phone)")
        else:
            # Resume Preview
            st.markdown("---")
            st.markdown(f"# {name}")
            st.markdown(f"**Email:** {email} | **Phone:** {phone} | **Location:** {location}")
            if linkedin:
                st.markdown(f"**LinkedIn:** [{linkedin}]({linkedin})")
            if github:
                st.markdown(f"**GitHub:** [{github}]({github})")
            
            st.markdown("---")
            
            # About Me Section
            st.markdown("### 👤 About Me")
            st.markdown(about_me)
            
            # Education Section
            st.markdown("### 🎓 Education")
            st.markdown(education)
            
            # Experience Section
            st.markdown("### 💼 Work Experience")
            st.markdown(experience)
            
            # Skills Section
            st.markdown("### 🛠️ Skills")
            skills_list = [skill.strip() for skill in skills.split('\n') if skill.strip()]
            for skill in skills_list:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
            
            # Projects Section
            st.markdown("### 📌 Projects")
            st.markdown(projects)
            
            st.success("Your resume has been generated above!")
            
            # Copy to Clipboard Button
            st.button("📋 Copy to Clipboard")

with tab2:
    st.header("AI Resume Analyzer")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=['pdf'])
    
    if uploaded_file is not None:
        # Read PDF
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.getvalue()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        if st.button("🔍 Analyze Resume"):
            with st.spinner("Analyzing your resume..."):
                # Initialize analysis results
                analysis = {
                    "Overall Score": 0,
                    "Key Findings": [],
                    "Recommendations": [],
                    "Missing Elements": [],
                    "Strengths": [],
                    "Areas for Improvement": []
                }
                
                # Basic analysis
                sections = {
                    "Contact Information": ["email", "phone", "address", "linkedin"],
                    "Education": ["university", "degree", "gpa", "graduation"],
                    "Experience": ["experience", "work", "job", "employment"],
                    "Skills": ["skills", "technologies", "programming", "tools"],
                    "Projects": ["projects", "portfolio", "applications"]
                }
                
                # Check for sections
                for section, keywords in sections.items():
                    found = any(keyword.lower() in text.lower() for keyword in keywords)
                    if not found:
                        analysis["Missing Elements"].append(f"Missing or unclear {section} section")
                
                # Analyze content length
                if len(text.split()) < 200:
                    analysis["Areas for Improvement"].append("Resume content is too brief")
                elif len(text.split()) > 1000:
                    analysis["Areas for Improvement"].append("Resume content is too lengthy")
                
                # Check for action verbs
                action_verbs = ["developed", "created", "implemented", "managed", "led", "achieved"]
                found_verbs = [verb for verb in action_verbs if verb in text.lower()]
                if found_verbs:
                    analysis["Strengths"].append(f"Good use of action verbs: {', '.join(found_verbs)}")
                
                # Calculate overall score
                base_score = 70
                deductions = len(analysis["Missing Elements"]) * 10
                additions = len(analysis["Strengths"]) * 5
                analysis["Overall Score"] = max(0, min(100, base_score - deductions + additions))
                
                # Display analysis results
                st.markdown("### 📊 Analysis Results")
                
                # Overall Score
                score_color = "score-high" if analysis["Overall Score"] >= 80 else "score-medium" if analysis["Overall Score"] >= 50 else "score-low"
                st.markdown(f"""
                <div class="score-card">
                    <h3>Overall Resume Score</h3>
                    <p class="{score_color}">Score: {analysis['Overall Score']}/100</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Key Findings
                st.markdown("### 🔑 Key Findings")
                for finding in analysis["Strengths"]:
                    st.markdown(f'<div class="analysis-box">✅ {finding}</div>', unsafe_allow_html=True)
                
                # Areas for Improvement
                if analysis["Areas for Improvement"]:
                    st.markdown("### ⚠️ Areas for Improvement")
                    for area in analysis["Areas for Improvement"]:
                        st.markdown(f'<div class="analysis-box">⚠️ {area}</div>', unsafe_allow_html=True)
                
                # Missing Elements
                if analysis["Missing Elements"]:
                    st.markdown("### ❌ Missing Elements")
                    for element in analysis["Missing Elements"]:
                        st.markdown(f'<div class="analysis-box">❌ {element}</div>', unsafe_allow_html=True)
                
                # Recommendations
                st.markdown("### 💡 Recommendations")
                if analysis["Missing Elements"]:
                    st.markdown("1. Add the missing sections to make your resume more complete")
                if len(text.split()) < 200:
                    st.markdown("2. Add more details to your experience and achievements")
                if len(text.split()) > 1000:
                    st.markdown("3. Consider making your resume more concise")
                if not found_verbs:
                    st.markdown("4. Use more action verbs to describe your achievements")
                
                st.success("Analysis complete! Review the results above to improve your resume.")

with tab3:
    st.header("AI Career Guide")
    
    # Career field selection
    career_field = st.selectbox(
        "Select your career field",
        ["Software Development", "Data Science", "Web Development", "Mobile Development", 
         "DevOps", "UI/UX Design", "Product Management", "Other"]
    )
    
    # Experience level
    experience_level = st.selectbox(
        "Select your experience level",
        ["Student", "Entry Level", "Mid Level", "Senior Level"]
    )

    # Display career insights based on selection
    st.markdown("### 📊 Career Insights")
    
    # Career path information
    career_paths = {
        "Software Development": {
            "Entry Level": "• Junior Software Developer\n• Software Engineer I\n• Associate Developer",
            "Mid Level": "• Software Engineer II\n• Senior Developer\n• Technical Lead",
            "Senior Level": "• Senior Software Engineer\n• Principal Engineer\n• Technical Architect"
        },
        "Data Science": {
            "Entry Level": "• Junior Data Analyst\n• Data Science Intern\n• Business Analyst",
            "Mid Level": "• Data Scientist\n• Machine Learning Engineer\n• Analytics Lead",
            "Senior Level": "• Senior Data Scientist\n• ML Architect\n• Data Science Manager"
        },
        "Web Development": {
            "Entry Level": "• Junior Web Developer\n• Frontend Developer\n• Web Developer Intern",
            "Mid Level": "• Full Stack Developer\n• Senior Web Developer\n• Technical Lead",
            "Senior Level": "• Lead Web Developer\n• Web Architect\n• Technical Director"
        }
    }

    # Display career path
    if career_field in career_paths:
        st.markdown("#### 🎯 Career Path")
        st.markdown(career_paths[career_field].get(experience_level, "Career path information coming soon..."))

    # Required skills and technologies
    st.markdown("#### 🛠️ Required Skills")
    skills_info = {
        "Software Development": {
            "Entry Level": "• Programming fundamentals\n• Basic algorithms\n• Version control (Git)\n• One programming language (Python/Java/JavaScript)",
            "Mid Level": "• Multiple programming languages\n• System design\n• Testing methodologies\n• CI/CD practices",
            "Senior Level": "• Architecture design\n• Team leadership\n• Performance optimization\n• Security best practices"
        },
        "Data Science": {
            "Entry Level": "• Python/R programming\n• Basic statistics\n• Data visualization\n• SQL basics",
            "Mid Level": "• Machine learning\n• Big data tools\n• Advanced statistics\n• Data engineering",
            "Senior Level": "• Deep learning\n• MLOps\n• Research methodology\n• Team management"
        },
        "Web Development": {
            "Entry Level": "• HTML/CSS/JavaScript\n• Basic frontend frameworks\n• Responsive design\n• Version control",
            "Mid Level": "• Full stack development\n• Database design\n• API development\n• Testing",
            "Senior Level": "• System architecture\n• Performance optimization\n• Security\n• Team leadership"
        }
    }

    if career_field in skills_info:
        st.markdown(skills_info[career_field].get(experience_level, "Skills information coming soon..."))

    # Learning resources
    st.markdown("#### 📚 Learning Resources")
    resources = {
        "Software Development": {
            "Entry Level": "• Codecademy - Programming fundamentals\n• freeCodeCamp - Full stack development\n• LeetCode - Coding practice\n• GitHub - Open source projects",
            "Mid Level": "• Coursera - Advanced programming\n• Udemy - Specialized courses\n• Pluralsight - Professional development\n• System Design Primer",
            "Senior Level": "• Design Patterns\n• Clean Code by Robert Martin\n• System Design Interview\n• Leadership courses"
        },
        "Data Science": {
            "Entry Level": "• DataCamp - Data science fundamentals\n• Kaggle - Practice datasets\n• Fast.ai - Practical deep learning\n• Python for Data Analysis",
            "Mid Level": "• Coursera - Machine Learning\n• Deep Learning Specialization\n• Data Engineering courses\n• Statistics and Mathematics",
            "Senior Level": "• Advanced ML courses\n• Research papers\n• MLOps resources\n• Leadership training"
        },
        "Web Development": {
            "Entry Level": "• MDN Web Docs\n• freeCodeCamp - Web development\n• Frontend Masters\n• CSS-Tricks",
            "Mid Level": "• Full Stack Open\n• Advanced JavaScript\n• Database design courses\n• API development",
            "Senior Level": "• System design resources\n• Performance optimization\n• Security best practices\n• Leadership courses"
        }
    }

    if career_field in resources:
        st.markdown(resources[career_field].get(experience_level, "Learning resources coming soon..."))

    # Job market insights
    st.markdown("#### 💼 Job Market Insights")
    st.markdown("""
    • Average salary ranges for your level
    • Top companies hiring in this field
    • Remote work opportunities
    • Industry growth trends
    """)

    # Interactive chat section
    st.markdown("### 💬 Ask Career Questions")
    user_question = st.text_input("Ask specific questions about your career path", key="career_question")
    
    if user_question:
        # Process the question and provide relevant guidance
        if "salary" in user_question.lower():
            st.markdown("""
            **Salary Insights:**
            • Entry Level: $60,000 - $80,000
            • Mid Level: $80,000 - $120,000
            • Senior Level: $120,000 - $200,000+
            
            Note: Salaries vary based on location, company size, and specific skills.
            """)
        elif "interview" in user_question.lower():
            st.markdown("""
            **Interview Preparation Tips:**
            1. Practice coding problems
            2. Review system design concepts
            3. Prepare behavioral questions
            4. Research the company
            5. Build a portfolio
            """)
        elif "skills" in user_question.lower():
            st.markdown("""
            **Essential Skills Development:**
            1. Technical skills
            2. Soft skills
            3. Problem-solving
            4. Communication
            5. Team collaboration
            """)
        else:
            st.markdown("""
            I can help you with:
            • Salary expectations
            • Interview preparation
            • Skill development
            • Career progression
            • Learning resources
            
            Please ask a specific question about any of these topics.
            """)

    # Quick action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💡 Get Skill Roadmap"):
            st.markdown("### Skill Development Roadmap")
            st.markdown("""
            1. **Foundation Skills**
               - Basic programming
               - Problem solving
               - Version control
            
            2. **Intermediate Skills**
               - Advanced programming
               - System design
               - Testing
            
            3. **Advanced Skills**
               - Architecture
               - Leadership
               - Performance optimization
            """)
    with col2:
        if st.button("🎯 Career Progression"):
            st.markdown("### Career Progression Path")
            st.markdown("""
            1. **Entry Level (0-2 years)**
               - Focus on learning
               - Build projects
               - Get mentorship
            
            2. **Mid Level (2-5 years)**
               - Take ownership
               - Mentor others
               - Lead small projects
            
            3. **Senior Level (5+ years)**
               - Lead teams
               - Drive architecture
               - Strategic planning
            """)
    with col3:
        if st.button("📚 Learning Path"):
            st.markdown("### Recommended Learning Path")
            st.markdown("""
            1. **Online Courses**
               - Coursera
               - Udemy
               - edX
            
            2. **Practice Platforms**
               - LeetCode
               - HackerRank
               - Project work
            
            3. **Community**
               - GitHub
               - Stack Overflow
               - Tech meetups
            """) 