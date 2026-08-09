from openpyxl import Workbook
from database import get_admin_data, export_users,search_user,delete_user
import matplotlib.pyplot as plt
from collections import Counter


def admin_panel():

    print("\n========== ADMIN PANEL ==========")

    users, total_users, top_student = get_admin_data()

    print("Total Registered Users :", total_users)

    if top_student:
        print("Highest CGPA           :", top_student[1])
        print("Top Student            :", top_student[0])
    else:
        print("Highest CGPA           : 0")
        print("Top Student            : No Data")

    print("\n========== ALL USERS ==========")

    for user in users:

        print("------------------------------")
        print("Name    :", user[2])
        print("College :", user[3])
        print("Branch  :", user[4])
        print("CGPA    :", user[5])

    # ================= EXCEL EXPORT =================

    wb = Workbook()

    sheet = wb.active

    sheet.title = "Students"

    sheet.append([
        "Username",
        "Full Name",
        "College",
        "Branch",
        "CGPA"
    ])

    data = export_users()

    for row in data:
        sheet.append(row)

    wb.save("students.xlsx")
    # ================= BRANCH GRAPH =================

    branches = []

    for user in users:
        branches.append(user[4])

    count = Counter(branches)

    plt.figure(figsize=(6, 4))
    plt.bar(count.keys(), count.values())

    plt.title("Branch Wise Students")
    plt.xlabel("Branch")
    plt.ylabel("No. of Students")

    plt.show()
        
    # ================= CGPA GRAPH =================

    names = []
    cgpas = []

    for user in users:
        names.append(user[2])
        cgpas.append(user[5])

    plt.figure(figsize=(7, 4))
    plt.bar(names, cgpas)

    plt.title("Student CGPA")
    plt.xlabel("Students")
    plt.ylabel("CGPA")

    plt.ylim(0, 10)

    plt.show() 

    print("\n✅ Excel file saved as students.xlsx")

    print("\n✅ Admin Panel Loaded Successfully")

    # ================= SEARCH STUDENT =================

    print("\n========== SEARCH STUDENT ==========")

    username = input("Enter Username: ")

    student = search_user(username)

    if student:

        print("\n✅ Student Found")
        print("----------------------------")
        print("Name     :", student[2])
        print("Username :", student[0])
        print("College  :", student[3])
        print("Branch   :", student[4])
        print("CGPA     :", student[5])

    else:

        print("\n❌ Student Not Found")

    # ================= DELETE STUDENT =================

    print("\n========== DELETE STUDENT ==========")

    username = input("Enter Username to Delete: ")

    deleted = delete_user(username)

    if deleted:

        print("\n✅ User Deleted Successfully")

    else:

        print("\n❌ User Not Found")