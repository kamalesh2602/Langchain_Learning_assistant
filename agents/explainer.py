from config import model
from langchain_core.messages import SystemMessage,HumanMessage

def generate_quiz(topic: str):
    return quiz_model.invoke(
        [
            SystemMessage(
                content="""
                You are an English quiz generator.

                Always respond in English.
                """
            ),
            HumanMessage(
                content=f"""
                Generate one quiz question
                about {topic}.
                """
            )
        ]
    )