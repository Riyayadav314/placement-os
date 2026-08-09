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

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def coming_soon(name):
    messagebox.showinfo(
        "Coming Soon",
        f"{name} will be connected next."
    )


def open_dashboard(profile):

    dashboard = ctk.CTk()

    dashboard.title("Placement OS Dashboard")

    dashboard.geometry("900x700")

    title = ctk.CTkLabel(
        dashboard,
        text=f"Welcome {profile[2]}",
        font=("Arial", 30, "bold")
    )

    title.pack(pady=20)

    frame = ctk.CTkFrame(dashboard)

    frame.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    buttons = [

        "My Profile",
        "Resume Analyzer",
        "Company Eligibility",
        "Placement Prediction",
        "Job Recommendation",
        "Quiz",
        "Resume Builder",
        "Certificate",
        "Edit Profile",
        "Change Password",
        "Mock Interview",
        "Admin Panel",
        "Leaderboard",
        "About Project",
        "Logout"

    ]

    row = 0
    col = 0

    for text in buttons:

        if text == "My Profile":
            cmd = lambda p=profile: open_profile(p)

        elif text == "Edit Profile":
            cmd = lambda p=profile: edit_profile(p)
        elif text == "Resume Analyzer":
        # Resume Analyzer ko current student profile ke saath open karega
             cmd = lambda p=profile: resume_analyzer(p)

        elif text == "Resume Builder":
            cmd = lambda p=profile: resume_builder(p)

        elif text == "Placement Prediction":

            cmd = lambda p=profile: placement_prediction(
                p[5]
            )
        elif text == "Company Eligibility":

            cmd = lambda p=profile: company_eligibility(
                p
            )

        elif text == "Job Recommendation":
            cmd = job_recommendation

        elif text == "Quiz":
            cmd = start_quiz

        elif text == "Certificate":
            cmd = lambda p=profile: generate_certificate(p)
        elif text == "Mock Interview":

           cmd = lambda p=profile: mock_interview(p)

        elif text == "Change Password":
            cmd = lambda p=profile: change_password(p)

        elif text == "Admin Panel":
            cmd = admin_panel

        elif text == "Leaderboard":
            cmd = leaderboard

        elif text == "About Project":
            cmd = about

        elif text == "Logout":
            cmd = dashboard.destroy

        else:
            cmd = lambda t=text: coming_soon(t)

        btn = ctk.CTkButton(
            frame,
            text=text,
            width=180,
            height=50,
            font=("Arial", 16, "bold"),
            command=cmd
        )

        btn.grid(
            row=row,
            column=col,
            padx=15,
            pady=15
        )

        col += 1

        if col == 2:
            col = 0
            row += 1

    dashboard.mainloop()