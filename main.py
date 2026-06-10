from agents.explainer import explain_topic
from agents.quiz import generate_quiz

result = explain_topic("Python Integers")
print(result)

quiz = generate_quiz("Python Lists")

print(quiz)
print(quiz.question)
print(quiz.answer)