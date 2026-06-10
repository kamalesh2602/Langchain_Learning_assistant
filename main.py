from agents.explainer import explain_topic
from agents.quiz import generate_quiz
from agents.evaluator import evaluate_answer
from state import LearningState
from agents.router import route_request

state = LearningState()

while True:
    print("\n=== Learning Assistant ===")
    print("1. Explain Topic")
    print("2. Take Quiz")
    print("3. View Progress")
    print("4. Exit")

    query = input("\n>>>")
    route = route_request(query)


    if route.action == "explain":

        if not route.topic:
            print("Please provide a topic")
            continue
    
        state.current_topic = route.topic

        explanation = explain_topic(state.current_topic)

        print("\n=== EXPLANATION ===")
        print(explanation)

    elif route.action == "quiz":

        topic = route.topic or state.current_topic


        if not topic:
            print("Please explain a topic first.")
            continue

        quiz = generate_quiz(
            state.current_topic
        )

        state.current_topic = topic
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

    elif route.action == "progress":
        print(f"Topic: {state.current_topic}")

        print(f"Score: {state.current_score}")

        print(state.quiz_history)
        

    elif route.action == "exit":
        print("Goodbye!")
        break

    elif route.action == "unknown":
        print("I didn't understand that request.")



