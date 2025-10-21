from langchain_community.tools import ShellTool

setup_tool = ShellTool()    

result = setup_tool.invoke("python --version")

print(result)