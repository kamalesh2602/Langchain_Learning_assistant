from config import model

def explain_topic(topic:str):
    response = model.invoke(
        f"Explain {topic} for a beginner."
    )

    return response.content