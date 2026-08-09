import customtkinter as ctk

import random

from tkinter import messagebox


# ================= APPEARANCE =================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ================= COLORS =================

BLUE = "#1F6AA5"
BLUE_HOVER = "#15527F"

GREEN = "#2E8B57"
GREEN_HOVER = "#246B45"

RED = "#C0392B"
RED_HOVER = "#962D22"

YELLOW = "#C99A2E"

DARK_CARD = "#1E1E1E"

NORMAL_BUTTON = "#444444"
NORMAL_BUTTON_HOVER = "#555555"

TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#BDBDBD"


# ================= QUESTION BANK =================

QUESTION_BANK = [

    # ================= HR QUESTIONS =================

    {
        "type": "HR",
        "difficulty": "Easy",
        "question": "Tell me about yourself.",
        "keywords": [
            "name",
            "education",
            "college",
            "degree",
            "skill",
            "project"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Easy",
        "question": "Why should we hire you?",
        "keywords": [
            "skill",
            "learning",
            "team",
            "project",
            "problem",
            "contribute"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Easy",
        "question": "What are your strengths?",
        "keywords": [
            "hardworking",
            "learning",
            "communication",
            "team",
            "problem",
            "adapt"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Easy",
        "question": "What is your weakness?",
        "keywords": [
            "weakness",
            "improve",
            "learning",
            "practice",
            "work"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Medium",
        "question": "Where do you see yourself in five years?",
        "keywords": [
            "career",
            "growth",
            "skill",
            "experience",
            "responsibility",
            "company"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Medium",
        "question": "Why do you want to join our company?",
        "keywords": [
            "company",
            "growth",
            "learning",
            "culture",
            "opportunity",
            "contribute"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Medium",
        "question": "How do you handle pressure?",
        "keywords": [
            "pressure",
            "priority",
            "planning",
            "calm",
            "deadline",
            "solution"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Medium",
        "question": "How do you handle failure?",
        "keywords": [
            "failure",
            "learn",
            "mistake",
            "improve",
            "experience",
            "try"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Hard",
        "question": "Tell me about a time when you solved a difficult problem.",
        "keywords": [
            "problem",
            "situation",
            "solution",
            "action",
            "result",
            "learn"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Hard",
        "question": "How would you handle a disagreement with a team member?",
        "keywords": [
            "listen",
            "communication",
            "team",
            "discuss",
            "solution",
            "respect"
        ]
    },


    # ================= TECHNICAL QUESTIONS =================

    {
        "type": "Technical",
        "difficulty": "Easy",
        "question": "What is Python?",
        "keywords": [
            "programming",
            "language",
            "high-level",
            "interpreted",
            "object-oriented"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Easy",
        "question": "What is the difference between a list and a tuple in Python?",
        "keywords": [
            "list",
            "tuple",
            "mutable",
            "immutable",
            "change"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Easy",
        "question": "What is SQL?",
        "keywords": [
            "sql",
            "database",
            "query",
            "data",
            "structured"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Easy",
        "question": "What is a primary key?",
        "keywords": [
            "primary",
            "key",
            "unique",
            "record",
            "table"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Easy",
        "question": "What is OOP?",
        "keywords": [
            "object",
            "oriented",
            "class",
            "object",
            "inheritance",
            "encapsulation"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Medium",
        "question": "Explain inheritance in object-oriented programming.",
        "keywords": [
            "inheritance",
            "class",
            "parent",
            "child",
            "properties",
            "methods"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Medium",
        "question": "What is normalization in DBMS?",
        "keywords": [
            "normalization",
            "database",
            "redundancy",
            "data",
            "tables",
            "dependency"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Medium",
        "question": "What is the difference between stack and queue?",
        "keywords": [
            "stack",
            "queue",
            "lifo",
            "fifo",
            "data",
            "structure"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Medium",
        "question": "What is an API?",
        "keywords": [
            "api",
            "application",
            "interface",
            "communication",
            "software",
            "request"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Hard",
        "question": "What is the difference between supervised and unsupervised learning?",
        "keywords": [
            "supervised",
            "unsupervised",
            "label",
            "data",
            "training",
            "clustering"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Hard",
        "question": "What is overfitting in machine learning?",
        "keywords": [
            "overfitting",
            "training",
            "data",
            "model",
            "generalization",
            "test"
        ]
    },

    {
        "type": "Technical",
        "difficulty": "Hard",
        "question": "Explain time complexity.",
        "keywords": [
            "time",
            "complexity",
            "algorithm",
            "input",
            "big",
            "o"
        ]
    },


    # ================= PROJECT QUESTIONS =================

    {
        "type": "Project",
        "difficulty": "Easy",
        "question": "Tell me about your project.",
        "keywords": [
            "project",
            "purpose",
            "technology",
            "feature",
            "result"
        ]
    },

    {
        "type": "Project",
        "difficulty": "Easy",
        "question": "Which technologies did you use in your project?",
        "keywords": [
            "python",
            "technology",
            "database",
            "html",
            "css",
            "framework"
        ]
    },

    {
        "type": "Project",
        "difficulty": "Medium",
        "question": "Why did you choose this project?",
        "keywords": [
            "problem",
            "interest",
            "solution",
            "learning",
            "purpose"
        ]
    },

    {
        "type": "Project",
        "difficulty": "Medium",
        "question": "What challenges did you face during the project?",
        "keywords": [
            "challenge",
            "problem",
            "error",
            "debug",
            "solution",
            "learn"
        ]
    },

    {
        "type": "Project",
        "difficulty": "Medium",
        "question": "How did you test your project?",
        "keywords": [
            "testing",
            "test",
            "error",
            "output",
            "validation",
            "result"
        ]
    },

    {
        "type": "Project",
        "difficulty": "Hard",
        "question": "If you had more time, what would you improve in your project?",
        "keywords": [
            "improve",
            "feature",
            "security",
            "performance",
            "database",
            "user"
        ]
    },

    {
        "type": "Project",
        "difficulty": "Hard",
        "question": "How would you make your project scalable?",
        "keywords": [
            "scalable",
            "performance",
            "database",
            "server",
            "users",
            "architecture"
        ]
    },


    # ================= SITUATION QUESTIONS =================

    {
        "type": "HR",
        "difficulty": "Medium",
        "question": "What would you do if you had a tight project deadline?",
        "keywords": [
            "priority",
            "planning",
            "deadline",
            "team",
            "task",
            "communication"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Medium",
        "question": "What would you do if you made a mistake in a project?",
        "keywords": [
            "mistake",
            "accept",
            "debug",
            "fix",
            "learn",
            "prevent"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Hard",
        "question": "How would you handle a situation where your manager disagrees with your approach?",
        "keywords": [
            "listen",
            "explain",
            "discussion",
            "feedback",
            "respect",
            "solution"
        ]
    },

    {
        "type": "HR",
        "difficulty": "Hard",
        "question": "What would you do if a team member was not completing their task?",
        "keywords": [
            "team",
            "communicate",
            "discuss",
            "help",
            "deadline",
            "manager"
        ]
    }
]


# ================= NORMALIZE TEXT =================

def normalize_text(text):

    return (
        text
        .lower()
        .replace(",", " ")
        .replace(".", " ")
        .replace("?", " ")
        .replace("!", " ")
        .replace(":", " ")
        .replace(";", " ")
    )


# ================= ANSWER ANALYSIS =================

def analyze_answer(question_data, answer):

    clean_answer = normalize_text(
        answer
    )

    words = clean_answer.split()

    word_count = len(
        words
    )

    # ================= KEYWORD MATCHING =================

    matched_keywords = []

    for keyword in question_data["keywords"]:

        if keyword.lower() in clean_answer:

            matched_keywords.append(
                keyword
            )

    keyword_count = len(
        matched_keywords
    )

    total_keywords = len(
        question_data["keywords"]
    )

    # ================= RELEVANCE SCORE =================

    if total_keywords > 0:

        relevance = int(
            (keyword_count / total_keywords) * 10
        )

    else:

        relevance = 5

    relevance = min(
        relevance,
        10
    )

    # ================= COMPLETENESS =================

    if word_count >= 80:

        completeness = 10

    elif word_count >= 50:

        completeness = 9

    elif word_count >= 35:

        completeness = 8

    elif word_count >= 20:

        completeness = 7

    elif word_count >= 10:

        completeness = 5

    elif word_count >= 5:

        completeness = 3

    else:

        completeness = 1

    # ================= COMMUNICATION =================

    communication_words = [
        "because",
        "therefore",
        "however",
        "also",
        "first",
        "then",
        "finally",
        "for example",
        "experience",
        "result"
    ]

    communication_count = 0

    for word in communication_words:

        if word in clean_answer:

            communication_count += 1

    if word_count >= 25 and communication_count >= 2:

        communication = 9

    elif word_count >= 15:

        communication = 7

    elif word_count >= 8:

        communication = 5

    else:

        communication = 3

    # ================= OVERALL SCORE =================

    overall = round(
        (
            relevance
            + completeness
            + communication
        ) / 3,
        1
    )

    # ================= GOOD POINTS =================

    good_points = []

    if word_count >= 20:

        good_points.append(
            "Your answer has reasonable detail."
        )

    if keyword_count >= 2:

        good_points.append(
            "Your answer covers important concepts."
        )

    if communication_count >= 1:

        good_points.append(
            "Your answer has a structured communication style."
        )

    if overall >= 7:

        good_points.append(
            "The answer is generally suitable for an interview."
        )

    if not good_points:

        good_points.append(
            "You attempted the question."
        )

    # ================= IMPROVEMENT POINTS =================

    improvements = []

    if word_count < 10:

        improvements.append(
            "Your answer is too short. Add more explanation."
        )

    elif word_count < 20:

        improvements.append(
            "Try to explain your answer in more detail."
        )

    if keyword_count == 0:

        improvements.append(
            "Your answer does not clearly address the main concepts."
        )

    elif keyword_count < 2:

        improvements.append(
            "Include more important points related to the question."
        )

    if communication < 6:

        improvements.append(
            "Use a clearer structure and explain your points step by step."
        )

    if not improvements:

        improvements.append(
            "You can make the answer more specific by adding an example."
        )

    # ================= BETTER ANSWER =================

    better_answer = create_better_answer(
        question_data,
        answer
    )

    return {
        "relevance": relevance,
        "completeness": completeness,
        "communication": communication,
        "overall": overall,
        "good_points": good_points,
        "improvements": improvements,
        "better_answer": better_answer
    }


# ================= BETTER ANSWER GENERATOR =================

def create_better_answer(
    question_data,
    answer
):

    question_type = question_data["type"]

    question = question_data["question"]

    if question_type == "HR":

        return (
            "A better answer should be structured in this order:\n\n"
            "1. Give a short introduction.\n"
            "2. Mention your education or background.\n"
            "3. Mention relevant technical skills.\n"
            "4. Give a project or practical example.\n"
            "5. End with your career goal or how you can contribute.\n\n"
            f"For this question — \"{question}\" — "
            "try to give a specific answer instead of a very general statement."
        )

    if question_type == "Technical":

        return (
            "A strong technical answer should follow this structure:\n\n"
            "1. Start with a simple definition.\n"
            "2. Explain how it works.\n"
            "3. Mention an example.\n"
            "4. If relevant, mention advantages, limitations or use cases.\n\n"
            "Avoid giving only one-line definitions."
        )

    if question_type == "Project":

        return (
            "A strong project answer should include:\n\n"
            "1. Project name and purpose.\n"
            "2. Problem the project solves.\n"
            "3. Technologies used.\n"
            "4. Your personal contribution.\n"
            "5. Challenges and how you solved them.\n"
            "6. Final result or future improvements."
        )

    return (
        "Try to answer using the STAR structure:\n\n"
        "Situation → Task → Action → Result\n\n"
        "This makes your interview answer clearer and more professional."
    )


# ================= MOCK INTERVIEW =================

def mock_interview(profile=None):

    # ================= CREATE WINDOW =================

    window = ctk.CTkToplevel()

    window.title(
        "Mock Interview"
    )

    # Full-screen

    window.state(
        "zoomed"
    )

    window.resizable(
        True,
        True
    )

    # ================= MAIN FRAME =================

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
        text="🎤 MOCK INTERVIEW",
        font=("Arial", 32, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 8)
    )

    ctk.CTkLabel(
        header,
        text="Practice your interview answers and improve your performance",
        font=("Arial", 17),
        text_color=TEXT_WHITE
    ).pack(
        pady=(0, 25)
    )

    # ================= SETUP FRAME =================

    setup_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    setup_frame.pack(
        fill="x",
        pady=10
    )

    ctk.CTkLabel(
        setup_frame,
        text="⚙️ Interview Settings",
        font=("Arial", 26, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )

    # ================= INTERVIEW TYPE =================

    ctk.CTkLabel(
        setup_frame,
        text="🎯 Interview Type",
        font=("Arial", 18, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 8)
    )

    type_box = ctk.CTkComboBox(
        setup_frame,
        values=[
            "Mixed",
            "HR",
            "Technical",
            "Project"
        ],
        width=400,
        height=45,
        font=("Arial", 17)
    )

    type_box.set(
        "Mixed"
    )

    type_box.pack(
        anchor="w",
        padx=30,
        pady=(0, 20)
    )

    # ================= DIFFICULTY =================

    ctk.CTkLabel(
        setup_frame,
        text="🎚️ Difficulty",
        font=("Arial", 18, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 8)
    )

    difficulty_box = ctk.CTkComboBox(
        setup_frame,
        values=[
            "Mixed",
            "Easy",
            "Medium",
            "Hard"
        ],
        width=400,
        height=45,
        font=("Arial", 17)
    )

    difficulty_box.set(
        "Mixed"
    )

    difficulty_box.pack(
        anchor="w",
        padx=30,
        pady=(0, 20)
    )

    # ================= QUESTION COUNT =================

    ctk.CTkLabel(
        setup_frame,
        text="🔢 Number of Questions",
        font=("Arial", 18, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 8)
    )

    count_box = ctk.CTkComboBox(
        setup_frame,
        values=[
            "5",
            "10",
            "15"
        ],
        width=400,
        height=45,
        font=("Arial", 17)
    )

    count_box.set(
        "5"
    )

    count_box.pack(
        anchor="w",
        padx=30,
        pady=(0, 25)
    )

    # ================= START BUTTON =================

    interview_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    # Do not pack initially

    # ================= PROGRESS =================

    progress_label = ctk.CTkLabel(
        interview_frame,
        text="",
        font=("Arial", 18, "bold"),
        text_color=TEXT_GRAY
    )

    progress_label.pack(
        pady=(25, 15)
    )

    # ================= QUESTION =================

    question_label = ctk.CTkLabel(
        interview_frame,
        text="",
        font=("Arial", 24, "bold"),
        wraplength=1100,
        justify="left"
    )

    question_label.pack(
        fill="x",
        padx=50,
        pady=(10, 25)
    )

    # ================= ANSWER LABEL =================

    ctk.CTkLabel(
        interview_frame,
        text="✍️ Your Answer",
        font=("Arial", 20, "bold")
    ).pack(
        anchor="w",
        padx=50,
        pady=(10, 10)
    )

    # ================= ANSWER BOX =================

    answer_box = ctk.CTkTextbox(
        interview_frame,
        height=220,
        font=("Arial", 17)
    )

    answer_box.pack(
        fill="x",
        padx=50,
        pady=(0, 15)
    )

    # ================= SUBMIT BUTTON =================
    
   # Submit Answer button ko directly submit_answer()
   # function se connect kiya jayega.

    submit_button = ctk.CTkButton(
        interview_frame,
        text="🔍 Submit Answer",
        width=250,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=lambda: submit_answer()
)

    submit_button.pack(
        pady=15
)

    # ================= FEEDBACK FRAME =================

    feedback_frame = ctk.CTkFrame(
        interview_frame,
        corner_radius=12
    )

    # ================= SCORE =================

    score_label = ctk.CTkLabel(
        feedback_frame,
        text="",
        font=("Arial", 25, "bold"),
        text_color=GREEN
    )

    score_label.pack(
        pady=(20, 15)
    )

    # ================= FEEDBACK BOX =================

    feedback_box = ctk.CTkTextbox(
        feedback_frame,
        height=400,
        font=("Arial", 16)
    )

    feedback_box.pack(
        fill="x",
        padx=25,
        pady=(0, 20)
    )

    # ================= NEXT BUTTON =================

    next_button = ctk.CTkButton(
        feedback_frame,
        text="Next Question →",
        width=250,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER
    )

    next_button.pack(
        pady=(0, 25)
    )

    # ================= RESULT FRAME =================

    result_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    # Do not pack initially

    ctk.CTkLabel(
        result_frame,
        text="🏆 INTERVIEW RESULT",
        font=("Arial", 30, "bold")
    ).pack(
        pady=(30, 15)
    )

    final_score_label = ctk.CTkLabel(
        result_frame,
        text="",
        font=("Arial", 42, "bold"),
        text_color=GREEN
    )

    final_score_label.pack(
        pady=10
    )

    final_message = ctk.CTkLabel(
        result_frame,
        text="",
        font=("Arial", 22, "bold"),
        wraplength=900
    )

    final_message.pack(
        pady=20
    )

    # ================= TRY AGAIN =================

    try_again_button = ctk.CTkButton(
        result_frame,
        text="🔄 Try Again",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER
    )

    try_again_button.pack(
        pady=10
    )

    # ================= CLOSE =================

    ctk.CTkButton(
        result_frame,
        text="❌ Close",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color=RED_HOVER,
        command=window.destroy
    ).pack(
        pady=(0, 30)
    )

    # ================= INTERVIEW STATE =================

    questions = []

    current_index = 0

    total_score = 0

    answered_count = 0

    # ================= PREPARE QUESTIONS =================

    def prepare_questions():

        nonlocal questions

        interview_type = type_box.get()

        difficulty = difficulty_box.get()

        amount = int(
            count_box.get()
        )

        available = []

        for item in QUESTION_BANK:

            type_match = (
                interview_type == "Mixed"
                or item["type"] == interview_type
            )

            difficulty_match = (
                difficulty == "Mixed"
                or item["difficulty"] == difficulty
            )

            if type_match and difficulty_match:

                available.append(
                    item
                )

        random.shuffle(
            available
        )

        questions = available[
            :min(
                amount,
                len(available)
            )
        ]

        return len(
            questions
        )

    # ================= SHOW QUESTION =================

    def show_question():

        # Hide feedback

        feedback_frame.pack_forget()

        # Clear answer

        answer_box.delete(
            "1.0",
            "end"
        )

        # Get current question

        item = questions[
            current_index
        ]

        progress_label.configure(
            text=(
                f"Question {current_index + 1} "
                f"/ {len(questions)}"
            )
        )

        question_label.configure(
            text=(
                f"{item['type']} • "
                f"{item['difficulty']}\n\n"
                f"{item['question']}"
            )
        )

        submit_button.configure(
            state="normal"
        )

    # ================= SUBMIT ANSWER =================

    def submit_answer():

        nonlocal total_score

        nonlocal answered_count

        answer = answer_box.get(
            "1.0",
            "end"
        ).strip()

        if not answer:

            messagebox.showwarning(
                "Answer Required",
                "Please write your answer before submitting."
            )

            return

        # Analyze answer

        analysis = analyze_answer(
            questions[current_index],
            answer
        )

        # Add score

        total_score += analysis[
            "overall"
        ]

        answered_count += 1

        # Disable submit

        submit_button.configure(
            state="disabled"
        )

        # ================= SCORE =================

        score_label.configure(
            text=(
                f"⭐ Overall Score: "
                f"{analysis['overall']} / 10"
            )
        )

        # ================= BUILD FEEDBACK =================

        feedback = (
            "✅ GOOD POINTS\n\n"
        )

        for point in analysis[
            "good_points"
        ]:

            feedback += (
                f"• {point}\n"
            )

        feedback += (
            "\n\n⚠️ NEEDS IMPROVEMENT\n\n"
        )

        for point in analysis[
            "improvements"
        ]:

            feedback += (
                f"• {point}\n"
            )

        feedback += (
            "\n\n📊 SCORE BREAKDOWN\n\n"
            f"Relevance      : "
            f"{analysis['relevance']}/10\n"
            f"Completeness   : "
            f"{analysis['completeness']}/10\n"
            f"Communication  : "
            f"{analysis['communication']}/10\n"
        )

        feedback += (
            "\n\n💡 BETTER WAY TO ANSWER\n\n"
            f"{analysis['better_answer']}"
        )

        feedback_box.configure(
            state="normal"
        )

        feedback_box.delete(
            "1.0",
            "end"
        )

        feedback_box.insert(
            "1.0",
            feedback
        )

        feedback_box.configure(
            state="disabled"
        )

        feedback_frame.pack(
            fill="x",
            padx=30,
            pady=25
        )

        # Last question

        if current_index == len(
            questions
        ) - 1:

            next_button.configure(
                text="🏆 Finish Interview"
            )

        else:

            next_button.configure(
                text="Next Question →"
            )     

    # ================= NEXT QUESTION =================

    def next_question():

        nonlocal current_index

        if current_index == len(
            questions
        ) - 1:

            show_final_result()

            return

        current_index += 1

        show_question()

    next_button.configure(
        command=next_question
    )

    # ================= FINAL RESULT =================

    def show_final_result():

        interview_frame.pack_forget()

        result_frame.pack(
            fill="x",
            pady=30
        )

        if answered_count > 0:

            average = round(
                total_score / answered_count,
                1
            )

        else:

            average = 0

        final_score_label.configure(
            text=f"{average} / 10"
        )

        if average >= 8:

            final_message.configure(
                text=(
                    "🎉 Excellent Interview Performance!\n\n"
                    "Your answers show good preparation. "
                    "Keep practicing real interview questions."
                ),
                text_color=GREEN
            )

        elif average >= 6:

            final_message.configure(
                text=(
                    "👍 Good Performance!\n\n"
                    "You have a good base, but some answers "
                    "need more detail and structure."
                ),
                text_color=YELLOW
            )

        else:

            final_message.configure(
                text=(
                    "📚 More Practice Needed\n\n"
                    "Work on answer structure, technical "
                    "knowledge and communication."
                ),
                text_color=RED
            )

    # ================= START INTERVIEW =================

    def start_interview():

        nonlocal current_index

        nonlocal total_score

        nonlocal answered_count

        question_count = prepare_questions()

        if question_count == 0:

            messagebox.showerror(
                "No Questions",
                "No questions are available for the selected settings."
            )

            return

        current_index = 0

        total_score = 0

        answered_count = 0

        setup_frame.pack_forget()

        result_frame.pack_forget()

        interview_frame.pack(
            fill="x",
            pady=30
        )

        show_question()

    # ================= START BUTTON =================

    ctk.CTkButton(
        setup_frame,
        text="🎤 Start Mock Interview",
        width=300,
        height=55,
        font=("Arial", 19, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=start_interview
    ).pack(
        pady=(5, 30)
    )

    # ================= TRY AGAIN =================

    def try_again():

        window.destroy()

        mock_interview(
            profile
        )

    try_again_button.configure(
        command=try_again
    )

    # ================= BOTTOM CLOSE BUTTON =================

    ctk.CTkButton(
        main,
        text="❌ Close",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color=RED_HOVER,
        command=window.destroy
    ).pack(
        pady=(5, 35)
    )