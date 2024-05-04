# bambot/templates/agent_runner.py
from langchain_agent import Agent

def run_agent():
    agent = Agent()
    agent.run()

if __name__ == "__main__":
    run_agent()