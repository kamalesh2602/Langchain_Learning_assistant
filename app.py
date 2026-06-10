import streamlit as st

from state import LearningState

from agents.explainer import explain_topic
from agents.quiz import generate_quiz
from agents.evaluator import evaluate_answer
from agents.planner import create_plan
from agents.progress import analyze_progress

if "state" not in st.session_state:
    st.session_state.state = LearningState()

state = st.session_state.state


st.sidebar.title("LangChain Learning Assistant")

page = st.sidebar.radio(
    "Choose",
    [
        "Explain",
        "Quiz",
        "Teach",
        "Progress"
    ]
)

if page == "Explain":

    topic = st.text_input(
        "Enter Topic"
    )

    if st.button("Explain"):

        state.current_topic = topic

        explanation = explain_topic(topic)

        st.subheader("Explanation")

        st.write(explanation)

elif page == "Quiz":

    topic = st.text_input(
        "Topic",
        value=state.current_topic or ""
    )

    if st.button("Generate Quiz"):

        # Clear old result
        st.session_state.pop(
            "quiz_result",
            None
        )

        state.current_topic = topic

        with st.spinner(
            "Generating quiz..."
        ):

            quiz = generate_quiz(topic)

        state.current_question = quiz.question

        st.session_state.quiz = quiz

    if "quiz" in st.session_state:

        st.subheader("Question")

        st.write(
            st.session_state.quiz.question
        )

        answer = st.text_area(
            "Your Answer",
            key="quiz_answer"
        )

        if st.button(
            "Submit Answer"
        ):

            with st.spinner(
                "Evaluating answer..."
            ):

                result = evaluate_answer(
                    st.session_state.quiz.question,
                    answer
                )

            state.current_score += result.score

            state.quiz_history.append(
                {
                    "topic": state.current_topic,
                    "question": st.session_state.quiz.question,
                    "score": result.score
                }
            )

            st.session_state.quiz_result = result

        # Persist result after reruns
        if "quiz_result" in st.session_state:

            st.success(
                f"Score: {st.session_state.quiz_result.score}"
            )

            st.write(
                st.session_state.quiz_result.feedback
            )


elif page == "Teach":

    topic = st.text_input(
        "Topic",
        value=state.current_topic or ""
    )

    if st.button("Generate Plan"):

        state.current_topic = topic

        with st.spinner("Creating learning plan..."):

            plan = create_plan(topic)

        st.session_state.plan = plan
        st.session_state.approved = False

    if "plan" in st.session_state:

        st.subheader("Learning Plan")

        st.write(
            st.session_state.plan
        )

        if st.button("Approve Plan"):

            st.session_state.approved = True

    if st.session_state.get(
        "approved",
        False
    ):

        if "teach_explanation" not in st.session_state:

            with st.spinner(
                "Preparing lesson..."
            ):

                explanation = explain_topic(
                    state.current_topic
                )

                quiz = generate_quiz(
                    state.current_topic
                )

            st.session_state.teach_explanation = explanation
            st.session_state.teach_quiz = quiz

        st.subheader("Explanation")

        st.write(
            st.session_state.teach_explanation
        )

        st.subheader("Quiz")

        st.write(
            st.session_state.teach_quiz.question
        )

        answer = st.text_area(
            "Your Answer",
            key="teach_answer"
        )

        if st.button(
            "Submit Teach Quiz"
        ):

            with st.spinner(
                "Evaluating answer..."
            ):

                result = evaluate_answer(
                    st.session_state.teach_quiz.question,
                    answer
                )

            state.current_score += result.score

            state.quiz_history.append(
                {
                    "topic": state.current_topic,
                    "question": st.session_state.teach_quiz.question,
                    "score": result.score
                }
            )

            st.success(
                f"Score: {result.score}"
            )

            st.write(result.feedback)

elif page == "Progress":

    result = analyze_progress(
        total_score=state.current_score,
        questions_attempted=len(
            state.quiz_history
        )
    )

    st.subheader("Progress")

    st.write(result)

    st.subheader("History")

    st.json(state.quiz_history)