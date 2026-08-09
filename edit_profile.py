import customtkinter as ctk
from tkinter import messagebox

from database import update_profile

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def edit_profile(profile):

    window = ctk.CTkToplevel()

    window.title("Edit Profile")

    window.geometry("650x720")

    window.resizable(False, False)

    # ================= TITLE =================

    title = ctk.CTkLabel(
        window,
        text="✏ EDIT PROFILE",
        font=("Arial", 28, "bold")
    )

    title.pack(pady=20)

    # ================= FULL NAME =================

    fullname = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="Full Name"
    )
    fullname.insert(0, profile[2])
    fullname.pack(pady=8)

    # ================= COLLEGE =================

    college = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="College"
    )
    college.insert(0, profile[3])
    college.pack(pady=8)

    # ================= BRANCH =================

    branch = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="Branch"
    )
    branch.insert(0, profile[4])
    branch.pack(pady=8)

    # ================= CGPA =================

    cgpa = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="CGPA"
    )
    cgpa.insert(0, str(profile[5]))
    cgpa.pack(pady=8)

    # ================= EMAIL =================

    email = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="Email"
    )
    email.insert(0, profile[6])
    email.pack(pady=8)

    # ================= MOBILE =================

    mobile = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="Mobile Number"
    )
    mobile.insert(0, profile[7])
    mobile.pack(pady=8)

    # ================= CITY =================

    city = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="City"
    )
    city.insert(0, profile[8])
    city.pack(pady=8)

    # ================= ADDRESS =================

    address = ctk.CTkEntry(
        window,
        width=380,
        placeholder_text="Address"
    )
    address.insert(0, profile[9])
    address.pack(pady=8)

    # ================= BUTTON FRAME =================

    button_frame = ctk.CTkFrame(
        window,
        fg_color="transparent"
    )

    button_frame.pack(pady=25)
        # ================= SAVE FUNCTION =================

    def save_profile():

        try:
            cgpa_value = float(cgpa.get())

        except:
            messagebox.showerror(
                "Error",
                "Please enter valid CGPA."
            )
            return

        update_profile(
            profile[0],          # username
            fullname.get(),
            college.get(),
            branch.get(),
            cgpa_value,
            email.get(),
            mobile.get(),
            city.get(),
            address.get()
        )

        messagebox.showinfo(
            "Success",
            "Profile Updated Successfully."
        )

        window.destroy()


    # ================= BUTTONS =================

    save_btn = ctk.CTkButton(
        button_frame,
        text="💾 Save",
        width=170,
        height=45,
        fg_color="#2E7D32",
        hover_color="#1B5E20",
        command=save_profile
    )

    save_btn.grid(
        row=0,
        column=0,
        padx=10
    )

    cancel_btn = ctk.CTkButton(
        button_frame,
        text="❌ Cancel",
        width=170,
        height=45,
        fg_color="#D32F2F",
        hover_color="#B71C1C",
        command=window.destroy
    )

    cancel_btn.grid(
        row=0,
        column=1,
        padx=10
    )