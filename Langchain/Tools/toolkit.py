from langchain_community.tools import tool

@tool
def multiply_numbers(a: int, b: int) -> int:       
    """Multiply two numbers"""
    return a * b

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

class MathTools:
    def get_tools   (self):
        return [multiply_numbers, add_numbers]
    
toolkit = MathTools()
tools = toolkit.get_tools()

for t in tools:
    result = t.invoke({"a": 5, "b": 7})
    print(f"{t.name} Result: {result}")

