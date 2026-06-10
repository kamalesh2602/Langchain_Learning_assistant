from agents.explainer import explain_topic
from agents.quiz import generate_quiz
from agents.evaluator import evaluate_answer
from state import LearningState

state = LearningState()

while True:
    print("\n=== Learning Assistant ===")
    print("1. Explain Topic")
    print("2. Take Quiz")
    print("3. View Progress")
    print("4. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        topic = input("Enter Topic: ")

        state.current_topic = topic

        explanation = explain_topic(topic)

        print("\n=== EXPLANATION ===")
        print(explanation)

    elif choice == "2":

        if not state.current_topic:
            print("Please explain a topic first.")
            continue

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

        state.quiz_history.append(
            {
                "topic": state.current_topic,
                "question": state.current_question,
                "score": result.score
            }
        )

        print("\nScore:", result.score)
        print("Feedback:", result.feedback)

    elif choice == "3":

        print("\n=== PROGRESS ===")
        print("Topic:", state.current_topic)
        print("Total Score:", state.current_score)

        print("\nHistory:")

        for item in state.quiz_history:
            print(item)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")