from langchain_community.tools import tool

# #step 1 : Create simple function
# def multiply_numbers(a ,b):
#     """Multiply two numbers"""
#     return a * b

# #step 2: add type hints
# def multiply_numbers(a: int, b: int) -> int:
#     """Multiply two numbers"""
#     return a * b

#step 3: add @tool decorator
@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

result = multiply_numbers.invoke({"a": 5, "b": 7})

print(f"Multiplication Result: {result}")

print(multiply_numbers.metadata)
print(multiply_numbers.name)
print(multiply_numbers.description)
print(multiply_numbers.args)

print("json formate of args:")
print(multiply_numbers.args_schema.model_json_schema())

