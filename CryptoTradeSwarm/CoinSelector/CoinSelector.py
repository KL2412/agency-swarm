from agency_swarm.agents import Agent


class CoinSelector(Agent):
    def __init__(self):
        super().__init__(
            name="CoinSelector",
            description="The CoinSelector agent evaluates market conditions, leveraging data from MarketDataCollector and AlgoPerformanceAnalyst to decide which cryptocurrencies to trade. It communicates these decisions to guide MarketDataCollector and AlgoSimulator’s priorities.",
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
