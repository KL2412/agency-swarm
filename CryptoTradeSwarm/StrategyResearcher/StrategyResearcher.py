from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class StrategyResearcher(Agent):
    def __init__(self):
        super().__init__(
            name="StrategyResearcher",
            description="The StrategyResearcher agent scans online resources to find reliable crypto trading strategies and turns them into actionable algorithms. It sends these algorithms to the AlgoSimulator for testing.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
