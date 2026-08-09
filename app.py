import os
from placement import placement_prediction
from jobs import job_recommendation
from quiz import start_quiz
from resume_builder import resume_builder
from certificate import generate_certificate
from edit_profile import edit_profile
from change_password import change_password 
from admin import admin_panel
from leaderboard import leaderboard 
from about import about
from database import check_user,add_user,login_user
from logger import write_log

write_log("testuser", "Testing Log")

print("=" * 40)
print("         PLACEMENT OS")
print("=" * 40)

print("Current Folder:", os.getcwd())

name = input("\nEnter your name: ")
print(f"Welcome, {name}!")


# ================= RESUME ANALYZER =================

def resume_analyzer():

    print("\n========== RESUME ANALYZER ==========")

    skills = [
        "Python",
        "C++",
        "Java",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "DBMS",
        "DSA",
        "OOP"
    ]

    score = 0

    for skill in skills:
        ans = input(f"Do you know {skill}? (y/n): ")

        if ans.lower() == "y":
            score += 10

    print("\n==============================")
    print("Resume Score :", score, "%")
    print("==============================")

    if score >= 90:
        print("Excellent Resume")
    elif score >= 70:
        print("Good Resume")
    elif score >= 50:
        print("Average Resume")
    else:
        print("Needs Improvement")

    print("\nSuggestions:")

    if score < 100:
        print("- Improve DSA")
        print("- Build Projects")
        print("- Practice Aptitude")
        print("- Improve Communication")
        print("- Learn Interview Questions")


# ================= COMPANY ELIGIBILITY =================

def company_eligibility(cgpa):

    cgpa = float(cgpa)

    print("\n========== COMPANY ELIGIBILITY ==========")

    if cgpa >= 8.5:
        print("✅ Eligible for TCS")
        print("✅ Eligible for Infosys")
        print("✅ Eligible for Accenture")
        print("✅ Eligible for Wipro")

    elif cgpa >= 7.5:
        print("✅ Eligible for Infosys")
        print("✅ Eligible for Wipro")
        print("✅ Eligible for Capgemini")

    elif cgpa >= 6.5:
        print("✅ Eligible for Wipro")
        print("✅ Eligible for HCL")

    else:
        print("❌ Improve your CGPA.")


# ================= MAIN MENU =================

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Login")
    print("2. Sign Up")
    print("3. Exit")

    option = input("Enter Choice: ")

    # ================= LOGIN =================

    if option == "1":

        username = input("Username: ")
        password = input("Password: ")

        profile = login_user(username, password)
        profile = list(profile) if profile else []

        if profile:
            login = True
        else:
            login = False

        if login:

            print("\n✅ Login Successful")
            write_log(profile[0], "Logged In")

            while True:

                print("\n========== DASHBOARD ==========")
                print("1. My Profile")
                print("2. Resume Analyzer")
                print("3. Company Eligibility")
                print("4. Placement prediction")
                print("5. Job Recommendation")
                print("6. Quiz")
                print("7. Resume builder")
                print("8. Certificate")
                print("9. Edit Profile")
                print("10.Change Password")
                print("11. Mock Interview")
                print("12. Admin Panel")
                print("13. Leaderboard")
                print("14. About Project")
                print("15. Logout")

                ch = input("Enter Choice: ")

                if ch == "1":

                    print("\n========== MY PROFILE ==========")
                    print("Full Name :", profile[2])
                    print("Username  :", profile[0])
                    print("College   :", profile[3])
                    print("Branch    :", profile[4])
                    print("CGPA      :", profile[5])

                elif ch == "2":

                    resume_analyzer()

                elif ch == "3":

                    company_eligibility(profile[5])

                elif ch == "4":
                    placement_prediction(profile[5])
                elif ch == "5": 
                    job_recommendation() 
                elif ch == "6":
                    start_quiz()
                elif ch == "7":
                    resume_builder(profile)
                elif ch == "8": 
                    generate_certificate(profile)
                elif ch == "9": 
                    edit_profile(profile)
                    write_log(profile[0], "Edited Profile")
                elif ch == "10":
                    change_password(profile)
                    write_log(profile[0], "Changed Password")
                elif ch == "11":                     

                    print("\n========== MOCK INTERVIEW ==========")

                    print("Q1. Tell me about yourself.")
                    input("Your Answer: ")

                    print("\nQ2. What are your strengths?")
                    input("Your Answer: ")

                    print("\nQ3. Why should we hire you?")
                    input("Your Answer: ")

                    print("\n🎉 Interview Completed Successfully")

                elif ch == "12":
                    admin_panel()
                elif ch == "13":
                    leaderboard()
                elif ch == "14":
                    about()
                elif ch == "15":

                    write_log(profile[0], "Logged Out") 

                    print("\nLogged Out Successfully")
                    break

                else:
                    print("Invalid Choice")

        else:

            print("\n❌ Invalid Username or Password")

         # ================= SIGN UP =================

    elif option == "2":

        print("\n========== SIGN UP ==========")

        username = input("Create Username: ")
        password = input("Create Password: ")
        fullname = input("Full Name: ")
        college = input("College: ")
        branch = input("Branch: ")
        cgpa = input("CGPA: ")

        if check_user(username):
            print("\n❌ Username already exists")

        else:

            try:

                cgpa = float(cgpa)

                add_user(
                    username,
                    password,
                    fullname,
                    college,
                    branch,
                    cgpa
            )

                print("\n✅ Account Created Successfully")

            except ValueError:

                print("\n❌ Invalid CGPA! Please enter a number.")

            except Exception as e:

                print("\n❌ Error:", e)

            print("\n✅ Account Created Successfully")


    # ================= EXIT =================

    elif option == "3":

        print("\nThank You!")
        break

    else:

        print("\nInvalid Choice")
        