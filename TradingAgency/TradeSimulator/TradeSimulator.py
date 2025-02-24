from agency_swarm.agents import Agent


class TradeSimulator(Agent):
    def __init__(self):
        super().__init__(
            name="TradeSimulator",
            description="The TradeSimulator agent performs simulation trades using market data provided by the DataRetriever agent. It analyzes the data and executes simulated trades based on predefined trading strategies.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
