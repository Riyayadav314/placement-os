import customtkinter as ctk


# ================= APPEARANCE =================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ================= PLACEMENT PREDICTION =================

def placement_prediction(cgpa):

    # Convert CGPA into number
    cgpa = float(cgpa)

    # ================= CREATE WINDOW =================

    window = ctk.CTkToplevel()

    window.title("Placement Prediction")

    window.state("zoomed")

    window.resizable(True, True)

    # ================= HEADER =================

    header = ctk.CTkFrame(
        window,
        height=90,
        corner_radius=0
    )

    header.pack(
        fill="x"
    )

    title = ctk.CTkLabel(
        header,
        text="📊 PLACEMENT PREDICTION",
        font=("Arial", 28, "bold")
    )

    title.pack(
        pady=25
    )

    # ================= CGPA =================

    cgpa_label = ctk.CTkLabel(
        window,
        text=f"Your CGPA : {cgpa}",
        font=("Arial", 20, "bold")
    )

    cgpa_label.pack(
        pady=(30, 10)
    )

    # ================= CALCULATE CHANCE =================

    if cgpa >= 9:

        chance = 95

    elif cgpa >= 8:

        chance = 85

    elif cgpa >= 7:

        chance = 70

    elif cgpa >= 6:

        chance = 55

    else:

        chance = 30

    # ================= RESULT =================

    if chance >= 85:

        result = "Excellent Chances of Placement"

    elif chance >= 70:

        result = "Good Chances of Placement"

    elif chance >= 50:

        result = "Average Chances"

    else:

        result = "Need More Preparation"

    # ================= CHANCE PERCENTAGE =================

    chance_label = ctk.CTkLabel(
        window,
        text=f"{chance}%",
        font=("Arial", 48, "bold")
    )

    chance_label.pack(
        pady=10
    )

    # ================= PROGRESS BAR =================

    progress = ctk.CTkProgressBar(
        window,
        width=500
    )

    progress.pack(
        pady=10
    )

    progress.set(
        chance / 100
    )

    # ================= RESULT TEXT =================

    result_label = ctk.CTkLabel(
        window,
        text=result,
        font=("Arial", 22, "bold")
    )

    result_label.pack(
        pady=15
    )

    # ================= SUGGESTIONS TITLE =================

    suggestion_title = ctk.CTkLabel(
        window,
        text="💡 Suggestions",
        font=("Arial", 20, "bold")
    )

    suggestion_title.pack(
        pady=(15, 5)
    )

    # ================= SUGGESTIONS BOX =================

    suggestions = ctk.CTkTextbox(
        window,
        width=500,
        height=150
    )

    suggestions.pack(
        pady=5
    )

    suggestions.insert(
        "1.0",
        "• Improve DSA\n"
        "• Build Projects\n"
        "• Practice Aptitude\n"
        "• Improve Communication Skills\n"
        "• Practice Interview Questions"
    )

    suggestions.configure(
        state="disabled"
    )

    # ================= CLOSE BUTTON =================

    close_btn = ctk.CTkButton(
        window,
        text="❌ Close",
        width=180,
        command=window.destroy
    )

    close_btn.pack(
        pady=20
    )