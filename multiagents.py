from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")

# 1st agent -- Live Cricket Agents

match_agent = Agent(
    name = "Live Cricket Agent",
    model = OpenAIChat(id = 'gpt-4o',api_key = api_key),
    tools = [DuckDuckGo()],
    instructions = [
        "Search for live cricket match scores.",
        "Summarize the score, top players, and match situation.",
        "Use markdown tables for better clarity and readability."
    ],
show_tool_calls = True,
markdown = True,
debug_mode = True
)

# 2nd agent -- Player Stats Agent

player_agent = Agent(
    name = "Player Stats Agent",
    model = OpenAIChat(id = 'gpt-4o',api_key = api_key),
    tools = [DuckDuckGo()],
    instructions = [
        "Find recent cricket player statistics.",
        "Include batting and bowling stats for the last 5 matches.",
        "Use tables for formatting."
    ],
show_tool_calls = True,
markdown = True,
debug_mode = True
)

# 3rd agent -- Cricket News Agent

news_agent = Agent(
    name = "Cricket News Agent",
    model = OpenAIChat(id = 'gpt-4o',api_key = api_key),
    tools = [DuckDuckGo()],
    instructions = [
        "Find and summarize the latest cricket news.",
        "Highlight upcoming matches, injuries, and tournament updates.",
        "List headlines with sources."
    ],
show_tool_calls = True,
markdown = True,
debug_mode = True
)

# Main cricket team agent(combining all agents)

cricket_team = Agent(
    name = "Cricket Analysis Team",
    model = OpenAIChat(id = 'gpt-4o', api_key = api_key),
    team = [match_agent, player_agent, news_agent],
    instructions = [
       "Provide live match scores, player statistics, and news updates.",
        "Use structured formatting and markdown tables.",
    ],
show_tool_calls = True,
markdown = False,
debug_mode = True
)

cricket_team.print_response(
    "Get the latest score of the India vs Pakisthan match, recent stats for Virat Kohli, and cricket news.",
    stream = True
)