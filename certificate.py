import customtkinter as ctk

import os

import uuid

from datetime import datetime

from tkinter import messagebox

from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import A4, landscape

from reportlab.lib import colors

from reportlab.pdfbase.pdfmetrics import stringWidth


# ================= APPEARANCE =================

ctk.set_appearance_mode("Dark")

ctk.set_default_color_theme("blue")


# ================= APPLICATION COLORS =================

BLUE = "#1F6AA5"

BLUE_HOVER = "#15527F"

GREEN = "#2E8B57"

RED = "#C0392B"

DARK_CARD = "#1E1E1E"

TEXT_WHITE = "#FFFFFF"

TEXT_GRAY = "#BDBDBD"


# ================= CERTIFICATE COLORS =================

CERT_BLUE = colors.HexColor("#1F6AA5")

CERT_DARK_BLUE = colors.HexColor("#123B5D")

CERT_GOLD = colors.HexColor("#C99A2E")

CERT_LIGHT = colors.HexColor("#F7F9FC")

CERT_GRAY = colors.HexColor("#555555")


# ================= GENERATE CERTIFICATE =================

def generate_certificate(profile):

    # ================= STUDENT INFORMATION =================

    name = str(profile[2])

    college = str(profile[3])

    branch = str(profile[4])

    cgpa = str(profile[5])

    # ================= CURRENT DATE =================

    current_date = datetime.now().strftime(
        "%d %B %Y"
    )

    # ================= UNIQUE CERTIFICATE ID =================

    certificate_id = (
        "POS-"
        + datetime.now().strftime("%Y")
        + "-"
        + uuid.uuid4().hex[:6].upper()
    )

    # ================= CREATE WINDOW =================

    window = ctk.CTkToplevel()

    window.title(
        "Placement OS Certificate"
    )

    # Full-screen / maximized

    window.state(
        "zoomed"
    )

    window.resizable(
        True,
        True
    )

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
        text="🎓 PLACEMENT OS CERTIFICATE",
        font=("Arial", 32, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 8)
    )

    ctk.CTkLabel(
        header,
        text="Certificate of Achievement",
        font=("Arial", 18),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 25)
    )

    # ================= INFORMATION CARD =================

    info_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    info_card.pack(
        fill="x",
        pady=10
    )

    ctk.CTkLabel(
        info_card,
        text="👤 Certificate Information",
        font=("Arial", 24, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 15)
    )

    # ================= NAME =================

    ctk.CTkLabel(
        info_card,
        text=f"Name : {name}",
        font=("Arial", 19, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=5
    )

    # ================= COLLEGE =================

    ctk.CTkLabel(
        info_card,
        text=f"College : {college}",
        font=("Arial", 18)
    ).pack(
        anchor="w",
        padx=30,
        pady=5
    )

    # ================= BRANCH =================

    ctk.CTkLabel(
        info_card,
        text=f"Branch : {branch}",
        font=("Arial", 18)
    ).pack(
        anchor="w",
        padx=30,
        pady=5
    )

    # ================= CGPA =================

    ctk.CTkLabel(
        info_card,
        text=f"CGPA : {cgpa}",
        font=("Arial", 18)
    ).pack(
        anchor="w",
        padx=30,
        pady=5
    )

    # ================= DATE =================

    ctk.CTkLabel(
        info_card,
        text=f"Date : {current_date}",
        font=("Arial", 18)
    ).pack(
        anchor="w",
        padx=30,
        pady=5
    )

    # ================= CERTIFICATE ID =================

    ctk.CTkLabel(
        info_card,
        text=f"Certificate ID : {certificate_id}",
        font=("Arial", 18, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 25)
    )

    # ================= PREVIEW CARD =================

    preview_card = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    preview_card.pack(
        fill="x",
        pady=30
    )

    ctk.CTkLabel(
        preview_card,
        text="👀 Certificate Preview",
        font=("Arial", 24, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 15)
    )

    # ================= PREVIEW BOX =================

    preview_box = ctk.CTkTextbox(
        preview_card,
        width=1000,
        height=360,
        font=("Arial", 18)
    )

    preview_box.pack(
        fill="x",
        padx=30,
        pady=(0, 25)
    )

    # ================= PREVIEW CONTENT =================

    preview_text = f"""
╔══════════════════════════════════════════════════════════╗

                 PLACEMENT OS

             CERTIFICATE OF ACHIEVEMENT


                    This is to certify that


                       {name}


          has successfully completed the

             Placement OS Assessment


College : {college}

Branch  : {branch}

CGPA    : {cgpa}


Date : {current_date}

Certificate ID : {certificate_id}


             STATUS : SUCCESSFULLY COMPLETED

╚══════════════════════════════════════════════════════════╝
"""

    preview_box.insert(
        "1.0",
        preview_text
    )

    preview_box.configure(
        state="disabled"
    )

    # ================= GENERATE PDF FUNCTION =================

    def create_certificate_pdf():

        # ================= SAFE FILE NAME =================

        safe_name = "".join(
            character
            for character in name
            if character.isalnum()
            or character in (
                " ",
                "_",
                "-"
            )
        ).strip()

        if not safe_name:

            safe_name = "Student"

        # ================= PDF FILE NAME =================

        filename = (
            f"certificate_{safe_name}.pdf"
        )

        # ================= PAGE SIZE =================

        page_width, page_height = landscape(
            A4
        )

        # ================= CREATE PDF =================

        pdf = canvas.Canvas(
            filename,
            pagesize=landscape(A4)
        )

        # ================= BACKGROUND =================

        pdf.setFillColor(
            colors.white
        )

        pdf.rect(
            0,
            0,
            page_width,
            page_height,
            fill=1,
            stroke=0
        )

        # ================= OUTER BORDER =================

        pdf.setStrokeColor(
            CERT_DARK_BLUE
        )

        pdf.setLineWidth(
            5
        )

        pdf.rect(
            25,
            25,
            page_width - 50,
            page_height - 50,
            fill=0,
            stroke=1
        )

        # ================= INNER BORDER =================

        pdf.setStrokeColor(
            CERT_GOLD
        )

        pdf.setLineWidth(
            2
        )

        pdf.rect(
            38,
            38,
            page_width - 76,
            page_height - 76,
            fill=0,
            stroke=1
        )

        # ================= TOP BRAND =================

        pdf.setFillColor(
            CERT_BLUE
        )

        pdf.setFont(
            "Helvetica-Bold",
            26
        )

        pdf.drawCentredString(
            page_width / 2,
            page_height - 85,
            "PLACEMENT OS"
        )

        # ================= CERTIFICATE TITLE =================

        pdf.setFillColor(
            CERT_DARK_BLUE
        )

        pdf.setFont(
            "Helvetica-Bold",
            30
        )

        pdf.drawCentredString(
            page_width / 2,
            page_height - 130,
            "CERTIFICATE OF ACHIEVEMENT"
        )

        # ================= SUBTITLE =================

        pdf.setFillColor(
            CERT_GRAY
        )

        pdf.setFont(
            "Helvetica",
            13
        )

        pdf.drawCentredString(
            page_width / 2,
            page_height - 160,
            "This certificate is proudly presented to"
        )

        # ================= STUDENT NAME =================

        pdf.setFillColor(
            CERT_DARK_BLUE
        )

        pdf.setFont(
            "Helvetica-Bold",
            34
        )

        pdf.drawCentredString(
            page_width / 2,
            page_height - 215,
            name
        )

        # ================= GOLD LINE =================

        pdf.setStrokeColor(
            CERT_GOLD
        )

        pdf.setLineWidth(
            2
        )

        pdf.line(
            180,
            page_height - 230,
            page_width - 180,
            page_height - 230
        )

        # ================= COMPLETION TEXT =================

        pdf.setFillColor(
            CERT_GRAY
        )

        pdf.setFont(
            "Helvetica",
            14
        )

        pdf.drawCentredString(
            page_width / 2,
            page_height - 265,
            "for successfully completing the"
        )

        pdf.setFillColor(
            CERT_BLUE
        )

        pdf.setFont(
            "Helvetica-Bold",
            18
        )

        pdf.drawCentredString(
            page_width / 2,
            page_height - 292,
            "Placement OS Assessment"
        )

        # ================= STUDENT DETAILS =================

        detail_y = page_height - 350

        pdf.setFillColor(
            CERT_GRAY
        )

        pdf.setFont(
            "Helvetica",
            12
        )

        pdf.drawCentredString(
            page_width / 2,
            detail_y,
            f"College : {college}"
        )

        pdf.drawCentredString(
            page_width / 2,
            detail_y - 22,
            f"Branch : {branch}"
        )

        pdf.drawCentredString(
            page_width / 2,
            detail_y - 44,
            f"CGPA : {cgpa}"
        )

        # ================= STATUS =================

        pdf.setFillColor(
            CERT_DARK_BLUE
        )

        pdf.setFont(
            "Helvetica-Bold",
            13
        )

        pdf.drawCentredString(
            page_width / 2,
            detail_y - 80,
            "STATUS : SUCCESSFULLY COMPLETED"
        )

        # ================= DATE =================

        pdf.setFillColor(
            CERT_GRAY
        )

        pdf.setFont(
            "Helvetica",
            10
        )

        pdf.drawString(
            75,
            75,
            f"Date : {current_date}"
        )

        # ================= CERTIFICATE ID =================

        pdf.drawRightString(
            page_width - 75,
            75,
            f"Certificate ID : {certificate_id}"
        )

        # ================= FOOTER =================

        pdf.setFillColor(
            CERT_BLUE
        )

        pdf.setFont(
            "Helvetica-Bold",
            11
        )

        pdf.drawCentredString(
            page_width / 2,
            75,
            "PLACEMENT OS"
        )

        # ================= SAVE PDF =================

        pdf.save()

        # ================= SUCCESS MESSAGE =================

        messagebox.showinfo(
            "Certificate Generated",
            f"Certificate generated successfully!\n\n"
            f"File : {filename}\n\n"
            f"Certificate ID : {certificate_id}"
        )

        # ================= OPEN PDF =================

        try:

            os.startfile(
                os.path.abspath(filename)
            )

        except Exception:

            pass

    # ================= BUTTON FRAME =================

    button_frame = ctk.CTkFrame(
        main,
        fg_color="transparent"
    )

    button_frame.pack(
        pady=(0, 35)
    )

    # ================= GENERATE PDF BUTTON =================

    ctk.CTkButton(
        button_frame,
        text="📄 Generate Certificate PDF",
        width=280,
        height=55,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=create_certificate_pdf
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    # ================= CLOSE BUTTON =================

    ctk.CTkButton(
        button_frame,
        text="❌ Close",
        width=220,
        height=55,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color="#962D22",
        command=window.destroy
    ).grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )