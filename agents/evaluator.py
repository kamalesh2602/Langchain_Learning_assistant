from config import model
from schemas.evaluation import Evaluation

evaluation_model = model.with_structured_output(
    Evaluation
)

def evaluate_answer(
    question: str,
    answer: str
):
   return evaluation_model.invoke(
    [
        SystemMessage(
            content="""
            You are an English evaluator.

            Always respond in English.
            """
        ),
        HumanMessage(
            content=f"""
            Question:
            {question}

            Student Answer:
            {answer}

            Evaluate it.
            """
        )
    ]
)