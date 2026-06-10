from agents.explainer import explain_topic
from agents.quiz import generate_quiz
from agents.evaluator import evaluate_answer
from state import LearningState
from agents.router import route_request
from agents.planner import create_plan
from agents.progress import analyze_progress


state = LearningState()

while True:
    print("\n=== Learning Assistant ===")
    print("0. Teach Topic")
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

        quiz = generate_quiz(topic)

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

    elif route.action == "teach":

        if not route.topic:
            print("Please provide a topic.")
            continue

        state.current_topic = route.topic

        plan = create_plan(route.topic)

        print("\n=== PLAN ===")
        print(plan)
        approval = input("\nApprove plan? (y/n): ")
        if approval.lower() != "y":
            print("Teaching cancelled.")
            continue

        explanation = explain_topic(route.topic)

        print("\n=== EXPLANATION ===")
        print(explanation)

        quiz = generate_quiz(route.topic)

        state.current_question = quiz.question

        print("\n=== QUIZ ===")
        print(quiz.question)
        state.current_question = quiz.question

        answer = input("\nYour Answer: ")

        result = evaluate_answer(state.current_question,answer)

        state.current_score += result.score

        state.quiz_history.append(
            {
                "topic": route.topic,
                "question": state.current_question,
                "score": result.score
            }
        )

        print("\n=== RESULT ===")
        print("Score:", result.score)
        print("Feedback:", result.feedback)


    elif route.action == "progress":
        from agents.progress import analyze_progress

        result = analyze_progress(
    total_score=state.current_score,
    questions_attempted=len(
        state.quiz_history
    )
)

        print(result)
        

    elif route.action == "exit":
        print("Goodbye!")
        break

    elif route.action == "unknown":
        print("I didn't understand that request.")



