from langchain.tools import tool

@tool
def get_learning_stats(total_score: int,questions_attempted: int):
    """Calculate learning statistics."""

    average = 0

    if questions_attempted > 0:
        average = total_score / questions_attempted

    return {
        "total_score": total_score,
        "questions_attempted": questions_attempted,
        "average_score": average
    }