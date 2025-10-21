from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyArgs(BaseModel):
    a: int = Field(require=True, description="The first number to multiply")
    b: int = Field(require=True, description="The second number to multiply")

def multiply_fuc(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply_fuc,  
    args_schema=MultiplyArgs,
    name="multiply numbers",
    description="Multiply two numbers"
)

result = multiply_tool.invoke({"a": 5, "b": 7})

print(f"Multiplication Result: {result}")

print(multiply_tool.metadata)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)

print("json formate of args:")
print(multiply_tool.args_schema.model_json_schema())

