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

