from config import model
from schemas.router import Route

router_model = model.with_structured_output(Route)

def route_request(user_input: str):
    return router_model.invoke(
        f"""
        Decide the action.

        Available actions:

        explain
        quiz
        progress
        exit

        User Request:
        {user_input}
        """
    )