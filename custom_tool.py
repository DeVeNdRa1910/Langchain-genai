from langchain.tools import tool


# Create the function for greeting 

# First we need to create the function then we convert that function in the tool using the tool decorator
@tool
def get_greeting(name: str) -> str:
    """Generate the greeting message for the user"""
    return f"Hello {name}, welcome to the AI world."

# Now we can use that tool with our llm

result = get_greeting.invoke({"name": "Divyanshi singh"})

print(result)

print(get_greeting.name)
print(get_greeting.description)
print(get_greeting.args)