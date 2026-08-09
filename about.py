import customtkinter as ctk


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

DARK_CARD = "#1E1E1E"

TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#BDBDBD"

LIGHT_BLUE = "#2B78B5"


# =========================================================
# ABOUT PROJECT
# =========================================================

def about():

    # =====================================================
    # CREATE WINDOW
    # =====================================================

    window = ctk.CTkToplevel()

    window.title(
        "About Placement OS"
    )

    # Full screen
    window.state(
        "zoomed"
    )

    window.resizable(
        True,
        True
    )


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
        corner_radius=18,
        fg_color=BLUE
    )

    header.pack(
        fill="x",
        pady=(0, 25)
    )


    ctk.CTkLabel(
        header,
        text="🎓 PLACEMENT OS",
        font=("Arial", 36, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(30, 8)
    )


    ctk.CTkLabel(
        header,
        text="Student Placement & Career Assistance System",
        font=("Arial", 19, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 8)
    )


    ctk.CTkLabel(
        header,
        text="A complete desktop platform designed to help students prepare for placements.",
        font=("Arial", 16),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 30)
    )


    # =====================================================
    # PROJECT INTRODUCTION
    # =====================================================

    intro_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    intro_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        intro_card,
        text="📖 About the Project",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 15)
    )


    ctk.CTkLabel(
        intro_card,
        text=(
            "Placement OS is a student-focused placement assistance "
            "application designed to bring important career preparation "
            "activities into one platform.\n\n"
            "The system provides students with tools for profile management, "
            "resume preparation, placement prediction, job recommendations, "
            "quiz practice, mock interviews, certificates, eligibility "
            "checking and other placement-related activities."
        ),
        font=("Arial", 17),
        text_color=TEXT_GRAY,
        justify="left",
        wraplength=1150
    ).pack(
        anchor="w",
        padx=30,
        pady=(0, 30)
    )


    # =====================================================
    # OBJECTIVE
    # =====================================================

    objective_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    objective_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        objective_card,
        text="🎯 Project Objective",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 15)
    )


    objective_text = (
        "The main objective of Placement OS is to provide students "
        "with a centralized platform where they can evaluate their "
        "skills, prepare for interviews, improve their resumes and "
        "understand their placement readiness."
    )


    ctk.CTkLabel(
        objective_card,
        text=objective_text,
        font=("Arial", 17),
        text_color=TEXT_GRAY,
        justify="left",
        wraplength=1150
    ).pack(
        anchor="w",
        padx=30,
        pady=(0, 30)
    )


    # =====================================================
    # KEY FEATURES
    # =====================================================

    feature_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    feature_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        feature_card,
        text="🚀 Key Features",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    features = [

        (
            "📄 Resume Analyzer",
            "Analyze resume information and receive a resume score, "
            "strengths and improvement suggestions."
        ),

        (
            "📝 Resume Builder",
            "Create a professional resume using the student's "
            "profile and project information."
        ),

        (
            "🎯 Placement Prediction",
            "Estimate placement chances based on academic performance "
            "and provide preparation suggestions."
        ),

        (
            "💼 Job Recommendation",
            "Recommend suitable career roles based on selected "
            "technical skills."
        ),

        (
            "🧠 Quiz",
            "Practice placement-oriented questions and improve "
            "technical and aptitude preparation."
        ),

        (
            "🎤 Mock Interview",
            "Practice HR, technical and project interview questions "
            "with answer evaluation and improvement guidance."
        ),

        (
            "🏢 Company Eligibility",
            "Check eligibility for companies based on student profile "
            "and academic information."
        ),

        (
            "🏆 Leaderboard",
            "View student rankings based on academic performance."
        ),

        (
            "📜 Certificate",
            "Generate a placement-related certificate in PDF format."
        )

    ]


    for title, description in features:

        card = ctk.CTkFrame(
            feature_card,
            corner_radius=12,
            fg_color=DARK_CARD,
            border_width=1,
            border_color=BLUE
        )

        card.pack(
            fill="x",
            padx=30,
            pady=7
        )


        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 19, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )


        ctk.CTkLabel(
            card,
            text=description,
            font=("Arial", 15),
            text_color=TEXT_GRAY,
            justify="left",
            wraplength=1080
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )


    # =====================================================
    # MODULES
    # =====================================================

    modules_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    modules_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        modules_card,
        text="🧩 Main Modules",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    modules = [

        "My Profile",
        "Resume Analyzer",
        "Resume Builder",
        "Company Eligibility",
        "Placement Prediction",
        "Job Recommendation",
        "Quiz",
        "Mock Interview",
        "Certificate",
        "Edit Profile",
        "Change Password",
        "Admin Panel",
        "Leaderboard"

    ]


    # Create two-column module layout

    module_grid = ctk.CTkFrame(
        modules_card,
        fg_color="transparent"
    )

    module_grid.pack(
        fill="x",
        padx=30,
        pady=(0, 30)
    )


    row = 0
    column = 0


    for module in modules:

        module_box = ctk.CTkFrame(
            module_grid,
            corner_radius=10,
            fg_color=DARK_CARD
        )

        module_box.grid(
            row=row,
            column=column,
            padx=8,
            pady=8,
            sticky="ew"
        )


        ctk.CTkLabel(
            module_box,
            text=f"✓  {module}",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=15
        )


        column += 1


        if column == 2:

            column = 0

            row += 1


    module_grid.grid_columnconfigure(
        0,
        weight=1
    )

    module_grid.grid_columnconfigure(
        1,
        weight=1
    )


    # =====================================================
    # TECHNOLOGIES
    # =====================================================

    technology_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    technology_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        technology_card,
        text="💻 Technologies Used",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    technologies = [

        "🐍 Python",
        "🖥️ CustomTkinter",
        "🗄️ SQLite",
        "📄 ReportLab",
        "🎨 Tkinter",
        "📁 File Handling",
        "🔐 Password Management",
        "📊 Data Processing"

    ]


    technology_grid = ctk.CTkFrame(
        technology_card,
        fg_color="transparent"
    )

    technology_grid.pack(
        fill="x",
        padx=30,
        pady=(0, 30)
    )


    row = 0
    column = 0


    for technology in technologies:

        tech_box = ctk.CTkFrame(
            technology_grid,
            corner_radius=10,
            fg_color=DARK_CARD,
            border_width=1,
            border_color=BLUE
        )

        tech_box.grid(
            row=row,
            column=column,
            padx=8,
            pady=8,
            sticky="ew"
        )


        ctk.CTkLabel(
            tech_box,
            text=technology,
            font=("Arial", 16, "bold")
        ).pack(
            padx=20,
            pady=15
        )


        column += 1


        if column == 2:

            column = 0

            row += 1


    technology_grid.grid_columnconfigure(
        0,
        weight=1
    )

    technology_grid.grid_columnconfigure(
        1,
        weight=1
    )


    # =====================================================
    # HOW IT WORKS
    # =====================================================

    workflow_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    workflow_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        workflow_card,
        text="🔄 How Placement OS Works",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    workflow_steps = [

        (
            "01",
            "Create Profile",
            "Enter your academic and personal information."
        ),

        (
            "02",
            "Build Your Resume",
            "Add skills, projects, education and experience."
        ),

        (
            "03",
            "Analyze & Prepare",
            "Check placement readiness and improve your resume."
        ),

        (
            "04",
            "Practice",
            "Take quizzes and practice mock interviews."
        ),

        (
            "05",
            "Explore Opportunities",
            "Check company eligibility and suitable job roles."
        ),

        (
            "06",
            "Track Performance",
            "Use leaderboard and other tools to monitor progress."
        )

    ]


    for number, title, description in workflow_steps:

        step_card = ctk.CTkFrame(
            workflow_card,
            corner_radius=12,
            fg_color=DARK_CARD
        )

        step_card.pack(
            fill="x",
            padx=30,
            pady=6
        )


        number_label = ctk.CTkLabel(
            step_card,
            text=number,
            width=70,
            height=55,
            corner_radius=10,
            fg_color=BLUE,
            font=("Arial", 20, "bold"),
            text_color=TEXT_WHITE
        )

        number_label.pack(
            side="left",
            padx=15,
            pady=12
        )


        text_frame = ctk.CTkFrame(
            step_card,
            fg_color="transparent"
        )

        text_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10,
            pady=10
        )


        ctk.CTkLabel(
            text_frame,
            text=title,
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w"
        )


        ctk.CTkLabel(
            text_frame,
            text=description,
            font=("Arial", 15),
            text_color=TEXT_GRAY
        ).pack(
            anchor="w",
            pady=(3, 0)
        )


    # =====================================================
    # PROJECT HIGHLIGHTS
    # =====================================================

    highlights_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    highlights_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        highlights_card,
        text="⭐ Project Highlights",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    highlights = [

        "Centralized placement preparation platform",

        "Student profile-based features",

        "Interactive graphical user interface",

        "Resume analysis and resume building",

        "Placement prediction and job recommendations",

        "Quiz and mock interview practice",

        "Company eligibility checking",

        "Leaderboard and performance tracking",

        "PDF certificate generation",

        "Local database-based student management"

    ]


    for highlight in highlights:

        ctk.CTkLabel(
            highlights_card,
            text=f"✓  {highlight}",
            font=("Arial", 16),
            text_color=TEXT_GRAY
        ).pack(
            anchor="w",
            padx=45,
            pady=5
        )


    # =====================================================
    # WHY PLACEMENT OS
    # =====================================================

    why_card = ctk.CTkFrame(
        main,
        corner_radius=15,
        fg_color=BLUE
    )

    why_card.pack(
        fill="x",
        pady=15
    )


    ctk.CTkLabel(
        why_card,
        text="💙 Why Placement OS?",
        font=("Arial", 27, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 15)
    )


    ctk.CTkLabel(
        why_card,
        text=(
            "Placement preparation becomes easier when important "
            "activities are available in one place.\n\n"
            "Placement OS combines profile management, resume tools, "
            "practice modules and placement assistance features into "
            "a single student-friendly application."
        ),
        font=("Arial", 17),
        text_color=TEXT_WHITE,
        justify="center",
        wraplength=1100
    ).pack(
        padx=40,
        pady=(0, 30)
    )


    # =====================================================
    # PROJECT INFORMATION
    # =====================================================

    info_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    info_card.pack(
        fill="x",
        pady=10
    )


    ctk.CTkLabel(
        info_card,
        text="📌 Project Information",
        font=("Arial", 27, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 15)
    )


    ctk.CTkLabel(
        info_card,
        text=(
            "Project Name : Placement OS\n"
            "Application Type : Desktop Application\n"
            "Purpose : Student Placement & Career Assistance\n"
            "Interface : Graphical User Interface\n"
            "Version : 1.0"
        ),
        font=("Arial", 17),
        text_color=TEXT_GRAY,
        justify="left"
    ).pack(
        anchor="w",
        padx=30,
        pady=(0, 30)
    )


    # =====================================================
    # FOOTER
    # =====================================================

    footer = ctk.CTkFrame(
        main,
        corner_radius=15,
        fg_color=DARK_CARD
    )

    footer.pack(
        fill="x",
        pady=(15, 20)
    )


    ctk.CTkLabel(
        footer,
        text="🎓 Placement OS",
        font=("Arial", 21, "bold")
    ).pack(
        pady=(20, 5)
    )


    ctk.CTkLabel(
        footer,
        text="Student Placement & Career Assistance System",
        font=("Arial", 15),
        text_color=TEXT_GRAY
    ).pack(
        pady=(0, 5)
    )


    ctk.CTkLabel(
        footer,
        text="Version 1.0",
        font=("Arial", 14),
        text_color=TEXT_GRAY
    ).pack(
        pady=(0, 20)
    )


    # =====================================================
    # CLOSE BUTTON
    # =====================================================

    ctk.CTkButton(
        main,
        text="❌ Close",
        width=240,
        height=52,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color=RED_HOVER,
        command=window.destroy
    ).pack(
        pady=(5, 35)
    )