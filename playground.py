#Learning Langchain Basics


import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from pydantic import BaseModel
from langchain.tools import tool


load_dotenv()
api = os.getenv("OPEN_ROUTER")


class Evaluation(BaseModel):
    score: int
    feedback: str
    improvement_area: str

class QuizQuestion(BaseModel):
    question: str
    answer: str
    
model = init_chat_model(
    "qwen/qwen3-8b",
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER"),
)

template = PromptTemplate.from_template(
    """
    Explain {topic}
    for a beginner.
    """
)
formatted_template = template.invoke({
    "topic" : "Python string"
})

# print(formatted_template)
# print(type(formatted_template))

# response = model.invoke(formatted_template)
# print(response.content)

# print(type(model))    #<class 'langchain_openai.chat_models.base.ChatOpenAI'>
# print(type(response))     #<class 'langchain_core.messages.ai.AIMessage'>
# print(response)       #has content, tokens, metadata and a lot



messages = [
    SystemMessage(content="Teach like I am 5 years old"),
    HumanMessage(content="Explain Python Lists"),

    AIMessage(
        content="Python Lists are ordered collections."
    ),

    HumanMessage(
        content="Give 3 examples."
    )
]

# response = model.invoke(messages)

# print(response.content)
# print(type(HumanMessage(content="Hi")))
# print(type(AIMessage(content="Hello")))

structured_model = model.with_structured_output(Evaluation)

#print(type(structured_model))   #<class 'langchain_core.runnables.base.RunnableSequence'>

result = structured_model.invoke(
    """
    Evaluate this answer.

    Question:
    What is OOP?

    Student Answer:
    OOP is Object Oriented Programming.
    """
)

# print(result)
# print(type(result))

quiz_model = model.with_structured_output(QuizQuestion)

result = quiz_model.invoke(
    "Generate one Python OOP question"
)

# print(result)
# print(type(result))

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


print(type(multiply))
print(multiply.name)
print(multiply.description)

print(
    multiply.invoke({
        "a": 5,
        "b": 10
    })
)

tool_model = model.bind_tools([multiply])

response = tool_model.invoke(
    "What is 258 * 947?"
)

print(response.tool_calls)

# if response.tool_calls:
#     tool_call = response.tool_calls[0]

#     tool_result = multiply.invoke(
#         tool_call["args"]
#     )

#     print("Tool Result:", tool_result)

#     final_response = model.invoke(
#         f"""
#         User asked:
#         What is 258 * 947?

#         Tool returned:
#         {tool_result}

#         Give the final answer.
#         """
#     )

#     print(final_response.content)

response1 = model.invoke(
    "My name is Kamal"
)

print(response1.content)

response2 = model.invoke(
    "What is my name?"
)

print(response2.content)