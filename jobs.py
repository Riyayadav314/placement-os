import customtkinter as ctk


# ================= APPEARANCE =================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ================= COLOR SETTINGS =================

BLUE = "#1F6AA5"
BLUE_HOVER = "#15527F"

GREEN = "#2E8B57"
GREEN_HOVER = "#246B45"

RED = "#C0392B"
RED_HOVER = "#962D22"

DARK_CARD = "#1E1E1E"
NORMAL_BUTTON = "#444444"
NORMAL_BUTTON_HOVER = "#555555"

TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#BDBDBD"


# ================= JOB RECOMMENDATION =================

def job_recommendation():

    # ================= CREATE WINDOW =================

    window = ctk.CTkToplevel()

    window.title("Job Recommendation")

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
        text="💼 JOB RECOMMENDATION",
        font=("Arial", 32, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 8)
    )

    ctk.CTkLabel(
        header,
        text="Find suitable career options based on your skills",
        font=("Arial", 17),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 25)
    )

    # ================= SKILLS SECTION =================

    ctk.CTkLabel(
        main,
        text="🧠 Select Your Skills",
        font=("Arial", 26, "bold")
    ).pack(
        anchor="w",
        pady=(10, 15)
    )

    skills_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    skills_frame.pack(
        fill="x",
        pady=10
    )

    # ================= SKILL VARIABLES =================

    python_var = ctk.StringVar(
        value="n"
    )

    sql_var = ctk.StringVar(
        value="n"
    )

    dsa_var = ctk.StringVar(
        value="n"
    )

    html_var = ctk.StringVar(
        value="n"
    )

    # ================= SKILL CARD FUNCTION =================

    def create_skill_card(
        parent,
        skill_name,
        variable,
        icon
    ):

        # ================= CREATE CARD =================

        card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            fg_color=DARK_CARD,
            border_width=2
        )

        card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # ================= SKILL NAME =================

        ctk.CTkLabel(
            card,
            text=f"{icon}  {skill_name}",
            font=("Arial", 20, "bold")
        ).pack(
            side="left",
            padx=25,
            pady=18
        )

        # ================= BUTTON UPDATE FUNCTION =================

        def update_buttons():

            # ================= YES SELECTED =================

            if variable.get() == "y":

                yes_button.configure(
                    fg_color=GREEN,
                    hover_color=GREEN_HOVER,
                    text="✓ YES"
                )

                no_button.configure(
                    fg_color=NORMAL_BUTTON,
                    hover_color=NORMAL_BUTTON_HOVER,
                    text="NO"
                )

            # ================= NO SELECTED =================

            else:

                no_button.configure(
                    fg_color=RED,
                    hover_color=RED_HOVER,
                    text="✓ NO"
                )

                yes_button.configure(
                    fg_color=NORMAL_BUTTON,
                    hover_color=NORMAL_BUTTON_HOVER,
                    text="YES"
                )

        # ================= SELECT YES =================

        def select_yes():

            variable.set("y")

            update_buttons()

        # ================= SELECT NO =================

        def select_no():

            variable.set("n")

            update_buttons()

        # ================= NO BUTTON =================

        no_button = ctk.CTkButton(
            card,
            text="✓ NO",
            width=100,
            height=40,
            fg_color=RED,
            hover_color=RED_HOVER,
            command=select_no
        )

        no_button.pack(
            side="right",
            padx=(5, 20),
            pady=15
        )

        # ================= YES BUTTON =================

        yes_button = ctk.CTkButton(
            card,
            text="YES",
            width=100,
            height=40,
            fg_color=NORMAL_BUTTON,
            hover_color=NORMAL_BUTTON_HOVER,
            command=select_yes
        )

        yes_button.pack(
            side="right",
            padx=5,
            pady=15
        )

        # ================= DEFAULT SELECTION =================

        update_buttons()

    # ================= CREATE PYTHON CARD =================

    create_skill_card(
        skills_frame,
        "Python",
        python_var,
        "🐍"
    )

    # ================= CREATE SQL CARD =================

    create_skill_card(
        skills_frame,
        "SQL",
        sql_var,
        "🗄️"
    )

    # ================= CREATE DSA CARD =================

    create_skill_card(
        skills_frame,
        "DSA",
        dsa_var,
        "🧩"
    )

    # ================= CREATE HTML / CSS CARD =================

    create_skill_card(
        skills_frame,
        "HTML / CSS",
        html_var,
        "🌐"
    )

    # ================= RESULT FRAME =================

    result_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    result_frame.pack(
        fill="x",
        pady=30
    )

    # ================= RESULT TITLE =================

    ctk.CTkLabel(
        result_frame,
        text="🎯 Recommended Jobs",
        font=("Arial", 26, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 10)
    )

    # ================= RESULT BOX =================

    result_box = ctk.CTkTextbox(
        result_frame,
        width=900,
        height=250,
        font=("Arial", 19)
    )

    result_box.pack(
        fill="x",
        padx=25,
        pady=15
    )

    result_box.insert(
        "1.0",
        "Select your skills above and click "
        "\"Get Job Recommendations\"."
    )

    result_box.configure(
        state="disabled"
    )

    # ================= RECOMMENDATION FUNCTION =================

    def show_recommendations():

        # ================= READ SELECTED SKILLS =================

        python = python_var.get()

        sql = sql_var.get()

        dsa = dsa_var.get()

        html = html_var.get()

        # ================= RECOMMENDATION LIST =================

        recommendations = []

        # ================= PYTHON DEVELOPER =================

        if python == "y":

            recommendations.append(
                "🐍 Python Developer"
            )

        # ================= DATA ANALYST =================

        if python == "y" and sql == "y":

            recommendations.append(
                "📊 Data Analyst"
            )

        # ================= SOFTWARE ENGINEER =================

        if python == "y" and dsa == "y":

            recommendations.append(
                "💻 Software Engineer"
            )

        # ================= FULL STACK PYTHON =================

        if python == "y" and html == "y":

            recommendations.append(
                "🌐 Full Stack Python Developer"
            )

        # ================= FRONTEND DEVELOPER =================

        if python == "n" and html == "y":

            recommendations.append(
                "🎨 Frontend Developer"
            )

        # ================= UPDATE RESULT BOX =================

        result_box.configure(
            state="normal"
        )

        result_box.delete(
            "1.0",
            "end"
        )

        # ================= SHOW RECOMMENDATIONS =================

        if recommendations:

            result_box.insert(
                "end",
                "Your Recommended Jobs:\n\n"
            )

            for job in recommendations:

                result_box.insert(
                    "end",
                    f"✓ {job}\n\n"
                )

            result_box.insert(
                "end",
                "💡 Keep Learning & Best of Luck!"
            )

        # ================= NO RECOMMENDATION =================

        else:

            result_box.insert(
                "end",
                "❌ No suitable recommendation found.\n\n"
                "Learn some technical skills first."
            )

        result_box.configure(
            state="disabled"
        )

    # ================= GET RECOMMENDATIONS BUTTON =================

    ctk.CTkButton(
        main,
        text="🔍 Get Job Recommendations",
        width=320,
        height=55,
        font=("Arial", 19, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=show_recommendations
    ).pack(
        pady=(0, 25)
    )

    # ================= CLOSE BUTTON =================

    ctk.CTkButton(
        main,
        text="❌ Close",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=window.destroy
    ).pack(
        pady=(0, 35)
    )