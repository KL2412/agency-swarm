from agency_swarm.agents import Agent


class TradingCEO(Agent):
    def __init__(self):
        super().__init__(
            name="TradingCEO",
            description="The TradingCEO oversees the operations of the TradingAgency, manages communication between agents, and ensures that the trading strategies are aligned with the agency's goals.",
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
