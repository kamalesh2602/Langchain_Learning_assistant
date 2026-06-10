from agents.explainer import explain_topic
from agents.quiz import generate_quiz
from agents.evaluator import evaluate_answer


result = explain_topic("Python Integers")
print(result)

quiz = generate_quiz("Python Lists")

print(quiz)
print(quiz.question)
print(quiz.answer)


result = evaluate_answer(
    "What is OOP?",
    "OOP is Object Oriented Programming"
)

print(result.score)
print(result.feedback)
print(result.improvement_area)