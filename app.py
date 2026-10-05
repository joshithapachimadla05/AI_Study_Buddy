import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📚 AI Study Buddy")
st.write("Your simple personal study assistant")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📌 Menu")

page = st.sidebar.radio(
    "Choose a feature:",
    [
        "🏠 Dashboard",
        "📝 Study Notes",
        "❓ Quiz Generator",
        "🧠 Flashcards",
        "📅 Study Planner",
        "📊 Progress"
    ]
)

# -----------------------------
# DASHBOARD
# -----------------------------
if page == "🏠 Dashboard":

    st.header("Welcome to AI Study Buddy! 👋")

    st.write(
        "Use this app to organize your studies, "
        "practice quizzes, review flashcards and track your progress."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Subjects", "5")

    with col2:
        st.metric("Quizzes", "10")

    with col3:
        st.metric("Study Progress", "70%")

    st.subheader("✨ Features")

    st.write("📖 **Study Notes** – Create and review your notes")
    st.write("❓ **Quiz Generator** – Practice questions")
    st.write("🧠 **Flashcards** – Quick revision")
    st.write("📅 **Study Planner** – Plan your study schedule")
    st.write("📊 **Progress** – Check your study progress")


# -----------------------------
# STUDY NOTES
# -----------------------------
elif page == "📝 Study Notes":

    st.header("📝 Study Notes")

    subject = st.selectbox(
        "Select Subject",
        [
            "Python",
            "Java",
            "Data Structures",
            "DBMS",
            "Artificial Intelligence"
        ]
    )

    topic = st.text_input("Enter Topic")

    notes = st.text_area(
        "Write your notes here:",
        height=250
    )

    if st.button("💾 Save Notes"):

        if topic and notes:
            st.success(
                f"Notes for '{topic}' in {subject} saved successfully!"
            )
        else:
            st.warning("Please enter both topic and notes.")


# -----------------------------
# QUIZ GENERATOR
# -----------------------------
elif page == "❓ Quiz Generator":

    st.header("❓ Quiz Generator")

    subject = st.selectbox(
        "Choose Subject",
        [
            "Python",
            "Java",
            "Data Structures",
            "DBMS",
            "Artificial Intelligence"
        ]
    )

    st.write(f"Quiz for **{subject}**")

    questions = {
        "Python": {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "fun", "define"],
            "answer": "def"
        },

        "Java": {
            "question": "Which method is the starting point of a Java program?",
            "options": ["start()", "run()", "main()", "begin()"],
            "answer": "main()"
        },

        "Data Structures": {
            "question": "Which data structure follows LIFO?",
            "options": ["Queue", "Stack", "Array", "Tree"],
            "answer": "Stack"
        },

        "DBMS": {
            "question": "Which command is used to retrieve data from a database?",
            "options": ["GET", "SELECT", "FETCH", "READ"],
            "answer": "SELECT"
        },

        "Artificial Intelligence": {
            "question": "What does AI stand for?",
            "options": [
                "Automatic Information",
                "Artificial Intelligence",
                "Advanced Internet",
                "Artificial Internet"
            ],
            "answer": "Artificial Intelligence"
        }
    }

    q = questions[subject]

    st.subheader(q["question"])

    answer = st.radio(
        "Choose your answer:",
        q["options"]
    )

    if st.button("Check Answer"):

        if answer == q["answer"]:
            st.success("🎉 Correct Answer!")

        else:
            st.error(
                f"❌ Wrong Answer. Correct answer is: {q['answer']}"
            )


# -----------------------------
# FLASHCARDS
# -----------------------------
elif page == "🧠 Flashcards":

    st.header("🧠 Flashcards")

    flashcards = {
        "Python": {
            "question": "What is Python?",
            "answer": "Python is a high-level programming language."
        },

        "Java": {
            "question": "What is JVM?",
            "answer": "JVM stands for Java Virtual Machine."
        },

        "Data Structures": {
            "question": "What is a stack?",
            "answer": "A stack is a LIFO data structure."
        },

        "DBMS": {
            "question": "What is SQL?",
            "answer": "SQL is used to communicate with relational databases."
        },

        "Artificial Intelligence": {
            "question": "What is AI?",
            "answer": "AI is the simulation of human intelligence by machines."
        }
    }

    subject = st.selectbox(
        "Choose Flashcard",
        list(flashcards.keys())
    )

    card = flashcards[subject]

    st.info("❓ " + card["question"])

    if st.button("👀 Show Answer"):
        st.success("💡 " + card["answer"])


# -----------------------------
# STUDY PLANNER
# -----------------------------
elif page == "📅 Study Planner":

    st.header("📅 Study Planner")

    subject = st.text_input("Subject")

    hours = st.number_input(
        "Study Hours",
        min_value=1,
        max_value=12,
        value=2
    )

    date = st.date_input("Study Date")

    if st.button("➕ Add Study Plan"):

        if subject:
            st.success(
                f"Study plan created: {subject} | "
                f"{hours} hours | {date}"
            )
        else:
            st.warning("Please enter a subject.")


# -----------------------------
# PROGRESS
# -----------------------------
elif page == "📊 Progress":

    st.header("📊 Study Progress")

    python_progress = st.slider(
        "Python",
        0,
        100,
        70
    )

    java_progress = st.slider(
        "Java",
        0,
        100,
        60
    )

    dbms_progress = st.slider(
        "DBMS",
        0,
        100,
        80
    )

    ds_progress = st.slider(
        "Data Structures",
        0,
        100,
        65
    )

    st.subheader("Your Progress")

    st.progress(python_progress / 100)
    st.write(f"Python: {python_progress}%")

    st.progress(java_progress / 100)
    st.write(f"Java: {java_progress}%")

    st.progress(dbms_progress / 100)
    st.write(f"DBMS: {dbms_progress}%")

    st.progress(ds_progress / 100)
    st.write(f"Data Structures: {ds_progress}%")

    average = (
        python_progress
        + java_progress
        + dbms_progress
        + ds_progress
    ) / 4

    st.metric(
        "Overall Progress",
        f"{average:.1f}%"
    )

    st.success("Keep studying! 💪📚")