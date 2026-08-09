import customtkinter as ctk
from database import get_leaderboard


# =========================================================
# APPEARANCE
# =========================================================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# =========================================================
# COLORS
# =========================================================

BLUE = "#1F6AA5"
BLUE_HOVER = "#15527F"

GREEN = "#2E8B57"
RED = "#C0392B"

DARK_CARD = "#1E1E1E"

TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#BDBDBD"


# =========================================================
# LEADERBOARD
# =========================================================

def leaderboard():

    # =====================================================
    # CREATE WINDOW
    # =====================================================

    window = ctk.CTkToplevel()

    window.title("Leaderboard")

    # Full screen
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
        text="🏆 LEADERBOARD",
        font=("Arial", 32, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 8)
    )

    ctk.CTkLabel(
        header,
        text="Top students based on academic performance",
        font=("Arial", 17),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 25)
    )


    # =====================================================
    # LEADERBOARD CARD
    # =====================================================

    leaderboard_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    leaderboard_frame.pack(
        fill="x",
        pady=10
    )


    # =====================================================
    # TITLE
    # =====================================================

    ctk.CTkLabel(
        leaderboard_frame,
        text="🥇 Student Rankings",
        font=("Arial", 26, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )


    # =====================================================
    # TABLE HEADER
    # =====================================================

    table_header = ctk.CTkFrame(
        leaderboard_frame,
        corner_radius=10,
        fg_color=BLUE
    )

    table_header.pack(
        fill="x",
        padx=25,
        pady=(0, 10)
    )


    # Rank
    ctk.CTkLabel(
        table_header,
        text="Rank",
        width=100,
        font=("Arial", 17, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        side="left",
        padx=15,
        pady=15
    )


    # Name
    ctk.CTkLabel(
        table_header,
        text="Student Name",
        width=400,
        anchor="w",
        font=("Arial", 17, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        side="left",
        padx=15,
        pady=15
    )


    # CGPA
    ctk.CTkLabel(
        table_header,
        text="CGPA",
        width=150,
        font=("Arial", 17, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        side="left",
        padx=15,
        pady=15
    )


    # =====================================================
    # DATA FRAME
    # =====================================================

    data_frame = ctk.CTkFrame(
        leaderboard_frame,
        fg_color="transparent"
    )

    data_frame.pack(
        fill="x",
        padx=25,
        pady=(0, 25)
    )


    # =====================================================
    # LOAD LEADERBOARD
    # =====================================================

    try:

        students = get_leaderboard()

    except Exception as error:

        ctk.CTkLabel(
            data_frame,
            text=f"Unable to load leaderboard.\n\n{error}",
            font=("Arial", 18),
            text_color=RED
        ).pack(
            pady=30
        )

        students = []


    # =====================================================
    # DISPLAY STUDENTS
    # =====================================================

    if not students:

        ctk.CTkLabel(
            data_frame,
            text="No leaderboard data available.",
            font=("Arial", 20),
            text_color=TEXT_GRAY
        ).pack(
            pady=40
        )

    else:

        for index, student in enumerate(
            students,
            start=1
        ):

            # =============================================
            # STUDENT CARD
            # =============================================

            if index == 1:

                row_color = "#6B5200"

            elif index == 2:

                row_color = "#454545"

            elif index == 3:

                row_color = "#5A3A29"

            else:

                row_color = DARK_CARD


            row = ctk.CTkFrame(
                data_frame,
                corner_radius=10,
                fg_color=row_color
            )

            row.pack(
                fill="x",
                pady=5
            )


            # =============================================
            # RANK
            # =============================================

            if index == 1:

                rank_text = "🥇 1"

            elif index == 2:

                rank_text = "🥈 2"

            elif index == 3:

                rank_text = "🥉 3"

            else:

                rank_text = str(index)


            ctk.CTkLabel(
                row,
                text=rank_text,
                width=100,
                font=("Arial", 18, "bold")
            ).pack(
                side="left",
                padx=15,
                pady=18
            )


            # =============================================
            # NAME
            # =============================================

            # get_leaderboard returns:
            # (fullname, cgpa)

            try:

                student_name = student[0]

                student_cgpa = student[1]

            except Exception:

                student_name = "Unknown"

                student_cgpa = "-"


            ctk.CTkLabel(
                row,
                text=str(student_name),
                width=400,
                anchor="w",
                font=("Arial", 18, "bold")
            ).pack(
                side="left",
                padx=15,
                pady=18
            )


            # =============================================
            # CGPA
            # =============================================

            ctk.CTkLabel(
                row,
                text=str(student_cgpa),
                width=150,
                font=("Arial", 18, "bold"),
                text_color=GREEN
            ).pack(
                side="left",
                padx=15,
                pady=18
            )


    # =====================================================
    # REFRESH FUNCTION
    # =====================================================

    def refresh():

        window.destroy()

        leaderboard()


    # =====================================================
    # BUTTON FRAME
    # =====================================================

    button_frame = ctk.CTkFrame(
        main,
        fg_color="transparent"
    )

    button_frame.pack(
        pady=20
    )


    # =====================================================
    # REFRESH BUTTON
    # =====================================================

    ctk.CTkButton(
        button_frame,
        text="🔄 Refresh",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=refresh
    ).pack(
        side="left",
        padx=10
    )


    # =====================================================
    # CLOSE BUTTON
    # =====================================================

    ctk.CTkButton(
        button_frame,
        text="❌ Close",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color="#962D22",
        command=window.destroy
    ).pack(
        side="left",
        padx=10
    )