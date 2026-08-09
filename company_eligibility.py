import customtkinter as ctk


# ================= APPEARANCE =================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ================= COLOR SETTINGS =================

BLUE = "#1F6AA5"
GREEN = "#2E8B57"
RED = "#C0392B"
DARK_CARD = "#1E1E1E"
TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#BDBDBD"


# ================= COMPANY ELIGIBILITY =================

def company_eligibility(profile):

    # ================= STUDENT DATA =================

    name = profile[2]
    cgpa = float(profile[5])
    branch = profile[4]

    # ================= CREATE WINDOW =================

    window = ctk.CTkToplevel()

    window.title("Company Eligibility")

    # Full-screen / maximized window
    window.state("zoomed")

    window.resizable(True, True)

    # ================= MAIN SCROLL FRAME =================

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

    # ================= HEADER =================

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
        text="🏢 COMPANY ELIGIBILITY",
        font=("Arial", 32, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 8)
    )

    ctk.CTkLabel(
        header,
        text="Check which companies you are eligible for",
        font=("Arial", 17),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 25)
    )

    # ================= STUDENT INFORMATION =================

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
        text="👤 Student Information",
        font=("Arial", 23, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 15)
    )

    # Student name

    ctk.CTkLabel(
        info_frame,
        text=f"Name : {name}",
        font=("Arial", 19, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=5
    )

    # Branch

    ctk.CTkLabel(
        info_frame,
        text=f"Branch : {branch}",
        font=("Arial", 19)
    ).pack(
        anchor="w",
        padx=30,
        pady=5
    )

    # CGPA

    ctk.CTkLabel(
        info_frame,
        text=f"CGPA : {cgpa}",
        font=("Arial", 19)
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 20)
    )

    # ================= ELIGIBILITY LOGIC =================

    eligible = []

    if cgpa >= 8.5:

        eligible = [
            ("TCS", "CGPA ≥ 8.5"),
            ("Infosys", "CGPA ≥ 8.5"),
            ("Accenture", "CGPA ≥ 8.5"),
            ("Wipro", "CGPA ≥ 8.5")
        ]

    elif cgpa >= 7.5:

        eligible = [
            ("Infosys", "CGPA ≥ 7.5"),
            ("Wipro", "CGPA ≥ 7.5"),
            ("Capgemini", "CGPA ≥ 7.5")
        ]

    elif cgpa >= 6.5:

        eligible = [
            ("Wipro", "CGPA ≥ 6.5"),
            ("HCL", "CGPA ≥ 6.5")
        ]

    # ================= ELIGIBLE TITLE =================

    ctk.CTkLabel(
        main,
        text="✅ Eligible Companies",
        font=("Arial", 26, "bold")
    ).pack(
        anchor="w",
        pady=(30, 15)
    )

    # ================= COMPANY CARDS =================

    if eligible:

        company_frame = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )

        company_frame.pack(
            fill="x"
        )

        for company, requirement in eligible:

            card = ctk.CTkFrame(
                company_frame,
                corner_radius=12,
                fg_color=DARK_CARD,
                border_width=2,
                border_color=GREEN
            )

            card.pack(
                fill="x",
                pady=8,
                padx=10
            )

            # Company name

            ctk.CTkLabel(
                card,
                text=f"✓  {company}",
                font=("Arial", 22, "bold"),
                text_color=GREEN
            ).pack(
                anchor="w",
                padx=25,
                pady=(15, 5)
            )

            # Requirement

            ctk.CTkLabel(
                card,
                text=f"Minimum Requirement: {requirement}",
                font=("Arial", 16),
                text_color=TEXT_GRAY
            ).pack(
                anchor="w",
                padx=25,
                pady=(0, 15)
            )

    else:

        # ================= NO ELIGIBILITY =================

        no_card = ctk.CTkFrame(
            main,
            corner_radius=15,
            fg_color=DARK_CARD,
            border_width=2,
            border_color=RED
        )

        no_card.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            no_card,
            text="❌ No Company Eligibility",
            font=("Arial", 24, "bold"),
            text_color=RED
        ).pack(
            pady=(25, 10)
        )

        ctk.CTkLabel(
            no_card,
            text="Your current CGPA does not meet the defined company criteria.",
            font=("Arial", 17),
            text_color=TEXT_GRAY,
            wraplength=800
        ).pack(
            pady=(0, 10)
        )

        ctk.CTkLabel(
            no_card,
            text="Improve your CGPA to increase your placement opportunities.",
            font=("Arial", 17),
            text_color=TEXT_GRAY,
            wraplength=800
        ).pack(
            pady=(0, 25)
        )

    # ================= PREPARATION MESSAGE =================

    preparation_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    preparation_frame.pack(
        fill="x",
        pady=30
    )

    ctk.CTkLabel(
        preparation_frame,
        text="💡 Placement Preparation",
        font=("Arial", 23, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 10)
    )

    ctk.CTkLabel(
        preparation_frame,
        text=(
            "Eligibility is based on the CGPA criteria currently defined "
            "in the Placement OS. Keep improving your DSA, projects, "
            "aptitude and interview preparation."
        ),
        font=("Arial", 17),
        text_color=TEXT_GRAY,
        wraplength=1000,
        justify="left"
    ).pack(
        anchor="w",
        padx=30,
        pady=(0, 20)
    )

    # ================= CLOSE BUTTON =================

    ctk.CTkButton(
        main,
        text="❌ Close",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color="#15527F",
        command=window.destroy
    ).pack(
        pady=(5, 35)
    )