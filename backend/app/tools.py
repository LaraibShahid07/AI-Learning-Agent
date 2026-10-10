from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    print("✅ Calculator Tool Called")

    try:
        result = eval(expression)
        print("Result:", result)
        return str(result)

    except Exception as e:
        print(e)
        return "Invalid Expression"