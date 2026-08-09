import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import os
import shutil

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def open_profile(profile):

    window = ctk.CTkToplevel()

    window.title("My Profile")

    window.geometry("900x750")
    window.minsize(900,750)

    window.resizable(True, True)


    # ================= PHOTO FUNCTION =================

    def upload_photo():
        print("Upload button clicked")

        folder= "profile_pics"

        if not os.path.exists(folder):
            os.makedirs(folder)

        file = filedialog.askopenfilename(
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg")
            ]
        )

        if file:
            print("Selected File:",file)

            extension = os.path.splitext(file)[1]

            new_file = os.path.join(
                folder,
                profile[0] + extension
            )
            print("Saving To:", new_file)

            shutil.copy(file, new_file)

            image = ctk.CTkImage(
                light_image=Image.open(new_file),
                dark_image=Image.open(new_file),
                size=(140,140)
            )

            avatar.configure(
                image=image,
                text=""
            )

            avatar.image = image


    # ================= HEADER =================

    header = ctk.CTkFrame(
        window,
        height=80,
        fg_color="#1565C0",
        corner_radius=0
    )

    header.pack(fill="x")

    heading = ctk.CTkLabel(
        header,
        text="👤 MY PROFILE",
        font=("Arial",30,"bold"),
        text_color="white"
    )

    heading.pack(pady=20)


    # ================= MAIN CARD =================

    card = ctk.CTkScrollableFrame(
       window,
       width=780,
       height=650,
       corner_radius=20
)

    card.pack(fill="both", expand=True, padx=20, pady=20)



    # ================= PROFILE PHOTO =================

    avatar = ctk.CTkLabel(
        card,
        text="👤",
        width=140,
        height=140,
        fg_color="#2B2B2B",
        corner_radius=70
)

    avatar.pack(pady=(20,10))


    # ================= LOAD PHOTO =================

    for ext in [".png",".jpg",".jpeg"]:

        photo = os.path.join(
            "profile_pics",
            profile[0] + ext
        )

        if os.path.exists(photo):

            image = ctk.CTkImage(
                light_image=Image.open(photo),
                dark_image=Image.open(photo),
                size=(140,140)
            )

            avatar.configure(
                image=image,
                text="",
                width=140,
                height=140
            )

            avatar.image = image

            break


    upload = ctk.CTkButton(
        card,
        text="📷 Upload Photo",
        width=200,
        height=40,
        command=upload_photo
    )

    upload.pack(pady=5)
    # ================= NAME =================

    name = ctk.CTkLabel(
        card,
        text=profile[2],
        font=("Arial", 24, "bold"),
        text_color="#4DA6FF"
    )

    name.pack(pady=(10,5))

    line = ctk.CTkLabel(
        card,
        text="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        font=("Arial",12)
    )

    line.pack(pady=5)


    # ================= DETAILS =================

    details_frame = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    details_frame.pack(pady=10)


    details = [

    ("🆔 Username", profile[0]),
    ("🏫 College", profile[3]),
    ("💻 Branch", profile[4]),
    ("🎓 CGPA", profile[5]),
    ("📧 Email", profile[6]),
    ("📱 Mobile", profile[7]),
    ("📍 City", profile[8]),
    ("🏠 Address", profile[9])

]


    for title, value in details:

        row = ctk.CTkFrame(
            details_frame,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=25,
            pady=8
        )

        left = ctk.CTkLabel(
            row,
            text=title,
            font=("Arial",17,"bold"),
            width=170,
            anchor="w"
        )

        left.pack(side="left")

        right = ctk.CTkLabel(
            row,
            text=str(value),
            font=("Arial",17)
        )

        right.pack(side="left")


    # ================= PROGRESS =================

    progress_title = ctk.CTkLabel(
        card,
        text="Placement Readiness",
        font=("Arial",18,"bold")
    )

    progress_title.pack(pady=(15,5))

    cgpa = float(profile[5])

    value = cgpa / 10

    progress = ctk.CTkProgressBar(
        card,
        width=320
    )

    progress.pack()

    progress.set(value)

    percent = ctk.CTkLabel(
        card,
        text=f"{int(value*100)} %",
        font=("Arial",15,"bold"),
        text_color="green"
    )

    percent.pack(pady=5)
    # ================= BUTTONS =================

    button_frame = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    button_frame.pack(pady=25)

    edit_btn = ctk.CTkButton(
        button_frame,
        text="✏ Edit Profile",
        width=160,
        height=40,
        fg_color="#1976D2"
    )

    edit_btn.grid(
        row=0,
        column=0,
        padx=10
    )

    resume_btn = ctk.CTkButton(
        button_frame,
        text="📄 Resume",
        width=160,
        height=40,
        fg_color="#388E3C"
    )

    resume_btn.grid(
        row=0,
        column=1,
        padx=10
    )

    close_btn = ctk.CTkButton(
        button_frame,
        text="❌ Close",
        width=160,
        height=40,
        fg_color="red",
        hover_color="#B71C1C",
        command=window.destroy
    )

    close_btn.grid(
        row=1,
        column=0,
        columnspan=2,
        pady=15
    )