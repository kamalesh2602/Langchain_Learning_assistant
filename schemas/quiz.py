from pydantic import BaseModel

class QuizQuestion(BaseModel):
    question: str
    answer: str