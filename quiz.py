import customtkinter as ctk

import json

import html

import random

from urllib.request import urlopen

from urllib.parse import urlencode


# ================= APPEARANCE =================

ctk.set_appearance_mode("Dark")

ctk.set_default_color_theme("blue")


# ================= COLOR SETTINGS =================

BLUE = "#1F6AA5"

BLUE_HOVER = "#15527F"

GREEN = "#2E8B57"

GREEN_HOVER = "#246B45"

RED = "#C0392B"

RED_HOVER = "#962D22"

DARK_CARD = "#1E1E1E"

NORMAL_BUTTON = "#444444"

NORMAL_BUTTON_HOVER = "#555555"

TEXT_WHITE = "#FFFFFF"

TEXT_GRAY = "#BDBDBD"


# ================= ONLINE QUIZ SETTINGS =================

API_URL = "https://opentdb.com/api.php"

COMPUTER_CATEGORY = 18


# ================= FALLBACK QUESTIONS =================
# These questions are used only when internet/API is unavailable.

FALLBACK_QUESTIONS = [

    {
        "question": "Python kis type ki language hai?",
        "correct_answer": "Programming Language",
        "incorrect_answers": [
            "Database",
            "Browser",
            "Operating System"
        ]
    },

    {
        "question": "Python file extension kya hoti hai?",
        "correct_answer": ".py",
        "incorrect_answers": [
            ".java",
            ".cpp",
            ".html"
        ]
    },

    {
        "question": "SQL ka full form kya hai?",
        "correct_answer": "Structured Query Language",
        "incorrect_answers": [
            "Simple Query Language",
            "System Query Language",
            "Sequential Query Language"
        ]
    },

    {
        "question": "HTML ka full form kya hai?",
        "correct_answer": "HyperText Markup Language",
        "incorrect_answers": [
            "HighText Machine Language",
            "HyperText Machine Language",
            "Hyper Tool Markup Language"
        ]
    },

    {
        "question": "CSS ka use kis liye hota hai?",
        "correct_answer": "Web page styling",
        "incorrect_answers": [
            "Database management",
            "Operating system",
            "Server installation"
        ]
    },

    {
        "question": "Which data structure follows FIFO?",
        "correct_answer": "Queue",
        "incorrect_answers": [
            "Stack",
            "Tree",
            "Graph"
        ]
    },

    {
        "question": "Which data structure follows LIFO?",
        "correct_answer": "Stack",
        "incorrect_answers": [
            "Queue",
            "Array",
            "Graph"
        ]
    },

    {
        "question": "SQL is mainly used for what?",
        "correct_answer": "Managing databases",
        "incorrect_answers": [
            "Designing images",
            "Playing videos",
            "Operating hardware"
        ]
    },

    {
        "question": "Which one is a Python data type?",
        "correct_answer": "List",
        "incorrect_answers": [
            "Website",
            "Browser",
            "Compiler"
        ]
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "correct_answer": "def",
        "incorrect_answers": [
            "function",
            "fun",
            "define"
        ]
    }
]


# ================= FETCH ONLINE QUESTIONS =================

def fetch_questions(amount, difficulty):

    # ================= CREATE API PARAMETERS =================

    params = {
        "amount": amount,
        "category": COMPUTER_CATEGORY,
        "type": "multiple"
    }

    # Add difficulty only when user selects
    # Easy, Medium or Hard.

    if difficulty != "Mixed":

        params["difficulty"] = difficulty.lower()

    # Create complete URL

    url = API_URL + "?" + urlencode(params)

    try:

        # Open online API

        response = urlopen(
            url,
            timeout=10
        )

        # Read API response

        data = response.read().decode(
            "utf-8"
        )

        # Convert JSON into Python dictionary

        data = json.loads(data)

        # ================= CHECK API RESPONSE =================

        if data.get("response_code") == 0:

            questions = []

            for item in data["results"]:

                # Decode HTML entities

                question = html.unescape(
                    item["question"]
                )

                correct = html.unescape(
                    item["correct_answer"]
                )

                incorrect = [
                    html.unescape(answer)
                    for answer in item["incorrect_answers"]
                ]

                # Create options

                options = incorrect + [correct]

                # Randomize options

                random.shuffle(options)

                questions.append(
                    {
                        "question": question,
                        "options": options,
                        "correct_answer": correct
                    }
                )

            return questions

        # ================= API NO RESULTS =================

        return []

    except Exception:

        # Internet/API error

        return []


# ================= PREPARE FALLBACK QUESTIONS =================

def get_fallback_questions(amount):

    questions = []

    selected = FALLBACK_QUESTIONS.copy()

    random.shuffle(
        selected
    )

    # Select requested amount,
    # but fallback contains limited questions.

    selected = selected[
        :min(amount, len(selected))
    ]

    for item in selected:

        options = item["incorrect_answers"].copy()

        options.append(
            item["correct_answer"]
        )

        random.shuffle(
            options
        )

        questions.append(
            {
                "question": item["question"],
                "options": options,
                "correct_answer": item["correct_answer"]
            }
        )

    return questions


# ================= START QUIZ =================

def start_quiz():

    # ================= CREATE WINDOW =================

    window = ctk.CTkToplevel()

    window.title(
        "Placement Quiz"
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

    # ================= QUIZ STATE =================

    quiz_questions = []

    current_question = 0

    score = 0

    selected_answer = ctk.StringVar(
        value=""
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
        text="🧠 PLACEMENT QUIZ",
        font=("Arial", 32, "bold"),
        text_color=TEXT_WHITE
    ).pack(
        pady=(25, 8)
    )

    ctk.CTkLabel(
        header,
        text="Test your Computer Science knowledge",
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
        text="⚙️ Quiz Settings",
        font=("Arial", 26, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )

    # ================= CATEGORY =================

    ctk.CTkLabel(
        setup_frame,
        text="📚 Subject",
        font=("Arial", 18, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 8)
    )

    category_box = ctk.CTkComboBox(
        setup_frame,
        values=[
            "Computer Science"
        ],
        width=400,
        height=45,
        font=("Arial", 17)
    )

    category_box.set(
        "Computer Science"
    )

    category_box.pack(
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

    # ================= NUMBER OF QUESTIONS =================

    ctk.CTkLabel(
        setup_frame,
        text="🔢 Number of Questions",
        font=("Arial", 18, "bold")
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 8)
    )

    question_count_box = ctk.CTkComboBox(
        setup_frame,
        values=[
            "10",
            "20",
            "30",
            "40",
            "50"
        ],
        width=400,
        height=45,
        font=("Arial", 17)
    )

    question_count_box.set(
        "10"
    )

    question_count_box.pack(
        anchor="w",
        padx=30,
        pady=(0, 25)
    )

    # ================= STATUS LABEL =================

    status_label = ctk.CTkLabel(
        setup_frame,
        text="",
        font=("Arial", 16),
        text_color=TEXT_GRAY
    )

    status_label.pack(
        pady=(0, 10)
    )

    # ================= QUIZ FRAME =================

    quiz_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    # Do not pack initially

    # ================= PROGRESS LABEL =================

    progress_label = ctk.CTkLabel(
        quiz_frame,
        text="",
        font=("Arial", 18, "bold"),
        text_color=TEXT_GRAY
    )

    progress_label.pack(
        pady=(25, 15)
    )

    # ================= QUESTION LABEL =================

    question_label = ctk.CTkLabel(
        quiz_frame,
        text="",
        font=("Arial", 23, "bold"),
        wraplength=1100,
        justify="left"
    )

    question_label.pack(
        fill="x",
        padx=50,
        pady=(10, 30)
    )

    # ================= OPTIONS FRAME =================

    options_frame = ctk.CTkFrame(
        quiz_frame,
        fg_color="transparent"
    )

    options_frame.pack(
        fill="x",
        padx=50
    )

    # ================= NEXT BUTTON =================

    next_button = ctk.CTkButton(
        quiz_frame,
        text="Next Question →",
        width=250,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER
    )

    next_button.pack(
        pady=30
    )

    # ================= RESULT FRAME =================

    result_frame = ctk.CTkFrame(
        main,
        corner_radius=15
    )

    # Do not pack initially

    # ================= RESULT TITLE =================

    result_title = ctk.CTkLabel(
        result_frame,
        text="🏆 QUIZ RESULT",
        font=("Arial", 30, "bold")
    )

    result_title.pack(
        pady=(30, 15)
    )

    # ================= SCORE LABEL =================

    score_label = ctk.CTkLabel(
        result_frame,
        text="",
        font=("Arial", 42, "bold"),
        text_color=GREEN
    )

    score_label.pack(
        pady=10
    )

    # ================= RESULT MESSAGE =================

    result_message = ctk.CTkLabel(
        result_frame,
        text="",
        font=("Arial", 24, "bold"),
        wraplength=900
    )

    result_message.pack(
        pady=15
    )

    # ================= TRY AGAIN BUTTON =================

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
        pady=15
    )

    # ================= CLOSE BUTTON =================

    close_button = ctk.CTkButton(
        result_frame,
        text="❌ Close",
        width=220,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=RED,
        hover_color=RED_HOVER,
        command=window.destroy
    )

    close_button.pack(
        pady=(0, 30)
    )

    # ================= SHOW RESULT =================

    def show_result():

        # Hide quiz

        quiz_frame.pack_forget()

        # Show result

        result_frame.pack(
            fill="x",
            pady=30
        )

        # Calculate percentage

        total = len(
            quiz_questions
        )

        percentage = int(
            (score / total) * 100
        )

        score_label.configure(
            text=f"{score} / {total}  ({percentage}%)"
        )

        # ================= PERFORMANCE =================

        if percentage >= 80:

            message = (
                "🎉 Excellent Performance!\n\n"
                "You have a strong understanding "
                "of the concepts."
            )

            result_message.configure(
                text_color=GREEN
            )

        elif percentage >= 60:

            message = (
                "👍 Good Job!\n\n"
                "Keep practicing to improve "
                "your score."
            )

            result_message.configure(
                text_color=GREEN
            )

        else:

            message = (
                "📚 Keep Practicing!\n\n"
                "Revise the concepts and try "
                "the quiz again."
            )

            result_message.configure(
                text_color=RED
            )

        result_message.configure(
            text=message
        )

    # ================= SHOW QUESTION =================

    def show_question():

        # Clear previous selection

        selected_answer.set(
            ""
        )

        # Remove old option buttons

        for widget in options_frame.winfo_children():

            widget.destroy()

        # Current question

        question = quiz_questions[
            current_question
        ]

        # Update progress

        progress_label.configure(
            text=(
                f"Question {current_question + 1} "
                f"/ {len(quiz_questions)}"
            )
        )

        # Update question

        question_label.configure(
            text=question["question"]
        )

        # ================= CREATE OPTIONS =================

        for option in question["options"]:

            option_button = ctk.CTkButton(
                options_frame,
                text=option,
                width=900,
                height=55,
                font=("Arial", 17),
                fg_color=NORMAL_BUTTON,
                hover_color=NORMAL_BUTTON_HOVER,
                anchor="w",
                command=lambda answer=option:
                select_answer(answer)
            )

            option_button.pack(
                fill="x",
                pady=7
            )

        # Last question button text

        if current_question == len(quiz_questions) - 1:

            next_button.configure(
                text="🏆 Finish Quiz"
            )

        else:

            next_button.configure(
                text="Next Question →"
            )

    # ================= SELECT ANSWER =================

    def select_answer(answer):

        selected_answer.set(
            answer
        )

        # Update all buttons

        for widget in options_frame.winfo_children():

            if widget.cget("text") == answer:

                widget.configure(
                    fg_color=GREEN,
                    hover_color=GREEN_HOVER
                )

            else:

                widget.configure(
                    fg_color=NORMAL_BUTTON,
                    hover_color=NORMAL_BUTTON_HOVER
                )

    # ================= NEXT QUESTION =================

    def next_question():

        nonlocal current_question

        nonlocal score

        # Check if answer selected

        if selected_answer.get() == "":

            status_label.configure(
                text="⚠️ Please select an answer first.",
                text_color=RED
            )

            return

        # Remove warning

        status_label.configure(
            text=""
        )

        # Get current question

        question = quiz_questions[
            current_question
        ]

        # Check answer

        if selected_answer.get() == question[
            "correct_answer"
        ]:

            score += 1

        # Last question

        if current_question == len(
            quiz_questions
        ) - 1:

            show_result()

            return

        # Move to next question

        current_question += 1

        show_question()

    # Connect next button

    next_button.configure(
        command=next_question
    )

    # ================= START QUIZ =================

    def generate_quiz():

        nonlocal quiz_questions

        nonlocal current_question

        nonlocal score

        # ================= READ SETTINGS =================

        difficulty = difficulty_box.get()

        amount = int(
            question_count_box.get()
        )

        # ================= STATUS =================

        status_label.configure(
            text="🌐 Fetching questions from internet...",
            text_color=TEXT_GRAY
        )

        window.update()

        # ================= FETCH ONLINE QUESTIONS =================

        questions = fetch_questions(
            amount,
            difficulty
        )

        # ================= FALLBACK =================

        if not questions:

            status_label.configure(
                text=(
                    "⚠️ Online questions unavailable. "
                    "Using local questions."
                ),
                text_color=RED
            )

            questions = get_fallback_questions(
                amount
            )

        else:

            status_label.configure(
                text=(
                    f"✅ {len(questions)} questions loaded successfully."
                ),
                text_color=GREEN
            )

        # If still no questions

        if not questions:

            status_label.configure(
                text="❌ Could not load questions.",
                text_color=RED
            )

            return

        # ================= RESET QUIZ =================

        quiz_questions = questions

        current_question = 0

        score = 0

        # Hide setup

        setup_frame.pack_forget()

        # Hide result if visible

        result_frame.pack_forget()

        # Show quiz

        quiz_frame.pack(
            fill="x",
            pady=30
        )

        # Show first question

        show_question()

    # ================= GENERATE BUTTON =================

    ctk.CTkButton(
        setup_frame,
        text="🚀 Generate Quiz",
        width=300,
        height=55,
        font=("Arial", 19, "bold"),
        fg_color=BLUE,
        hover_color=BLUE_HOVER,
        command=generate_quiz
    ).pack(
        pady=(5, 30)
    )

    # ================= TRY AGAIN =================

    def try_again():

        window.destroy()

        start_quiz()

    try_again_button.configure(
        command=try_again
    )

    # ================= CLOSE WINDOW =================

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