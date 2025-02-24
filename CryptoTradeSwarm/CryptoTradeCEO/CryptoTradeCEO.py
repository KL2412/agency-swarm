from agency_swarm.agents import Agent


class CryptoTradeCEO(Agent):
    def __init__(self):
        super().__init__(
            name="CryptoTradeCEO",
            description="The CryptoTradeCEO agent is the central decision-maker and coordinator within the CryptoTradeSwarm agency. It oversees the entire operation to ensure all agents work harmoniously towards optimizing crypto trading strategies. It has the ability to initiate communication with all other agents in the agency.",
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
