from langchain_community.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MultiplyArgs(BaseModel):
    a: int = Field(require=True, description="The first number to multiply")
    b: int = Field(require=True, description="The second number to multiply")

class MultiplyTool(BaseTool):
    name:str = "multiply numbers"
    description:str = "Multiply two numbers"

    args_schema : Type[BaseModel] = MultiplyArgs

    def _run(self, a: int, b: int) -> int:
        """Multiply two numbers"""
        return a * b
    
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({"a": 5, "b": 7})

print(f"Multiplication Result: {result}")
print(multiply_tool.metadata)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)
print("json formate of args:")
print(multiply_tool.args_schema.model_json_schema())