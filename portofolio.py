import streamlit as st

dark_mode = st.toggle("Dark Mode", value=False)

bg_color = "#000000" if dark_mode else "#FFFFFF"
text_color = "#FFFFFF" if dark_mode else "#000000"

# Styling untuk background putih
st.markdown("""
    <style>
        body, .main {
            transition: background-color 0.3s, color 0.3s;
        }

        /* Mode Terang */
        :root {
            --bg-color: white;
            --text-color: black;
        }

        /* Mode Gelap */
        @media (prefers-color-scheme: dark) {
            :root {
                --bg-color: black;
                --text-color: white;
            }
        }

        /* Terapkan ke seluruh halaman */
        .main {
            background-color: var(--bg-color) !important;
        }

        h1, h2, h3, h4, h5, h6, p, div, span {
            color: var(--text-color) !important;
        }
    </style>
""", unsafe_allow_html=True)

# Styling untuk foto profil
st.markdown(
    """
    <style>
        .profile-pic {
            display: block;
            border-radius: 50%; /* Bikin foto jadi bulat */
            width: 150px;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        .profile-pic:hover {
            transform: scale(1.1); /* Foto jadi sedikit membesar */
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2); /* Efek bayangan */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Bikin dua kolom: Foto di kiri, info di kanan
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(
        """
            <img src='https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/agum.jpg' width='400'>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.title("Agum Medisa")
    st.write("Padang, West Sumatera")

    # Email dengan ikon
    st.markdown(
        """
        <div style='display: flex; align-items: center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png' width='20' style='margin-right: 8px;'/>
            <span>medisaagum@gmail.com</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # LinkedIn dengan ikon + custom warna link
    st.markdown(
        """
        <style>
            .custom-link {
                text-decoration: none;
                font-weight: bold;
            }

            .custom-link:hover {
                text-decoration: underline;
            }
        </style>
        <div style='display: flex; align-items: center;'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='20' style='margin-right: 8px;'/>
            <a href='https://www.linkedin.com/in/agummedisa' target='_blank' class='custom-link'>LinkedIn Profile</a>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        .custom-header-container {
            text-align: center; /* Pusatkan teks */
        }

        .custom-header {
            position: relative;
            display: inline-block; /* Ukuran elemen hanya selebar teks */
            font-size: 24px;
            font-family: 'Poppins', sans-serif;
            font-weight: normal;
            cursor: pointer;
            padding-bottom: 2px;
            margin-bottom: 16px;
        }

        .custom-header::after {
            content: '';
            position: absolute;
            width: 100%; /* Lebar garis pas sama teks */
            height: 2px;
            background-color: black;
            bottom: -4px; /* Geser garis biar pas */
            left: 0; /* Mulai dari kiri elemen */
            transform: scaleX(1); /* Garis awal penuh */
            transition: transform 0.3s ease-in-out;
        }

        .custom-header:hover::after {
            transform: scaleX(0); /* Garis menghilang saat hover */
        }

        .custom-header:hover {
            font-weight: bold;
        }
    </style>
    <div class='custom-header-container'>
        <h2 class='custom-header'>Summary</h2>
    </div>
    """,
    unsafe_allow_html=True
)


st.write("Final-year Computer Engineering student passionate about Cloud Engineering and Software Development.")
st.write("Gained hands-on experience in cloud computing and networking through the Bangkit Academy program.")
st.write("AWS & Alibaba Cloud certified, with expertise in cloud technology and a strong drive to solve real-world tech challenges.")

# Pendidikan
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        .custom-header-container {
            text-align: center; /* Pusatkan teks */
        }

        .custom-header {
            position: relative;
            display: inline-block; /* Ukuran elemen hanya selebar teks */
            font-size: 24px;
            font-family: 'Poppins', sans-serif;
            font-weight: normal;
            cursor: pointer;
            padding-bottom: 2px;
            margin-bottom: 16px;
        }

        .custom-header::after {
            content: '';
            position: absolute;
            width: 100%; /* Lebar garis pas sama teks */
            height: 2px;
            background-color: black;
            bottom: -4px; /* Geser garis biar pas */
            left: 0; /* Mulai dari kiri elemen */
            transform: scaleX(1); /* Garis awal penuh */
            transition: transform 0.3s ease-in-out;
        }

        .custom-header:hover::after {
            transform: scaleX(0); /* Garis menghilang saat hover */
        }

        .custom-header:hover {
            font-weight: bold;
        }
    </style>
    <div class='custom-header-container'>
        <h2 class='custom-header'>Education</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("**Andalas University** - Computer Engineering Student (July 2021 - Present)")
st.write("Active student with experience in computer networks, embedded systems, and cloud computing.")

# Pengalaman
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        .custom-header-container {
            text-align: center; /* Pusatkan teks */
        }

        .custom-header {
            position: relative;
            display: inline-block; /* Ukuran elemen hanya selebar teks */
            font-size: 24px;
            font-family: 'Poppins', sans-serif;
            font-weight: normal;
            cursor: pointer;
            padding-bottom: 2px;
            margin-bottom: 16px;
        }

        .custom-header::after {
            content: '';
            position: absolute;
            width: 100%; /* Lebar garis pas sama teks */
            height: 2px;
            background-color: black;
            bottom: -4px; /* Geser garis biar pas */
            left: 0; /* Mulai dari kiri elemen */
            transform: scaleX(1); /* Garis awal penuh */
            transition: transform 0.3s ease-in-out;
        }

        .custom-header:hover::after {
            transform: scaleX(0); /* Garis menghilang saat hover */
        }

        .custom-header:hover {
            font-weight: bold;
        }
    </style>
    <div class='custom-header-container'>
        <h2 class='custom-header'>Experience</h2>
    </div>
    """,
    unsafe_allow_html=True
)

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
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        .custom-header-container {
            text-align: center; /* Pusatkan teks */
        }

        .custom-header {
            position: relative;
            display: inline-block; /* Ukuran elemen hanya selebar teks */
            font-size: 24px;
            font-family: 'Poppins', sans-serif;
            font-weight: normal;
            cursor: pointer;
            padding-bottom: 2px;
            margin-bottom: 16px;
        }

        .custom-header::after {
            content: '';
            position: absolute;
            width: 100%; /* Lebar garis pas sama teks */
            height: 2px;
            background-color: black;
            bottom: -4px; /* Geser garis biar pas */
            left: 0; /* Mulai dari kiri elemen */
            transform: scaleX(1); /* Garis awal penuh */
            transition: transform 0.3s ease-in-out;
        }

        .custom-header:hover::after {
            transform: scaleX(0); /* Garis menghilang saat hover */
        }

        .custom-header:hover {
            font-weight: bold;
        }
    </style>
    <div class='custom-header-container'>
        <h2 class='custom-header'>Projects</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("**Web Server Building Project**")
st.write("- Scalable web server architecture with NGINX and Node.js backend.")
st.write("- Automated CI/CD pipeline with GitHub Actions & Docker.")

st.write("**Open Music**")
st.write("- Designed RESTful API for playlist management with JWT authentication.")

st.write("**Money Tracker App**")
st.write("- Built financial tracking app using Google App Engine and Cloud Storage.")

# Skills

# Skills
st.markdown("<h2 class='custom-header'>Skills</h2>", unsafe_allow_html=True)
empty_col1, col1, col2, empty_col2 = st.columns([1, 3, 3, 1])

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        .custom-header-container {
            text-align: center; /* Pusatkan teks */
        }

        .custom-header {
            position: relative;
            display: inline-block; /* Ukuran elemen hanya selebar teks */
            font-size: 24px;
            font-family: 'Poppins', sans-serif;
            font-weight: normal;
            cursor: pointer;
            padding-bottom: 2px;
            margin-bottom: 16px;
        }

        .custom-header::after {
            content: '';
            position: absolute;
            width: 100%; /* Lebar garis pas sama teks */
            height: 2px;
            background-color: black;
            bottom: -4px; /* Geser garis biar pas */
            left: 0; /* Mulai dari kiri elemen */
            transform: scaleX(1); /* Garis awal penuh */
            transition: transform 0.3s ease-in-out;
        }

        .custom-header:hover::after {
            transform: scaleX(0); /* Garis menghilang saat hover */
        }

        .custom-header:hover {
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with col1:
    st.subheader("💻 Hard Skills")
    st.markdown("""
    <ul style='text-align: left;'>
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
    <ul style='text-align: left;'>
        <li class='skill-item'>Growth Mindset</li>
        <li class='skill-item'>Problem Solving</li>
        <li class='skill-item'>Critical Thinking</li>
        <li class='skill-item'>Time Management</li>
    </ul>
    """, unsafe_allow_html=True)

# Sertifikasi

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        .custom-header-container {
            text-align: center; /* Pusatkan teks */
        }

        .custom-header {
            position: relative;
            display: inline-block; /* Ukuran elemen hanya selebar teks */
            font-size: 24px;
            font-family: 'Poppins', sans-serif;
            font-weight: normal;
            cursor: pointer;
            padding-bottom: 2px;
            margin-bottom: 16px;
        }

        .custom-header::after {
            content: '';
            position: absolute;
            width: 100%; /* Lebar garis pas sama teks */
            height: 2px;
            background-color: black;
            bottom: -4px; /* Geser garis biar pas */
            left: 0; /* Mulai dari kiri elemen */
            transform: scaleX(1); /* Garis awal penuh */
            transition: transform 0.3s ease-in-out;
        }

        .custom-header:hover::after {
            transform: scaleX(0); /* Garis menghilang saat hover */
        }

        .custom-header:hover {
            font-weight: bold;
        }
    </style>
    <div class='custom-header-container'>
        <h2 class='custom-header'>Certification</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Baris pertama: Empat kolom sejajar
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

# Baris kedua: Satu kolom di tengah
col_left, col_center, col_right = st.columns([2, 1, 2])

# Kolom 5 (di tengah)
with col_center:
    st.image(
        "https://raw.githubusercontent.com/agummds/AgumMedisaPortofolio/master/image/ITS-Badges_Python_1200px.png",
        caption="IT Specialist - Python",
        width=100
    )
