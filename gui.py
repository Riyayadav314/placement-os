import customtkinter as ctk
from tkinter import messagebox
from dashboard import open_dashboard

from database import login_user, add_user, check_user

# ---------------- LOGIN FUNCTION ----------------

def login():

    user = username.get()
    pwd = password.get()

    profile = login_user(user, pwd)
    

    if profile:
        print(profile)
        print(len(profile))

        app.destroy()

        open_dashboard(profile)

    else:
        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )


# ---------------- SIGNUP FUNCTION ----------------

def signup():

    win = ctk.CTkToplevel(app)
    win.title("Sign Up")
    win.geometry("400x500")

    ctk.CTkLabel(
        win,
        text="Create Account",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    u = ctk.CTkEntry(win, placeholder_text="Username")
    u.pack(pady=8)

    p = ctk.CTkEntry(win, placeholder_text="Password", show="*")
    p.pack(pady=8)

    n = ctk.CTkEntry(win, placeholder_text="Full Name")
    n.pack(pady=8)

    c = ctk.CTkEntry(win, placeholder_text="College")
    c.pack(pady=8)

    b = ctk.CTkEntry(win, placeholder_text="Branch")
    b.pack(pady=8)

    g = ctk.CTkEntry(win, placeholder_text="CGPA")
    g.pack(pady=8)
    email = ctk.CTkEntry(
        win,
        placeholder_text="Email",
        width=300
)
    email.pack(pady=8)

    mobile = ctk.CTkEntry(
        win,
        placeholder_text="Mobile Number",
        width=300
)
    mobile.pack(pady=8)

    city = ctk.CTkEntry(
        win,
        placeholder_text="City",
        width=300
)
    city.pack(pady=8)

    address = ctk.CTkEntry(
        win,
        placeholder_text="Address",
        width=300
)
    address.pack(pady=8)

    def create():
        print("Create button clicked")

        username = u.get()
        password = p.get()
        fullname = n.get()
        college = c.get()
        branch = b.get()

        try:
            cgpa = float(g.get())
        except:
            messagebox.showerror(
                "Error",
                "Invalid CGPA"
            )
            
            return
        
        # New Variables

        email_id = email.get().strip()

        mobile_no = mobile.get().strip()

        city_name = city.get().strip()

        address_text = address.get().strip()

        if check_user(username):
            messagebox.showerror(
                "Error",
                "Username already exists"
            )
            return

        add_user(
            username,
            password,
            fullname,
            college,
            branch,
            cgpa,
            email_id,
            mobile_no,
            city_name,
            address_text  
        )         

        messagebox.showinfo(
            "Success",
            "Account Created Successfully"
        )

        win.destroy()


    ctk.CTkButton(
        win,
        text="Create Account",
        command=create
    ).pack(pady=20)


# ---------------- GUI ----------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Placement OS")
app.geometry("700x500")

title = ctk.CTkLabel(
    app,
    text="PLACEMENT OS",
    font=("Arial",30,"bold")
)
title.pack(pady=30)

username = ctk.CTkEntry(
    app,
    placeholder_text="Username",
    width=300
)
username.pack(pady=10)

password = ctk.CTkEntry(
    app,
    placeholder_text="Password",
    show="*",
    width=300
)
password.pack(pady=10)

login_btn = ctk.CTkButton(
    app,
    text="Login",
    width=300,
    command=login
)
login_btn.pack(pady=15)

signup_btn = ctk.CTkButton(
    app,
    text="Sign Up",
    width=300,
    command=signup
)
signup_btn.pack()

app.mainloop()