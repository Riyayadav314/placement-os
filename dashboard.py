import customtkinter as ctk
from tkinter import messagebox

from my_profile import open_profile
from resume_builder import resume_builder
from placement import placement_prediction
from jobs import job_recommendation
from quiz import start_quiz
from certificate import generate_certificate
from edit_profile import edit_profile
from change_password import change_password
from admin import admin_panel
from leaderboard import leaderboard
from about import about
from company_eligibility import company_eligibility
from mock_interview import mock_interview
from resume_analyzer import resume_analyzer


# =========================================================
# APPEARANCE
# =========================================================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# =========================================================
# COLORS
# =========================================================

BG_COLOR = "#101820"

CARD_COLOR = "#18232D"
CARD_HOVER = "#243542"

BLUE = "#1F6AA5"
BLUE_HOVER = "#15527F"

GREEN = "#2E8B57"
GREEN_HOVER = "#246B45"

RED = "#C0392B"
RED_HOVER = "#962D22"

WHITE = "#FFFFFF"
GRAY = "#AEB8C2"


# =========================================================
# COMING SOON
# =========================================================

def coming_soon(name):

    messagebox.showinfo(
        "Coming Soon",
        f"{name} will be connected next."
    )


# =========================================================
# OPEN DASHBOARD
# =========================================================

def open_dashboard(profile):

    dashboard = ctk.CTk()

    dashboard.title(
        "Placement OS | Student Dashboard"
    )

    dashboard.configure(
        fg_color=BG_COLOR
    )

    # =====================================================
    # SCREEN SIZE
    # =====================================================

    screen_width = dashboard.winfo_screenwidth()
    screen_height = dashboard.winfo_screenheight()

    # Safe window size
    window_width = min(
        1250,
        screen_width - 80
    )

    window_height = min(
        850,
        screen_height - 100
    )

    # Center window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    dashboard.geometry(
        f"{window_width}x{window_height}+{x}+{y}"
    )

    dashboard.minsize(
        950,
        650
    )


    # =====================================================
    # MAIN SCROLL FRAME
    # =====================================================

    main = ctk.CTkScrollableFrame(
        dashboard,
        fg_color=BG_COLOR,
        scrollbar_button_color=BLUE,
        scrollbar_button_hover_color=BLUE_HOVER
    )

    main.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )


    # =====================================================
    # MAIN CONTENT WIDTH
    # =====================================================

    content = ctk.CTkFrame(
        main,
        fg_color="transparent"
    )

    content.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=5
    )


    # =====================================================
    # HEADER
    # =====================================================

    header = ctk.CTkFrame(
        content,
        fg_color=BLUE,
        corner_radius=18
    )

    header.pack(
        fill="x",
        pady=(0, 18)
    )


    header_content = ctk.CTkFrame(
        header,
        fg_color="transparent"
    )

    header_content.pack(
        fill="x",
        padx=25,
        pady=20
    )


    ctk.CTkLabel(
        header_content,
        text="💼  PLACEMENT OS",
        font=("Arial", 30, "bold"),
        text_color=WHITE
    ).pack(
        anchor="w"
    )


    ctk.CTkLabel(
        header_content,
        text="Student Placement & Career Assistance System",
        font=("Arial", 15),
        text_color=WHITE
    ).pack(
        anchor="w",
        pady=(4, 0)
    )


    # =====================================================
    # WELCOME CARD
    # =====================================================

    welcome_card = ctk.CTkFrame(
        content,
        fg_color=CARD_COLOR,
        corner_radius=18
    )

    welcome_card.pack(
        fill="x",
        pady=(0, 18)
    )


    welcome_content = ctk.CTkFrame(
        welcome_card,
        fg_color="transparent"
    )

    welcome_content.pack(
        fill="x",
        padx=25,
        pady=20
    )


    student_name = profile[2]


    ctk.CTkLabel(
        welcome_content,
        text=f"👋  Welcome, {student_name}",
        font=("Arial", 25, "bold"),
        text_color=WHITE
    ).pack(
        anchor="w"
    )


    ctk.CTkLabel(
        welcome_content,
        text=(
            "Your complete placement preparation platform. "
            "Build your resume, practice interviews and prepare for your career."
        ),
        font=("Arial", 14),
        text_color=GRAY,
        wraplength=1000,
        justify="left"
    ).pack(
        anchor="w",
        pady=(5, 0)
    )


    # =====================================================
    # QUICK INFORMATION
    # =====================================================

    info_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    info_frame.pack(
        fill="x",
        pady=(0, 20)
    )


    info_frame.grid_columnconfigure(
        0,
        weight=1
    )

    info_frame.grid_columnconfigure(
        1,
        weight=1
    )

    info_frame.grid_columnconfigure(
        2,
        weight=1
    )


    def create_info_card(
        column,
        icon,
        value,
        title
    ):

        card = ctk.CTkFrame(
            info_frame,
            fg_color=CARD_COLOR,
            corner_radius=16
        )

        card.grid(
            row=0,
            column=column,
            padx=6,
            sticky="ew"
        )


        ctk.CTkLabel(
            card,
            text=icon,
            font=("Arial", 27)
        ).pack(
            pady=(14, 3)
        )


        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 18, "bold"),
            text_color=WHITE
        ).pack(
            padx=10
        )


        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 12),
            text_color=GRAY
        ).pack(
            pady=(3, 14)
        )


    create_info_card(
        0,
        "🎓",
        str(profile[5]),
        "Current CGPA"
    )


    create_info_card(
        1,
        "💻",
        str(profile[4]),
        "Branch"
    )


    create_info_card(
        2,
        "🏫",
        str(profile[3]),
        "College"
    )


    # =====================================================
    # SECTION FUNCTION
    # =====================================================

    def create_section(
        title,
        subtitle,
        modules
    ):

        section = ctk.CTkFrame(
            content,
            fg_color=CARD_COLOR,
            corner_radius=18
        )

        section.pack(
            fill="x",
            pady=9
        )


        # -------------------------------------------------
        # SECTION HEADER
        # -------------------------------------------------

        section_header = ctk.CTkFrame(
            section,
            fg_color="transparent"
        )

        section_header.pack(
            fill="x",
            padx=22,
            pady=(18, 8)
        )


        ctk.CTkLabel(
            section_header,
            text=title,
            font=("Arial", 21, "bold"),
            text_color=WHITE
        ).pack(
            anchor="w"
        )


        ctk.CTkLabel(
            section_header,
            text=subtitle,
            font=("Arial", 12),
            text_color=GRAY
        ).pack(
            anchor="w",
            pady=(3, 0)
        )


        # -------------------------------------------------
        # BUTTON AREA
        # -------------------------------------------------

        button_frame = ctk.CTkFrame(
            section,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=15,
            pady=(5, 18)
        )


        # Responsive columns

        for col in range(3):

            button_frame.grid_columnconfigure(
                col,
                weight=1
            )


        # -------------------------------------------------
        # BUTTONS
        # -------------------------------------------------

        for index, module in enumerate(modules):

            row = index // 3
            col = index % 3


            button = ctk.CTkButton(
                button_frame,

                text=(
                    f"{module['icon']}  {module['text']}\n"
                    f"{module['description']}"
                ),

                height=75,

                corner_radius=12,

                fg_color="#202E39",

                hover_color=CARD_HOVER,

                text_color=WHITE,

                font=("Arial", 14, "bold"),

                anchor="w",

                command=module["command"]
            )


            button.grid(
                row=row,
                column=col,
                padx=7,
                pady=7,
                sticky="ew"
            )


    # =====================================================
    # STUDENT PROFILE
    # =====================================================

    create_section(
        "👤  Student Profile",
        "Manage your personal and account information",

        [

            {
                "icon": "👤",
                "text": "My Profile",
                "description": "View your profile",
                "command": lambda p=profile:
                    open_profile(p)
            },

            {
                "icon": "✏️",
                "text": "Edit Profile",
                "description": "Update your details",
                "command": lambda p=profile:
                    edit_profile(p)
            },

            {
                "icon": "🔐",
                "text": "Change Password",
                "description": "Secure your account",
                "command": lambda p=profile:
                    change_password(p)
            }

        ]
    )


    # =====================================================
    # RESUME & CAREER
    # =====================================================

    create_section(
        "📄  Resume & Career",
        "Improve your resume and discover suitable career options",

        [

            {
                "icon": "📊",
                "text": "Resume Analyzer",
                "description": "Check & improve resume",
                "command": lambda p=profile:
                    resume_analyzer(p)
            },

            {
                "icon": "📝",
                "text": "Resume Builder",
                "description": "Create professional resume",
                "command": lambda p=profile:
                    resume_builder(p)
            },

            {
                "icon": "🏢",
                "text": "Company Eligibility",
                "description": "Check eligible companies",
                "command": lambda p=profile:
                    company_eligibility(p)
            },

            {
                "icon": "🎯",
                "text": "Placement Prediction",
                "description": "Check placement probability",
                "command": lambda p=profile:
                    placement_prediction(p[5])
            },

            {
                "icon": "💼",
                "text": "Job Recommendation",
                "description": "Find suitable job roles",
                "command": job_recommendation
            }

        ]
    )


    # =====================================================
    # PLACEMENT PREPARATION
    # =====================================================

    create_section(
        "🎯  Placement Preparation",
        "Practice technical and interview skills",

        [

            {
                "icon": "🧠",
                "text": "Quiz",
                "description": "Test your knowledge",
                "command": start_quiz
            },

            {
                "icon": "🎤",
                "text": "Mock Interview",
                "description": "Practice interview answers",
                "command": lambda p=profile:
                    mock_interview(p)
            }

        ]
    )


    # =====================================================
    # PROGRESS & SYSTEM
    # =====================================================

    create_section(
        "🏆  Progress & System",
        "Track your performance and manage the system",

        [

            {
                "icon": "📜",
                "text": "Certificate",
                "description": "Generate your certificate",
                "command": lambda p=profile:
                    generate_certificate(p)
            },

            {
                "icon": "🏆",
                "text": "Leaderboard",
                "description": "View student rankings",
                "command": leaderboard
            },

            {
                "icon": "🛠️",
                "text": "Admin Panel",
                "description": "Manage student data",
                "command": admin_panel
            },

            {
                "icon": "ℹ️",
                "text": "About Project",
                "description": "Learn about Placement OS",
                "command": about
            }

        ]
    )


    # =====================================================
    # LOGOUT
    # =====================================================

    logout_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    logout_frame.pack(
        fill="x",
        pady=(20, 10)
    )


    ctk.CTkButton(
        logout_frame,

        text="🚪  Logout",

        width=240,
        height=52,

        corner_radius=12,

        font=("Arial", 17, "bold"),

        fg_color=RED,

        hover_color=RED_HOVER,

        command=dashboard.destroy

    ).pack()


    # =====================================================
    # FOOTER
    # =====================================================

    ctk.CTkLabel(
        content,

        text=(
            "Placement OS  •  "
            "Student Placement & Career Assistance System"
        ),

        font=("Arial", 11),

        text_color=GRAY
    ).pack(
        pady=(5, 20)
    )


    # =====================================================
    # START
    # =====================================================

    dashboard.mainloop()