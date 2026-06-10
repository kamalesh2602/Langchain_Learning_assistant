from agents.explainer import explain_topic
from agents.quiz import generate_quiz
from agents.evaluator import evaluate_answer
from state import LearningState

state = LearningState()

topic = input("Enter Topic: ")
state.current_topic = topic

explanation = explain_topic(
    state.current_topic
)

print("\n=== EXPLANATION ===")
print(explanation)


quiz = generate_quiz(
    state.current_topic
)
state.current_question = quiz.question

print("\n=== QUIZ ===")
print(quiz.question)

answer = input("\nYour Answer: ")

result = evaluate_answer(
    state.current_question,
    answer
)

state.current_score += result.score

print("\n=== RESULT ===")
print("Score:", result.score)
print("Feedback:", result.feedback)
print("Improvement:", result.improvement_area)


print("\n--- STATE ---")

print(state.current_topic)
print(state.current_question)
print(state.current_score)
