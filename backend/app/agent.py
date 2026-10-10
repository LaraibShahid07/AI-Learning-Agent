from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage

from app.config import GOOGLE_API_KEY
from app.prompts import SYSTEM_PROMPT
from app.tools import calculator

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3,
)

# Register Tools
tools = [calculator]

# Create Agent
agent = create_react_agent(
    model=llm,
    tools=tools,
)


def ask_agent(question: str):

    response = agent.invoke(
        {
            "messages": [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=question),
            ]
        }
    )

    last_message = response["messages"][-1]

    # Return clean text
    if hasattr(last_message, "text"):
        return last_message.text

    if hasattr(last_message, "content"):
        if isinstance(last_message.content, str):
            return last_message.content

        if isinstance(last_message.content, list):
            for item in last_message.content:
                if isinstance(item, dict) and item.get("type") == "text":
                    return item.get("text", "")

    return str(last_message)