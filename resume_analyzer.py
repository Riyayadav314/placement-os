import customtkinter as ctk
from tkinter import messagebox


# =========================================================
# APPEARANCE
# =========================================================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# =========================================================
# COLOR SETTINGS
# =========================================================

BLUE = "#1F6AA5"
BLUE_HOVER = "#15527F"

GREEN = "#2E8B57"
GREEN_HOVER = "#246B45"

RED = "#C0392B"
RED_HOVER = "#962D22"

YELLOW = "#C99A2E"

DARK_CARD = "#1E1E1E"

TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#BDBDBD"

RESET_COLOR = "#444444"
RESET_HOVER = "#555555"


# =========================================================
# RESUME ANALYZER
# =========================================================

def resume_analyzer(profile=None):

    # =====================================================
    # CREATE WINDOW
    # =====================================================

    window = ctk.CTkToplevel()

    window.title("Resume Analyzer")

    # Full screen / maximized
    window.state("zoomed")

    window.resizable(True, True)


    # =====================================================
    # MAIN SCROLLABLE FRAME
    # =====================================================

    main = ctk.CTkScrollableFrame(
        window,
        fg_color="transparent"
    )

    main.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=30
    )


    # =====================================================
    # HEADER
    # =====================================================

    header = ctk.CTkFrame(
        main,
        corner_radius=15,
        fg_color=BLUE
    )

    header.pack(
        fill="x",
        pady=(0, 25)
    )

    ctk.CTkLabel(
        header,
        text="📄 RESUME ANALYZER",
        font=("Arial", 32, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 8)
    )

    ctk.CTkLabel(
        header,
        text="Analyze your resume profile and get personalized improvement suggestions",
        font=("Arial", 17),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 25)
    )


    # =====================================================
    # INFORMATION CARD
    # =====================================================

    info_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    info_frame.pack(
        fill="x",
        pady=10
    )

    ctk.CTkLabel(
        info_frame,
        text="👤 Resume Information",
        font=("Arial", 26, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    # =====================================================
    # FULL NAME
    # =====================================================

    ctk.CTkLabel(
        info_frame,
        text="Full Name",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 5)
    )

    name_entry = ctk.CTkEntry(
        info_frame,
        height=45,
        font=("Arial", 16),
        placeholder_text="Enter your full name"
    )

    name_entry.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )


    # =====================================================
    # EDUCATION
    # =====================================================

    ctk.CTkLabel(
        info_frame,
        text="Education / Degree",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 5)
    )

    education_entry = ctk.CTkEntry(
        info_frame,
        height=45,
        font=("Arial", 16),
        placeholder_text="Example: B.Tech in AIML"
    )

    education_entry.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )


    # =====================================================
    # TECHNICAL SKILLS
    # =====================================================

    ctk.CTkLabel(
        info_frame,
        text="Technical Skills",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 5)
    )

    skills_entry = ctk.CTkEntry(
        info_frame,
        height=45,
        font=("Arial", 16),
        placeholder_text=(
            "Example: Python, Java, SQL, HTML, CSS, Machine Learning"
        )
    )

    skills_entry.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )


    # =====================================================
    # PROJECTS
    # =====================================================

    ctk.CTkLabel(
        info_frame,
        text="Projects",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 5)
    )

    projects_entry = ctk.CTkEntry(
        info_frame,
        height=45,
        font=("Arial", 16),
        placeholder_text=(
            "Example: Student Performance Prediction, Portfolio Website"
        )
    )

    projects_entry.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )


    # =====================================================
    # INTERNSHIP / TRAINING
    # =====================================================

    ctk.CTkLabel(
        info_frame,
        text="Internship / Training",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 5)
    )

    internship_entry = ctk.CTkEntry(
        info_frame,
        height=45,
        font=("Arial", 16),
        placeholder_text="Example: Python Developer Internship"
    )

    internship_entry.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )


    # =====================================================
    # CERTIFICATIONS
    # =====================================================

    ctk.CTkLabel(
        info_frame,
        text="Certifications",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 5)
    )

    certifications_entry = ctk.CTkEntry(
        info_frame,
        height=45,
        font=("Arial", 16),
        placeholder_text="Example: Python Certificate, AI Certificate"
    )

    certifications_entry.pack(
        fill="x",
        padx=30,
        pady=(0, 15)
    )


    # =====================================================
    # GITHUB / LINKEDIN
    # =====================================================

    ctk.CTkLabel(
        info_frame,
        text="GitHub / LinkedIn",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 5)
    )

    links_entry = ctk.CTkEntry(
        info_frame,
        height=45,
        font=("Arial", 16),
        placeholder_text="Enter GitHub or LinkedIn profile"
    )

    links_entry.pack(
        fill="x",
        padx=30,
        pady=(0, 25)
    )


    # =====================================================
    # RESULT FRAME
    # =====================================================

    result_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )


    # =====================================================
    # RESULT TITLE
    # =====================================================

    ctk.CTkLabel(
        result_frame,
        text="📊 Resume Analysis Result",
        font=("Arial", 28, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    # =====================================================
    # SCORE LABEL
    # =====================================================

    score_label = ctk.CTkLabel(
        result_frame,
        text="",
        font=("Arial", 42, "bold"),
        text_color=GREEN
    )

    score_label.pack(
        pady=(5, 20)
    )


    # =====================================================
    # RESULT BOX
    # =====================================================

    result_box = ctk.CTkTextbox(
        result_frame,
        height=500,
        font=("Arial", 17)
    )

    result_box.pack(
        fill="x",
        padx=30,
        pady=(0, 25)
    )


    # =====================================================
    # ANALYZE RESUME FUNCTION
    # =====================================================

    def analyze_resume():

        # -------------------------------------------------
        # GET USER INPUT
        # -------------------------------------------------

        name = name_entry.get().strip()

        education = education_entry.get().strip()

        skills = skills_entry.get().strip()

        projects = projects_entry.get().strip()

        internship = internship_entry.get().strip()

        certifications = certifications_entry.get().strip()

        links = links_entry.get().strip()


        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------

        if not name:

            messagebox.showwarning(
                "Missing Information",
                "Please enter your name."
            )

            return


        if not education:

            messagebox.showwarning(
                "Missing Information",
                "Please enter your education."
            )

            return


        if not skills:

            messagebox.showwarning(
                "Missing Information",
                "Please enter your technical skills."
            )

            return


        # -------------------------------------------------
        # CONVERT SKILLS TO LOWERCASE
        # -------------------------------------------------

        skill_text = skills.lower()


        # -------------------------------------------------
        # IMPORTANT SKILLS
        # -------------------------------------------------

        recommended_skills = [

            "python",
            "java",
            "c++",
            "c",
            "sql",
            "html",
            "css",
            "javascript",
            "django",
            "flask",
            "machine learning",
            "artificial intelligence",
            "data analysis",
            "git",
            "github",
            "excel",
            "react",
            "node"

        ]


        # -------------------------------------------------
        # FIND MATCHED SKILLS
        # -------------------------------------------------

        matched_skills = []

        for skill in recommended_skills:

            if skill in skill_text:

                matched_skills.append(
                    skill
                )


        # -------------------------------------------------
        # SCORE VARIABLES
        # -------------------------------------------------

        score = 0

        strengths = []

        improvements = []


        # -------------------------------------------------
        # EDUCATION SCORE
        # -------------------------------------------------

        if education:

            score += 15

            strengths.append(
                "Education information is present."
            )


        # -------------------------------------------------
        # SKILLS SCORE
        # -------------------------------------------------

        if len(matched_skills) >= 6:

            score += 25

            strengths.append(
                "Good number of relevant technical skills."
            )

        elif len(matched_skills) >= 3:

            score += 18

            strengths.append(
                "You have some relevant technical skills."
            )

        else:

            score += 8

            improvements.append(
                "Add more relevant technical skills."
            )


        # -------------------------------------------------
        # PROJECTS SCORE
        # -------------------------------------------------

        if projects:

            score += 20

            strengths.append(
                "Projects are included."
            )

        else:

            improvements.append(
                "Add at least 2 strong academic or personal projects."
            )


        # -------------------------------------------------
        # INTERNSHIP SCORE
        # -------------------------------------------------

        if internship:

            score += 15

            strengths.append(
                "Internship/training experience is present."
            )

        else:

            improvements.append(
                "Add internship, training or practical experience if available."
            )


        # -------------------------------------------------
        # CERTIFICATION SCORE
        # -------------------------------------------------

        if certifications:

            score += 10

            strengths.append(
                "Certifications are included."
            )

        else:

            improvements.append(
                "Add relevant certifications to strengthen your profile."
            )


        # -------------------------------------------------
        # LINK SCORE
        # -------------------------------------------------

        if links:

            score += 10

            strengths.append(
                "Professional profile link is available."
            )

        else:

            improvements.append(
                "Add GitHub and/or LinkedIn profile."
            )


        # -------------------------------------------------
        # NAME SCORE
        # -------------------------------------------------

        if name:

            score += 5


        # -------------------------------------------------
        # MAX SCORE
        # -------------------------------------------------

        score = min(
            score,
            100
        )


        # -------------------------------------------------
        # EXTRA SKILL SUGGESTIONS
        # -------------------------------------------------

        if "sql" not in skill_text:

            improvements.append(
                "Consider adding SQL/database knowledge."
            )


        if (
            "git" not in skill_text
            and "github" not in skill_text
        ):

            improvements.append(
                "Add Git/GitHub to demonstrate version-control knowledge."
            )


        if (
            "machine learning" not in skill_text
            and "artificial intelligence" not in skill_text
        ):

            improvements.append(
                "For AI/ML roles, mention relevant Machine Learning or AI skills."
            )


        # -------------------------------------------------
        # RESUME STATUS
        # -------------------------------------------------

        if score >= 85:

            status = "Excellent Resume Profile"

            status_text = (
                "Your resume profile is strong and suitable "
                "for many entry-level opportunities."
            )

            score_color = GREEN


        elif score >= 70:

            status = "Good Resume Profile"

            status_text = (
                "Your resume has a good foundation, but a few "
                "improvements can make it stronger."
            )

            score_color = GREEN


        elif score >= 50:

            status = "Average Resume Profile"

            status_text = (
                "Your resume needs some important improvements "
                "before applying to competitive roles."
            )

            score_color = YELLOW


        else:

            status = "Needs Improvement"

            status_text = (
                "Your resume profile needs more development "
                "and practical information."
            )

            score_color = RED


        # =================================================
        # DISPLAY SCORE
        # =================================================

        score_label.configure(
            text=f"{score}/100\n{status}",
            text_color=score_color
        )


        # =================================================
        # CLEAR OLD RESULT
        # =================================================

        result_box.configure(
            state="normal"
        )

        result_box.delete(
            "1.0",
            "end"
        )


        # =================================================
        # CANDIDATE
        # =================================================

        result_box.insert(
            "end",
            f"👤 Candidate: {name}\n\n"
        )


        # =================================================
        # OVERALL ASSESSMENT
        # =================================================

        result_box.insert(
            "end",
            "📌 OVERALL ASSESSMENT\n\n"
        )

        result_box.insert(
            "end",
            f"{status_text}\n\n"
        )


        # =================================================
        # TECHNICAL SKILLS
        # =================================================

        result_box.insert(
            "end",
            "🛠️ TECHNICAL SKILLS DETECTED\n\n"
        )

        if matched_skills:

            result_box.insert(
                "end",
                ", ".join(
                    matched_skills
                )
                + "\n\n"
            )

        else:

            result_box.insert(
                "end",
                "No major technical skills detected "
                "from the entered skills.\n\n"
            )


        # =================================================
        # STRENGTHS
        # =================================================

        result_box.insert(
            "end",
            "✅ STRENGTHS\n\n"
        )

        if strengths:

            for item in strengths:

                result_box.insert(
                    "end",
                    f"• {item}\n"
                )

        else:

            result_box.insert(
                "end",
                "No major strengths detected yet.\n"
            )


        result_box.insert(
            "end",
            "\n"
        )


        # =================================================
        # IMPROVEMENTS
        # =================================================

        result_box.insert(
            "end",
            "⚠️ AREAS TO IMPROVE\n\n"
        )

        if improvements:

            for item in improvements:

                result_box.insert(
                    "end",
                    f"• {item}\n"
                )

        else:

            result_box.insert(
                "end",
                "No major improvement required.\n"
            )


        result_box.insert(
            "end",
            "\n"
        )


        # =================================================
        # RESUME TIPS
        # =================================================

        result_box.insert(
            "end",
            "💡 RESUME TIPS\n\n"
        )

        result_box.insert(
            "end",
            "• Keep your resume concise and professional.\n"
            "• Highlight projects with technologies and your contribution.\n"
            "• Mention measurable results wherever possible.\n"
            "• Keep technical skills relevant to the target job.\n"
            "• Add GitHub/LinkedIn links.\n"
            "• Check grammar and spelling before applying.\n"
            "• Customize your resume according to the job description.\n"
        )


        # =================================================
        # LOCK RESULT BOX
        # =================================================

        result_box.configure(
            state="disabled"
        )


        # =================================================
        # SHOW RESULT FRAME
        # =================================================

        result_frame.pack(
            fill="x",
            pady=25
        )

        main.update_idletasks()


    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    ctk.CTkButton(
        main,
        text="🔍 Analyze My Resume",
        width=300,
        height=55,
        font=("Arial", 19, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=analyze_resume
    ).pack(
        pady=(25, 15)
    )


    # =====================================================
    # RESET FUNCTION
    # =====================================================

    def reset_form():

        name_entry.delete(
            0,
            "end"
        )

        education_entry.delete(
            0,
            "end"
        )

        skills_entry.delete(
            0,
            "end"
        )

        projects_entry.delete(
            0,
            "end"
        )

        internship_entry.delete(
            0,
            "end"
        )

        certifications_entry.delete(
            0,
            "end"
        )

        links_entry.delete(
            0,
            "end"
        )

        result_frame.pack_forget()


    # =====================================================
    # RESET BUTTON
    # =====================================================

    ctk.CTkButton(
        main,
        text="🔄 Reset",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=RESET_COLOR,
        hover_color=RESET_HOVER,
        command=reset_form
    ).pack(
        pady=10
    )


    # =====================================================
    # CLOSE BUTTON
    # =====================================================

    ctk.CTkButton(
        main,
        text="❌ Close",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color=RED_HOVER,
        command=window.destroy
    ).pack(
        pady=(10, 35)
    )