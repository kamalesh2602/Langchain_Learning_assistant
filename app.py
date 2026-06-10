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


st.sidebar.title("Learning Assistant")

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

        quiz = generate_quiz(topic)

        state.current_topic = topic
        state.current_question = quiz.question

        st.session_state.quiz_generated = True
        if state.current_question:
            st.subheader("Question")
            st.write(state.current_question)
            answer = st.text_area("Your Answer")
            if st.button("Submit Answer"):

                result = evaluate_answer(state.current_question,answer)

                state.current_score += result.score

                state.quiz_history.append(
                    {
                        "topic": state.current_topic,
                        "question": state.current_question,
                        "score": result.score
                    }
                )
                st.success(f"Score: {result.score}")
                st.write(result.feedback)

elif page == "Teach":

    topic = st.text_input(
        "Topic"
    )

    if st.button("Teach Me"):

        state.current_topic = topic

        plan = create_plan(topic)

        st.subheader("Plan")

        st.write(plan)

        explanation = explain_topic(topic)

        st.subheader("Explanation")

        st.write(explanation)

        quiz = generate_quiz(topic)

        state.current_question = quiz.question

        st.subheader("Quiz")

        st.write(quiz.question)

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