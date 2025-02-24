from agency_swarm.agents import Agent


class MarketDataCollector(Agent):
    def __init__(self):
        super().__init__(
            name="MarketDataCollector",
            description="The MarketDataCollector agent gathers real-time market data using Binance's API, updating the internal database with current prices, volumes, and trends. It communicates with the CoinSelector agent to provide necessary data for decision-making.",
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
