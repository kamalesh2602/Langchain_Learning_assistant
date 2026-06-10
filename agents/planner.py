from config import model

def create_plan(topic: str):
    response = model.invoke(
        f"""
        Create a short learning plan
        for {topic}.

        Maximum 3 steps.
        """
    )

    return response.content