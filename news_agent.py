from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# News Agent

new_agent = Agent(
    name = "News Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = [
        'Search the latest news about Nvidia stock',
        'Summarize the top 5 news articles',
        'provide key insights in markdown formate for read'
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)

new_agent.print_response(
    "Find the Summarize latest financial news about Nvidia stock",
    stream = True
)
