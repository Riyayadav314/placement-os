from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def resume_builder(profile):

    print("\n========== RESUME ==========")

    print("Name     :", profile[2])
    print("Username :", profile[0])
    print("College  :", profile[3])
    print("Branch   :", profile[4])
    print("CGPA     :", profile[5])

    print("\nSkills")
    print("--------")
    print("✔ Python")
    print("✔ SQL")
    print("✔ DBMS")
    print("✔ DSA")
    print("✔ OOP")

    with open("resume.txt", "w", encoding="utf-8") as file:

        file.write("========== RESUME ==========\n")
        file.write(f"Name : {profile[2]}\n")
        file.write(f"Username : {profile[0]}\n")
        file.write(f"College : {profile[3]}\n")
        file.write(f"Branch : {profile[4]}\n")
        file.write(f"CGPA : {profile[5]}\n\n")

        file.write("Skills\n")
        file.write("Python\n")
        file.write("SQL\n")
        file.write("DBMS\n")
        file.write("DSA\n")
        file.write("OOP\n")
    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate("resume.pdf")

    content = []

    content.append(Paragraph("<b>RESUME</b>", styles["Heading1"]))

    content.append(Paragraph(f"<b>Name:</b> {profile[2]}", styles["Normal"]))
    content.append(Paragraph(f"<b>Username:</b> {profile[0]}", styles["Normal"]))
    content.append(Paragraph(f"<b>College:</b> {profile[3]}", styles["Normal"]))
    content.append(Paragraph(f"<b>Branch:</b> {profile[4]}", styles["Normal"]))
    content.append(Paragraph(f"<b>CGPA:</b> {profile[5]}", styles["Normal"]))

    content.append(Paragraph("<br/><b>Skills</b>", styles["Heading2"]))

    content.append(Paragraph("• Python", styles["Normal"]))
    content.append(Paragraph("• SQL", styles["Normal"]))
    content.append(Paragraph("• DBMS", styles["Normal"]))
    content.append(Paragraph("• DSA", styles["Normal"]))
    content.append(Paragraph("• OOP", styles["Normal"]))

    pdf.build(content)

    print("\n✅ Resume saved as resume.pdf")
    print("\n✅ Resume saved as resume.txt")