from config import model
from langchain_core.messages import HumanMessage, SystemMessage
def explain_topic(topic:str):
    response = model.invoke(
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
    )

    return response.content