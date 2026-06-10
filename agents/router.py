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
        teach
        exit
        If the request does not match any action,
return:

action = unknown

    If user says:

"Teach me Python Lists"
"Teach Python OOP"
"Help me learn dictionaries"

return:

action = teach
topic = extracted topic
        Extract topic if present.

        User Request:
        {user_input}
        """
    )

