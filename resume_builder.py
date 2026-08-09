import customtkinter as ctk
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from tkinter import messagebox
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import navy


from resume_db import (

    # Resume
    save_resume,
    load_resume,

    # Skills
    save_skill,
    load_skills,
    delete_all_skills,

    # Projects
    save_project,
    load_projects,
    delete_all_projects,

    # Internship
    save_internship,
    load_internships,
    delete_all_internships,

    # Certificates
    save_certificate,
    load_certificates,
    delete_all_certificates

)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def resume_builder(profile):

    window = ctk.CTkToplevel()

    window.title("Resume Builder")

    window.geometry("1000x700")

    # Main Scroll Frame
    main = ctk.CTkScrollableFrame(window)
    main.pack(fill="both", expand=True, padx=20, pady=20)

    # Heading
    ctk.CTkLabel(
        main,
        text="📄 Professional Resume Builder",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    # ================= BASIC INFORMATION =================

    ctk.CTkLabel(
        main,
        text="Basic Information",
        font=("Arial",22,"bold")
    ).pack(anchor="w", pady=(10,5))

    fullname = ctk.CTkEntry(main, width=700)
    fullname.insert(0, profile[2])
    fullname.pack(pady=5)

    email = ctk.CTkEntry(main, width=700)
    email.insert(0, profile[6])
    email.pack(pady=5)

    mobile = ctk.CTkEntry(main, width=700)
    mobile.insert(0, profile[7])
    mobile.pack(pady=5)

    college = ctk.CTkEntry(main, width=700)
    college.insert(0, profile[3])
    college.pack(pady=5)

    branch = ctk.CTkEntry(main, width=700)
    branch.insert(0, profile[4])
    branch.pack(pady=5)

    cgpa = ctk.CTkEntry(main, width=700)
    cgpa.insert(0, str(profile[5]))
    cgpa.pack(pady=5)

    city = ctk.CTkEntry(main, width=700)
    city.insert(0, profile[8])
    city.pack(pady=5)

    address = ctk.CTkTextbox(main, width=700, height=80)
    address.insert("1.0", profile[9])
    address.pack(pady=5)

    # ================= CAREER OBJECTIVE =================

    ctk.CTkLabel(
        main,
        text="Career Objective",
        font=("Arial",22,"bold")
    ).pack(anchor="w", pady=(20,5))

    objective = ctk.CTkTextbox(
        main,
        width=700,
        height=120
    )

    objective.pack(pady=5)
        # ================= SKILLS =================

    ctk.CTkLabel(
        main,
        text="💻 Skills",
        font=("Arial",22,"bold")
    ).pack(anchor="w", pady=(20,5))

    skills = ctk.CTkTextbox(
        main,
        width=700,
        height=120
    )

    skills.pack(pady=5)

    # ================= PROJECTS =================

    ctk.CTkLabel(
        main,
        text="🚀 Projects",
        font=("Arial",22,"bold")
    ).pack(anchor="w", pady=(20,5))

    projects = ctk.CTkTextbox(
        main,
        width=700,
        height=150
    )

    projects.pack(pady=5)

    # ================= INTERNSHIP =================

    ctk.CTkLabel(
        main,
        text="💼 Internship",
        font=("Arial",22,"bold")
    ).pack(anchor="w", pady=(20,5))

    internship = ctk.CTkTextbox(
        main,
        width=700,
        height=120
    )

    internship.pack(pady=5)

    # ================= CERTIFICATES =================

    ctk.CTkLabel(
        main,
        text="🏆 Certificates",
        font=("Arial",22,"bold")
    ).pack(anchor="w", pady=(20,5))

    certificates = ctk.CTkTextbox(
        main,
        width=700,
        height=120
    )

    certificates.pack(pady=5)

    # ================= LINKS =================

    ctk.CTkLabel(
        main,
        text="🌐 Links",
        font=("Arial",22,"bold")
    ).pack(anchor="w", pady=(20,5))

    linkedin = ctk.CTkEntry(
        main,
        width=700,
        placeholder_text="LinkedIn Profile"
    )

    linkedin.pack(pady=5)

    github = ctk.CTkEntry(
        main,
        width=700,
        placeholder_text="GitHub Profile"
    )

    github.pack(pady=5)
        # ================= AUTO LOAD =================

    data = load_resume(profile[0])

    if data:

        objective.delete("1.0", "end")
        objective.insert("1.0", data[1])

        linkedin.delete(0, "end")
        linkedin.insert(0, data[2])

        github.delete(0, "end")
        github.insert(0, data[3])
        
            # ================= AUTO LOAD SKILLS =================

    skills.delete("1.0", "end")

    all_skills = load_skills(
        profile[0]
    )

    for skill in all_skills:

        skills.insert(
            "end",
            skill[0] + "\n"
        )
            
         # ================= AUTO LOAD PROJECTS =================

    projects.delete("1.0", "end")

    all_projects = load_projects(profile[0])

    for project in all_projects:

        projects.insert(
            "end",
            project[1] + "\n"
        
        )
            # ================= AUTO LOAD INTERNSHIP =================

    internship.delete("1.0", "end")

    all_internships = load_internships(profile[0])

    for item in all_internships:

        internship.insert(
            "end",
            item[3] + "\n"
        )
            # ================= AUTO LOAD CERTIFICATES =================

    certificates.delete("1.0", "end")

    all_certificates = load_certificates(profile[0])

    for certificate in all_certificates:

        certificates.insert(
            "end",
            certificate[0] + "\n"
        )
            # ================= SAVE FUNCTION =================

    def save_data():

        # ================= SAVE RESUME =================

        save_resume(
            profile[0],
            objective.get("1.0", "end").strip(),
            linkedin.get().strip(),
            github.get().strip()
        )

        # ================= SAVE SKILLS =================

        delete_all_skills(profile[0])

        skills_text = skills.get("1.0", "end").strip()

        if skills_text:

            for skill in skills_text.split("\n"):

                if skill.strip():

                    save_skill(
                        profile[0],
                        skill.strip()
                    )

        # ================= SAVE PROJECTS =================

        delete_all_projects(profile[0])

        project_text = projects.get("1.0", "end").strip()

        if project_text:

            save_project(
                profile[0],
                "Project",
                project_text,
                "",
                ""
            )

        # ================= SAVE INTERNSHIP =================

        delete_all_internships(profile[0])

        internship_text = internship.get("1.0", "end").strip()

        if internship_text:

            save_internship(
                profile[0],
                "Internship",
                "Trainee",
                "",
                internship_text
            )

        # ================= SAVE CERTIFICATES =================

        delete_all_certificates(profile[0])

        certificate_text = certificates.get("1.0", "end").strip()

        if certificate_text:

            save_certificate(
                profile[0],
                certificate_text,
                "",
                ""
            )

        # ================= SUCCESS MESSAGE =================

        messagebox.showinfo(
            "Success",
            "Resume Saved Successfully."
        )
        
   
            # ================= RESET FUNCTION =================

    def reset_data():

        objective.delete("1.0", "end")

        skills.delete("1.0", "end")

        projects.delete("1.0", "end")

        internship.delete("1.0", "end")

        certificates.delete("1.0", "end")

        linkedin.delete(0, "end")

        github.delete(0, "end")

        messagebox.showinfo(
            "Success",
            "Form Reset Successfully."
        )
            # ================= PDF FUNCTION =================

    def generate_pdf():

        doc = SimpleDocTemplate("resume.pdf")

        styles = getSampleStyleSheet()
                # ================= PDF STYLES =================

        title_style = ParagraphStyle(
            "Title",
            parent=styles["Heading1"],
            alignment=TA_CENTER,
            textColor=navy,
            fontSize=22,
            spaceAfter=20
        )

        heading_style = ParagraphStyle(
            "Heading",
            parent=styles["Heading2"],
            textColor=navy,
            spaceBefore=12,
            spaceAfter=8
        )

        story = []

        
                # ================= PDF TITLE =================

        story.append(
            Paragraph(
                "PROFESSIONAL RESUME",
                title_style
            )
        )

        story.append(Paragraph("<br/>", styles["Normal"]))

        story.append(Paragraph("<b>Name:</b> " + fullname.get(), styles["Normal"]))

        story.append(Paragraph("<b>Email:</b> " + email.get(), styles["Normal"]))

        story.append(Paragraph("<b>Mobile:</b> " + mobile.get(), styles["Normal"]))

        story.append(Paragraph("<b>College:</b> " + college.get(), styles["Normal"]))

        story.append(Paragraph("<b>Branch:</b> " + branch.get(), styles["Normal"]))

        story.append(Paragraph("<b>CGPA:</b> " + cgpa.get(), styles["Normal"]))

        story.append(Paragraph("<b>City:</b> " + city.get(), styles["Normal"]))

        story.append(Paragraph("<b>Address:</b> " + address.get("1.0","end").strip(), styles["Normal"]))

        story.append(Paragraph("<br/>", styles["Normal"]))

        
                # ================= CAREER OBJECTIVE =================

        story.append(
            Paragraph(
                "Career Objective",
                heading_style
            )
        )

        story.append(Paragraph(objective.get("1.0","end").strip(), styles["Normal"]))

        
                # ================= SKILLS =================

        story.append(
            Paragraph(
                "Skills",
                heading_style
            )
        )

        story.append(Paragraph(skills.get("1.0","end").strip(), styles["Normal"]))

        
                # ================= PROJECTS =================

        story.append(
            Paragraph(
                "Projects",
                heading_style
            )
        )

        story.append(Paragraph(projects.get("1.0","end").strip(), styles["Normal"]))

                # ================= INTERNSHIP =================

        story.append(
            Paragraph(
                "Internship",
                heading_style
            )
        )

        story.append(Paragraph(internship.get("1.0","end").strip(), styles["Normal"]))

    
                # ================= CERTIFICATES =================

        story.append(
            Paragraph(
                "Certificates",
                heading_style
            )
        )      

        story.append(Paragraph(certificates.get("1.0","end").strip(), styles["Normal"]))

        story.append(Paragraph("<b>LinkedIn</b> : " + linkedin.get(), styles["Normal"]))

        story.append(Paragraph("<b>GitHub</b> : " + github.get(), styles["Normal"]))

        doc.build(story)

        messagebox.showinfo(
            "Success",
            "PDF Generated Successfully."
        )
            # ================= PREVIEW FUNCTION =================

    def preview_resume():

        preview = ctk.CTkToplevel(window)

        preview.title("Resume Preview")

        preview.geometry("700x700")

        box = ctk.CTkTextbox(
            preview,
            width=650,
            height=650
        )

        box.pack(padx=20, pady=20)

        text = f"""
==========================
        RESUME
==========================

Name : {fullname.get()}

Email : {email.get()}

Mobile : {mobile.get()}

College : {college.get()}

Branch : {branch.get()}

CGPA : {cgpa.get()}

City : {city.get()}

Address :
{address.get("1.0","end").strip()}

--------------------------

CAREER OBJECTIVE

{objective.get("1.0","end").strip()}

--------------------------

SKILLS

{skills.get("1.0","end").strip()}

--------------------------

PROJECTS

{projects.get("1.0","end").strip()}

--------------------------

INTERNSHIP

{internship.get("1.0","end").strip()}

--------------------------

CERTIFICATES

{certificates.get("1.0","end").strip()}

--------------------------

LinkedIn :
{linkedin.get()}

GitHub :
{github.get()}
"""

        box.insert("1.0", text)

        box.configure(state="disabled")
        
        
        # ================= BUTTONS =================

    button_frame = ctk.CTkFrame(main)

    button_frame.pack(
        pady=25
    )

    save_btn = ctk.CTkButton(
        button_frame,
        text="💾 Save Resume",
        width=180,
        command=save_data
    )

    save_btn.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    preview_btn = ctk.CTkButton(
        button_frame,
        text="👀 Preview",
        width=180,
        command=preview_resume
    )

    preview_btn.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    pdf_btn = ctk.CTkButton(
        button_frame,
        text="📄 Generate PDF",
        width=180,
        command=generate_pdf
    )

    pdf_btn.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    reset_btn = ctk.CTkButton(
        button_frame,
        text="🔄 Reset",
        width=180,
        fg_color="red",
        command=reset_data
    )

    reset_btn.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )