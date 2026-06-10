from config import model
from schemas.quiz import QuizQuestion

quiz_model = model.with_structured_output(
    QuizQuestion
)

def generate_quiz(topic: str):
    return quiz_model.invoke(
        f"Generate one quiz question about {topic}"
    )