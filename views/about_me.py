import streamlit as st


# -----------intiliazing content----------
name = "Anuj Kumar"
description = "Senior RPA AI Developer at IQVIA | Automation Anywhere Developer | Power Apps | Power Automate Developer | Azure AI"
email = "anuj89822@gmail.com"
mobileNo="+91 8982280835"

social_media = {
    "YouTube": "https://www.youtube.com/channel/UCDKIlFseCDdfXhNQ4linbEg",
    "LinkedIn":"https://www.linkedin.com/in/anuj-kumar-rpa/",
}
# ------Reading files -------
with open("./assets/resume_anuj_RPA.pdf", "rb") as pdf_file:
    PDFByte = pdf_file.read()

with open("./styles/main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --------------Creating Dialog-----
@st.dialog("Contact Me")
def contact_form():
    st.html(f"<b>Mail ID:</b> 📧 {email}")
    st.html(f"<b>Mobile Number:</b> 📞 {mobileNo}")
    st.html("<b>Linkdin Profile:</b> <a href = 'https://www.linkedin.com/in/anuj-kumar-rpa/'> 🧑Click Me</a>")

# -------Hero section----

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/my_pic2.png", width=230)
with col2:
    st.title(name, anchor=False)
    st.write(description)
    st.download_button(
        label = " 📃 Download Resume",
        data = PDFByte,
        file_name = "resume_anuj_RPA_AI.pdf",
        mime="application/octet-stream"
    )
    if st.button("✉ Contact Me"):
        contact_form()

# -----------Social Media -------
st.write("#")
cols = st.columns(len(social_media))

for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")

# ------All the user details --------
st.write("\n")
st.subheader("Profile Summary", anchor = False)
st.write(
    """
    Dynamic and experienced Senior Software Engineer with a robust background in RPA tools, Python, APIs, SQL,
    and database management. Proven track record in successfully leading automation projects and receiving accolades for
    exceptional performance. Proficient in RPA platforms such as Automation Anywhere, with extensive experience 
    managing diverse client applications across multiple domains, including healthcare and finance. 
    Skilled in leveraging Azure services for application development and deployment. 
    Committed to advancing expertise in Data Science to drive innovative technological solutions. 
    Adept at enhancing operational efficiency and driving business growth through the application of advanced technical skills.
    """
)


# ------All the user details --------
st.write("\n")
st.subheader("Skills", anchor = False)
st.html(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skills</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .skills-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                background-color: transparent;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .skills-table th, .skills-table td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            .skills-table th {
                background-color: #f2f2f2;
            }
            .skills-table tr:hover {
                background-color: #f1f1f1;
            }
        </style>
    </head>
    <body>
        <table class="skills-table">
            <tr>
                <td>RPA Tools</td>
                <td>Automation Anywhere, Power Automate Desktop</td>
            </tr>
            <tr>
                <td>Programming Languages</td>
                <td>Python, SQL, VBScript, API</td>
            </tr>
            <tr>
                <td>Cloud Services</td>
                <td>Azure AI</td>
            </tr>
            <tr>
                <td>Databases</td>
                <td>SQL Server, Postgres SQL</td>
            </tr>
            <tr>
                <td>Other Tools</td>
                <td>Power Automate, Power Apps, VBA Macros, Excel</td>
            </tr>
        </table>
    </body>
    </html>

    """
)

# ------------------Employment history---
st.write("\n")
st.subheader("Employment History", anchor = False)
st.html(
    """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .employment-history {
            background-color: transparent;
            padding: 20px;
            border-radius: 8px;
        }
        .employment-history h2 {
            color: white;
            border-bottom: 2px solid white;
            padding-bottom: 10px;
        }
        .job {
            margin-bottom: 20px;
            padding: 15px;
            border-left: 4px solid #0078d4;
            background-color: rgba(0, 120, 212, 0.1);
            border-radius: 4px;
        }
        .job h3, .job h4, .job p, .job ul li {
            color: white;
        }
        .job ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        .job ul li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="employment-history">
        
        <div class="job">
            <h3>💻 Senior Software Engineer at IQVIA</h3>
            <h4>📆 07/2021 - Present</h4>
            <p>As a Senior Software Engineer at IQVIA, I specialize in developing and implementing software solutions tailored to meet healthcare objectives. I collaborate with cross-functional teams to analyse requirements, design system architectures, and create scalable applications utilizing RPA tools, Python, SQL, APIs and Azure services, including Intelligent Document Processing and Translator. My key accomplishments include:</p>
            <ul>
                <li>Led a team of 5 developers in designing and implementing RPA solutions, resulting in a 40% reduction in processing time.</li>
                <li>Received the Star Performer Award for outstanding contributions to software development and project delivery.</li>
                <li>Cultivated specialized knowledge in healthcare processes leading to the successful design and deployment of RPA tools; achieved a significant decrease in processing time for patient data entry.</li>
            </ul>
        </div>
    </div>
</body>
<body>
    <div class="employment-history">
        
        <div class="job">
            <h3>💻 Senior RPA Support Developer at Tesco</h3>
            <h4>📆 06/2019 – 06/2021</h4>
            <p>During my tenure as a Senior RPA Support Developer at TESCO: -</p>
            <ul>
                <li>Led a small team of RPA support specialists.</li>
                <li>Provided maintenance and support for over 200+ bots across various business functions.</li>
                <li>Managed, monitored, and ensured the smooth operation and performance of all automated bots.</li>
                <li>Work on multiple enhancement for bots.</li>
            </ul>
        </div>
    </div>
</body>
<body>
    <div class="employment-history">
        
        <div class="job">
            <h3>💻 RPA Developer at Opteamix</h3>
            <h4>📆 10/2018 – 06/2019</h4>
            <p>Developed expertise in healthcare workflows, designing RPA solutions to improve efficiency and accuracy while ensuring regulatory compliance. Key contributions:</p>
            <ul>
                <li>Engineered RPA bots, reducing data entry time by 50% and enhancing accuracy</li>
                <li>Managed bot life cycle from feasibility to deployment.</li>
                <li>Executed comprehensive UAT with detailed test scripts.</li>
                <li>Supported team by troubleshooting and resolving issues throughout SDLC.</li>
            </ul>
        </div>
    </div>
</body>
<body>
    <div class="employment-history">
        
        <div class="job">
            <h3>💻 Associate Developer at Accenture</h3>
            <h4>📆 10/2015 – 06/2018</h4>
            <ul>
                <li>Developed automation solutions using VBA, Excel, Automation Anywhere, and VBScript for internal processes.</li>
                <li>Automated data processing tasks with VBA in Excel, reducing manual effort.</li>
                <li>Designed bots in Automation Anywhere to enhance workflow efficiency.</li>
                <li>Optimized internal workflows for Accenture teams, saving time and resources.</li>
                <li>Collaborated with stakeholders to ensure seamless integration of automation solutions.</li>
            </ul>
        </div>
    </div>
</body>
</html>
    """
)
