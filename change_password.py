import customtkinter as ctk
from tkinter import messagebox

from database import login_user, update_password


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
GREEN_HOVER = "#246B45"

RED = "#C0392B"
RED_HOVER = "#962D22"

DARK_CARD = "#1E1E1E"
DARK_INPUT = "#252525"

TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#BDBDBD"

ORANGE = "#D68910"


# =========================================================
# CHANGE PASSWORD
# =========================================================

def change_password(profile):

    # =====================================================
    # CREATE WINDOW
    # =====================================================

    window = ctk.CTkToplevel()

    window.title("Change Password")

    # Full-screen / maximized
    window.state("zoomed")

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
        padx=30,
        pady=25
    )


    # =====================================================
    # HEADER
    # =====================================================

    header = ctk.CTkFrame(
        main,
        corner_radius=16,
        fg_color=BLUE
    )

    header.pack(
        fill="x",
        pady=(0, 20)
    )


    ctk.CTkLabel(
        header,
        text="🔐 CHANGE PASSWORD",
        font=("Arial", 30, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(22, 5)
    )


    ctk.CTkLabel(
        header,
        text="Update your account password securely",
        font=("Arial", 16),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 22)
    )


    # =====================================================
    # MAIN PASSWORD CARD
    # =====================================================

    card = ctk.CTkFrame(
        main,
        corner_radius=18,
        fg_color=DARK_CARD
    )

    card.pack(
        fill="x",
        padx=100,
        pady=10
    )


    # =====================================================
    # CARD TITLE
    # =====================================================

    ctk.CTkLabel(
        card,
        text="🛡️  Password Security",
        font=("Arial", 25, "bold")
    ).pack(
        anchor="w",
        padx=40,
        pady=(25, 20)
    )


    # =====================================================
    # CURRENT PASSWORD
    # =====================================================

    ctk.CTkLabel(
        card,
        text="Current Password",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=40,
        pady=(0, 7)
    )


    current_password = ctk.CTkEntry(
        card,
        height=48,
        font=("Arial", 16),
        show="•",
        placeholder_text="Enter your current password",
        fg_color=DARK_INPUT
    )

    current_password.pack(
        fill="x",
        padx=40,
        pady=(0, 18)
    )


    # =====================================================
    # NEW PASSWORD
    # =====================================================

    ctk.CTkLabel(
        card,
        text="New Password",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=40,
        pady=(0, 7)
    )


    new_password = ctk.CTkEntry(
        card,
        height=48,
        font=("Arial", 16),
        show="•",
        placeholder_text="Enter your new password",
        fg_color=DARK_INPUT
    )

    new_password.pack(
        fill="x",
        padx=40,
        pady=(0, 10)
    )


    # =====================================================
    # PASSWORD STRENGTH
    # =====================================================

    strength_label = ctk.CTkLabel(
        card,
        text="Password strength: Not entered",
        font=("Arial", 14),
        text_color=TEXT_GRAY
    )

    strength_label.pack(
        anchor="w",
        padx=40,
        pady=(0, 15)
    )


    # =====================================================
    # CONFIRM PASSWORD
    # =====================================================

    ctk.CTkLabel(
        card,
        text="Confirm New Password",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        padx=40,
        pady=(0, 7)
    )


    confirm_password = ctk.CTkEntry(
        card,
        height=48,
        font=("Arial", 16),
        show="•",
        placeholder_text="Re-enter your new password",
        fg_color=DARK_INPUT
    )

    confirm_password.pack(
        fill="x",
        padx=40,
        pady=(0, 12)
    )


    # =====================================================
    # CONFIRMATION STATUS
    # =====================================================

    match_label = ctk.CTkLabel(
        card,
        text="",
        font=("Arial", 14)
    )

    match_label.pack(
        anchor="w",
        padx=40,
        pady=(0, 15)
    )


    # =====================================================
    # SHOW / HIDE PASSWORD
    # =====================================================

    show_password_var = ctk.BooleanVar(
        value=False
    )


    def toggle_password():

        if show_password_var.get():

            current_password.configure(
                show=""
            )

            new_password.configure(
                show=""
            )

            confirm_password.configure(
                show=""
            )

        else:

            current_password.configure(
                show="•"
            )

            new_password.configure(
                show="•"
            )

            confirm_password.configure(
                show="•"
            )


    ctk.CTkCheckBox(
        card,
        text="Show Password",
        variable=show_password_var,
        command=toggle_password,
        font=("Arial", 15)
    ).pack(
        anchor="w",
        padx=40,
        pady=(0, 20)
    )


    # =====================================================
    # PASSWORD REQUIREMENTS
    # =====================================================

    requirements_frame = ctk.CTkFrame(
        card,
        corner_radius=12,
        fg_color="#181818"
    )

    requirements_frame.pack(
        fill="x",
        padx=40,
        pady=(0, 25)
    )


    ctk.CTkLabel(
        requirements_frame,
        text="🔎 Password Requirements",
        font=("Arial", 16, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 8)
    )


    ctk.CTkLabel(
        requirements_frame,
        text=(
            "✓ Minimum 6 characters\n"
            "✓ New password should be different from current password\n"
            "✓ Confirm password must match the new password"
        ),
        font=("Arial", 14),
        text_color=TEXT_GRAY,
        justify="left"
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 15)
    )


    # =====================================================
    # PASSWORD STRENGTH FUNCTION
    # =====================================================

    def check_strength(event=None):

        password = new_password.get()


        if not password:

            strength_label.configure(
                text="Password strength: Not entered",
                text_color=TEXT_GRAY
            )

            return


        score = 0


        # Length
        if len(password) >= 6:
            score += 1

        if len(password) >= 10:
            score += 1


        # Uppercase
        if any(
            char.isupper()
            for char in password
        ):
            score += 1


        # Lowercase
        if any(
            char.islower()
            for char in password
        ):
            score += 1


        # Number
        if any(
            char.isdigit()
            for char in password
        ):
            score += 1


        # Special character
        if any(
            not char.isalnum()
            for char in password
        ):
            score += 1


        if score <= 2:

            strength_label.configure(
                text="Password strength: Weak",
                text_color=RED
            )

        elif score <= 4:

            strength_label.configure(
                text="Password strength: Medium",
                text_color=ORANGE
            )

        else:

            strength_label.configure(
                text="Password strength: Strong",
                text_color=GREEN
            )


    new_password.bind(
        "<KeyRelease>",
        check_strength
    )


    # =====================================================
    # CONFIRM PASSWORD CHECK
    # =====================================================

    def check_match(event=None):

        new = new_password.get()

        confirm = confirm_password.get()


        if not confirm:

            match_label.configure(
                text=""
            )

        elif new == confirm:

            match_label.configure(
                text="✓ Passwords match",
                text_color=GREEN
            )

        else:

            match_label.configure(
                text="✗ Passwords do not match",
                text_color=RED
            )


    confirm_password.bind(
        "<KeyRelease>",
        check_match
    )

    new_password.bind(
        "<KeyRelease>",
        check_match
    )


    # =====================================================
    # UPDATE PASSWORD
    # =====================================================

    def update():

        current = current_password.get().strip()

        new = new_password.get()

        confirm = confirm_password.get()


        # -------------------------------------------------
        # EMPTY CHECK
        # -------------------------------------------------

        if not current:

            messagebox.showwarning(
                "Missing Password",
                "Please enter your current password.",
                parent=window
            )

            current_password.focus()

            return


        if not new:

            messagebox.showwarning(
                "Missing Password",
                "Please enter a new password.",
                parent=window
            )

            new_password.focus()

            return


        if not confirm:

            messagebox.showwarning(
                "Missing Password",
                "Please confirm your new password.",
                parent=window
            )

            confirm_password.focus()

            return


        # -------------------------------------------------
        # PASSWORD LENGTH
        # -------------------------------------------------

        if len(new) < 6:

            messagebox.showwarning(
                "Weak Password",
                "New password must contain at least 6 characters.",
                parent=window
            )

            new_password.focus()

            return


        # -------------------------------------------------
        # PASSWORD MATCH
        # -------------------------------------------------

        if new != confirm:

            messagebox.showerror(
                "Password Mismatch",
                "New password and confirm password do not match.",
                parent=window
            )

            confirm_password.focus()

            return


        # -------------------------------------------------
        # SAME PASSWORD CHECK
        # -------------------------------------------------

        if current == new:

            messagebox.showwarning(
                "Invalid Password",
                "New password must be different from your current password.",
                parent=window
            )

            new_password.focus()

            return


        # -------------------------------------------------
        # GET USERNAME
        # -------------------------------------------------

        try:

            username = profile[0]

        except Exception:

            messagebox.showerror(
                "Error",
                "Unable to identify your account.",
                parent=window
            )

            return


        # -------------------------------------------------
        # VERIFY CURRENT PASSWORD
        # -------------------------------------------------

        try:

            verified_user = login_user(
                username,
                current
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                f"Unable to verify current password.\n\n{error}",
                parent=window
            )

            return


        if not verified_user:

            messagebox.showerror(
                "Incorrect Password",
                "The current password you entered is incorrect.",
                parent=window
            )

            current_password.focus()

            return


        # -------------------------------------------------
        # UPDATE PASSWORD
        # -------------------------------------------------

        try:

            update_password(
                username,
                new
            )

        except Exception as error:

            messagebox.showerror(
                "Update Failed",
                f"Unable to update password.\n\n{error}",
                parent=window
            )

            return


        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        messagebox.showinfo(
            "Password Updated",
            "✓ Your password has been changed successfully.",
            parent=window
        )


        # Clear fields

        current_password.delete(
            0,
            "end"
        )

        new_password.delete(
            0,
            "end"
        )

        confirm_password.delete(
            0,
            "end"
        )


        strength_label.configure(
            text="Password strength: Not entered",
            text_color=TEXT_GRAY
        )

        match_label.configure(
            text=""
        )


        window.destroy()


    # =====================================================
    # BUTTON FRAME
    # =====================================================

    button_frame = ctk.CTkFrame(
        main,
        fg_color="transparent"
    )

    button_frame.pack(
        pady=(15, 15)
    )


    # =====================================================
    # UPDATE BUTTON
    # =====================================================

    ctk.CTkButton(
        button_frame,
        text="🔐 Update Password",
        width=260,
        height=55,
        font=("Arial", 18, "bold"),
        fg_color=GREEN,
        hover_color=GREEN_HOVER,
        command=update
    ).pack(
        side="left",
        padx=10
    )


    # =====================================================
    # CANCEL BUTTON
    # =====================================================

    ctk.CTkButton(
        button_frame,
        text="❌ Cancel",
        width=220,
        height=55,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color=RED_HOVER,
        command=window.destroy
    ).pack(
        side="left",
        padx=10
    )


    # =====================================================
    # FOOTER
    # =====================================================

    ctk.CTkLabel(
        main,
        text="🔒 Keep your password private and secure.",
        font=("Arial", 14),
        text_color=TEXT_GRAY
    ).pack(
        pady=(0, 25)
    )


    # =====================================================
    # INITIAL FOCUS
    # =====================================================

    current_password.focus()