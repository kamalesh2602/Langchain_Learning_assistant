from config import model
from langchain_core.messages import HumanMessage,SystemMessage
def explain_topic(topic:str):
    response = model.invoke(
       [
    SystemMessage(
        content="""
        You are an expert programming tutor.

        Explain clearly.
        Use English.
        Assume beginner level.
        """
    ),
    HumanMessage(
        content=f"Explain {topic}"
    )
])
    return response.content