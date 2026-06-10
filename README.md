# Learning Assistant

An AI-powered Learning Assistant built using LangChain, OpenRouter, and Streamlit.

The project started as a CLI application and later evolved into a Streamlit web application. It helps users learn topics, generate quizzes, evaluate answers, track progress, and experience core AI engineering concepts such as agents, tools, routing, state management, middleware, and human-in-the-loop workflows.

---

# Features

## Explain Topics

Generate beginner-friendly explanations for any topic.

Example:

```text
Explain Python Lists
```

---

## Generate Quizzes

Create quiz questions based on a learning topic.

Example:

```text
Generate Quiz on Python OOP
```

---

## Evaluate Answers

Evaluate user answers and provide:

* Score
* Feedback
* Improvement Areas

---

## Teach Workflow

A complete learning flow:

```text
User Request
    ↓
Learning Plan
    ↓
Human Approval
    ↓
Explanation
    ↓
Quiz
    ↓
Evaluation
```

Example:

```text
Teach me Python Lists
```

---

## Progress Tracking

Track:

* Total Score
* Questions Attempted
* Average Score
* Quiz History

---

# Tech Stack

* Python
* LangChain
* OpenRouter
* Qwen 3 8B
* Pydantic
* Streamlit

---

# Project Structure

```text
learning-assistant/

├── agents/
│   ├── explainer.py
│   ├── quiz.py
│   ├── evaluator.py
│   ├── planner.py
│   ├── router.py
│   └── progress.py
│
├── schemas/
│   └── router.py
│
├── tools/
│   └── progress_tools.py
│
├── middleware/
│   └── logger.py
│
├── state.py
├── config.py
├── main.py
└── app.py
```

---

# Core Concepts Implemented

## 1. Chat Models

Initialize and use LLMs through LangChain.

```python
model = init_chat_model(...)
```

---

## 2. Messages

Used:

* SystemMessage
* HumanMessage
* AIMessage

For structured conversations.

---

## 3. Structured Output

Used Pydantic models to receive structured responses.

Example:

```python
class Evaluation(BaseModel):
    score: int
    feedback: str
    improvement_area: str
```

---

## 4. Agents

Specialized agents were created for different tasks.

### Explainer Agent

Explains topics.

### Quiz Agent

Generates quiz questions.

### Evaluator Agent

Evaluates user answers.

### Planner Agent

Creates learning plans.

### Progress Agent

Analyzes learning progress.

### Router Agent

Routes user requests to the correct agent.

---

## 5. State Management

Application state is maintained using a custom LearningState object.

Tracks:

* Current Topic
* Current Question
* Total Score
* Quiz History

---

## 6. Dynamic Routing

User requests are routed dynamically.

Example:

```text
Explain Python Lists
```

↓

```text
Explainer Agent
```

---

```text
Generate Quiz on OOP
```

↓

```text
Quiz Agent
```

---

## 7. Multi-Agent Workflow

The Teach feature uses multiple agents together.

```text
Router Agent
    ↓
Planner Agent
    ↓
Explainer Agent
    ↓
Quiz Agent
    ↓
Evaluator Agent
```

---

## 8. Tools

Custom LangChain tools were implemented.

Example:

```python
@tool
def get_learning_stats(...)
```

Used for learning analytics and progress tracking.

---

## 9. Tool Calling

Implemented:

```python
model.bind_tools(...)
```

Workflow:

```text
Agent
    ↓
Tool Decision
    ↓
Tool Execution
    ↓
Final Response
```

---

## 10. Human In The Loop (HITL)

Before starting a learning session:

```text
Generate Plan
    ↓
Approve Plan?
    ↓
Continue
```

The user explicitly approves the generated learning plan.

---

## 11. Middleware

Request logging middleware was implemented.

Example:

```text
User Request
    ↓
Middleware
    ↓
Router
    ↓
Agent
```

Used for request logging and preprocessing.

---

# CLI Version

Run:

```bash
uv run main.py
```

Features:

* Explain Topics
* Generate Quizzes
* Evaluate Answers
* Teach Workflow
* Progress Tracking

---

# Streamlit Version

Run:

```bash
uv run streamlit run app.py
```

Features:

* Web Interface
* Topic Explanation
* Quiz Generation
* Answer Evaluation
* Progress Dashboard
* Interactive Learning Workflow

---

# Example Workflow

```text
Teach me Python Lists

↓
Generate Learning Plan

↓
Approve Plan

↓
Read Explanation

↓
Take Quiz

↓
Receive Feedback

↓
Track Progress
```

---

# Future Improvements

* Multimodal Learning (Image Uploads)
* PDF Notes Analysis
* Persistent Database Storage
* User Authentication
* Learning Streaks
* RAG-based Learning Assistant
* Personalized Learning Paths

---

# Learning Outcomes

This project was built to understand practical AI engineering concepts using LangChain.

Key concepts learned:

* Chat Models
* Prompting
* Messages
* Structured Outputs
* State Management
* Tools
* Tool Calling
* Dynamic Routing
* Multi-Agent Systems
* Human In The Loop
* Middleware
* Streamlit Integration

The project serves as a hands-on implementation of modern AI application development patterns.
