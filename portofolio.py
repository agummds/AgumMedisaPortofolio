import streamlit as st

# Styling untuk background putih
st.markdown("""
    <style>
        .main { background-color: #ffffff; }
        h1, h2, h3, h4, h5, h6, p, div, span { color: #000000 !important; }
    </style>
""", unsafe_allow_html=True)

# Informasi Pribadi
st.title("Agum Medisa")
st.write("Padang, West Sumatera")
st.write("📧 medisaagum@gmail.com")
st.write("[LinkedIn](https://www.linkedin.com/in/agummedisa)")

# Summary
st.header("Summary")
st.write("Final-year Computer Engineering student passionate about Cloud Engineering and Software Development.")
st.write("Gained hands-on experience in cloud computing and networking through the Bangkit Academy program.")
st.write("AWS & Alibaba Cloud certified, with expertise in cloud technology and a strong drive to solve real-world tech challenges.")

# Pendidikan
st.header("Education")
st.write("**Andalas University** - Computer Engineering Student (July 2021 - Present)")
st.write("Active student with experience in computer networks, embedded systems, and cloud computing.")

# Pengalaman
st.header("Experience")

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://th.bing.com/th/id/OIP.w98CGrXq5S_JRyxgBGmFMQHaFj?rs=1&pid=ImgDetMain", width=100)
with col2:
    st.write("**DevOps Intern - DTI UNAND** (Jan 2025 - Feb 2025)")
    st.write("- Developed and deployed applications using Docker and Docker Compose.")
    st.write("- Implemented CI/CD principles for automated builds and deployments.")
    st.write("- Utilized Prometheus and Grafana for application monitoring.")

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://movielabs.com/wp-content/uploads/2022/10/aws-logo-png-4.png", width=100)
with col2:
    st.write("**AWS re/Start Program** (Oct 2024 - Dec 2024)")
    st.write("- Completed the program with 96% attendance rate.")
    st.write("- Achieved AWS Certified Cloud Practitioner certification.")

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://th.bing.com/th/id/OIP.04A6c_tsuCs6rjh45RJ03QHaHa?rs=1&pid=ImgDetMain", width=100)
with col2:
    st.write("**Bangkit Academy Cloud Computing Cohort** (Aug 2023 - Dec 2023)")
    st.write("- Developed proficiency in GCP cloud services and built web applications.")

# Proyek
st.header("Projects")
st.write("**Web Server Building Project**")
st.write("- Scalable web server architecture with NGINX and Node.js backend.")
st.write("- Automated CI/CD pipeline with GitHub Actions & Docker.")

st.write("**Open Music**")
st.write("- Designed RESTful API for playlist management with JWT authentication.")

st.write("**Money Tracker App**")
st.write("- Built financial tracking app using Google App Engine and Cloud Storage.")

# Skills
st.header("Skills")
st.write("- **Hard Skills:** JavaScript, AWS, SQL, Git/GitHub, Cloud Computing (GCP)")
st.write("- **Soft Skills:** Growth Mindset, Problem Solving, Critical Thinking, Time Management")

# Sertifikasi
st.header("Certifications")

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/mtcna-300x150.png", width=50)
with col2:
    st.write("- MTCNA Certified")

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://th.bing.com/th/id/OIP.04A6c_tsuCs6rjh45RJ03QHaHa?rs=1&pid=ImgDetMain", width=50)
with col2:
    st.write("- Bangkit Academy Certificate")

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/ACA.avif", width=50)
with col2:
    st.write("- Alibaba Cloud Database Certified")

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/aws.png", width=50)
with col2:
    st.write("- AWS Certified Cloud Practitioner")
