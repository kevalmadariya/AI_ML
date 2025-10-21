# !pip install langchain==0.3.27
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests
from langchain import hub
from langchain.agents import create_agent # Corrected import
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'

  response = requests.get(url)

  return response.json()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")  # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# Step 5: Invoke
response = agent.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})
print(response)

response['output']