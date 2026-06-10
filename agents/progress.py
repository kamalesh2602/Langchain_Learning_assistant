from config import model
from tools.progress_tools import get_learning_stats

tool_model = model.bind_tools(
    [get_learning_stats]
)

def analyze_progress(
    total_score,
    questions_attempted
):
    response = tool_model.invoke(
        f"""
        Analyze my learning progress.

        Total Score:
        {total_score}

        Questions Attempted:
        {questions_attempted}
        """
    )

    tool_call = response.tool_calls[0]

    tool_result = get_learning_stats.invoke(
        tool_call["args"]
    )


    final_response = model.invoke(
    f"""
    Learning Statistics:

    {tool_result}

    Give a short progress analysis.
    """
)

    return final_response.content

