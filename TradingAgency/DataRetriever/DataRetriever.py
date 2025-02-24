from agency_swarm.agents import Agent


class DataRetriever(Agent):
    def __init__(self):
        super().__init__(
            name="DataRetriever",
            description="This agent retrieves market data from Binance's public API endpoints without requiring an API key.",
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
