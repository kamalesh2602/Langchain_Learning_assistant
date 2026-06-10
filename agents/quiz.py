from config import model
from schemas.quiz import QuizQuestion
from langchain_core.messages import SystemMessage, HumanMessage


quiz_model = model.with_structured_output(
    QuizQuestion
)

def generate_quiz(topic: str):
    return quiz_model.invoke(
        [
            SystemMessage(
                content="""
                You are an English quiz generator.

                Always generate responses in English.
                """
            ),
            HumanMessage(
                content=f"""
                Generate one quiz question
                about {topic}
                """
            )
        ]
    )