from agents.explainer import explain_topic
from agents.quiz import generate_quiz
from agents.evaluator import evaluate_answer
from state import LearningState

state = LearningState()

topic = input("Enter Topic: ")
state.current_topic = topic
num_questions = int(input("How many questions required for your quiz?: "))

explanation = explain_topic(
    state.current_topic
)

print("\n=== EXPLANATION ===")
print(explanation)


for i in range(num_questions):

    print(f"\n=== QUESTION {i+1} ===")

    quiz = generate_quiz(
        state.current_topic
    )

    state.current_question = quiz.question

    print(quiz.question)

    answer = input(
        "\nYour Answer: "
    )

    result = evaluate_answer(
        state.current_question,
        answer
    )

    state.current_score += result.score

    print("\nScore:", result.score)

    print("Feedback:")
    print(result.feedback)
    state.quiz_history.append(
    {
        "topic": state.current_topic,
        "question": state.current_question,
        "score": result.score
    }
)

print("\n=== FINAL SCORE ===")
print(f"{state.current_score}")
print("Improvement:", result.improvement_area)



print("\n--- STATE ---")

print(state.current_topic)
print(state.current_question)
print(state.current_score)

print("\n=== HISTORY ===")

for item in state.quiz_history:
    print(item)