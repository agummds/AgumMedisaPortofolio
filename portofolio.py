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

col1, col2 = st.columns([1,2])
with col1:
    st.write("📧 medisaagum@gmail.com")
with col2:
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
st.markdown("<h2 style='text-align: center;'>Skills</h2>", unsafe_allow_html=True)
empty_col1, col1, col2, empty_col2 = st.columns([1, 3, 3, 1])

st.markdown(
    """
    <style>
        .skill-item {
            transition: all 0.3s ease-in-out;
        }

        .skill-item:hover {
            color: #0077b5; 
            font-weight: bold;
            transform: scale(1.05); 
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with col1:
    st.subheader("💻 Hard Skills")
    st.markdown("""
    <ul>
        <li class='skill-item'>JavaScript</li>
        <li class='skill-item'>AWS</li>
        <li class='skill-item'>SQL</li>
        <li class='skill-item'>Git/GitHub</li>
        <li class='skill-item'>Cloud Computing (GCP)</li>
    </ul>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("🧠 Soft Skills")
    st.markdown("""
    <ul>
        <li class='skill-item'>Growth Mindset</li>
        <li class='skill-item'>Problem Solving</li>
        <li class='skill-item'>Critical Thinking</li>
        <li class='skill-item'>Time Management</li>
    </ul>
    """, unsafe_allow_html=True)

# Sertifikasi
st.markdown(
    "<h2 style='text-align: center;'>Certifications</h2>",
    unsafe_allow_html=True
)

# Bikin empat kolom sejajar
col1, col2, col3, col4 = st.columns(4)

# Kolom 1
with col1:
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/mtcna-300x150.png' width='200'>
            <p>MTCNA Certified</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Kolom 2
with col2:
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='https://th.bing.com/th/id/OIP.04A6c_tsuCs6rjh45RJ03QHaHa?rs=1&pid=ImgDetMain' width='100'>
            <p>Bangkit Academy Certificate</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Kolom 3
with col3:
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/ACA.avif' width='100'>
            <p>Alibaba Cloud Database Certified</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Kolom 4
with col4:
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/aws.png' width='100'>
            <p>AWS Certified Cloud Practitioner</p>
        </div>
        """, 
        unsafe_allow_html=True
    )