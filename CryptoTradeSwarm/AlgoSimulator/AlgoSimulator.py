from agency_swarm.agents import Agent


class AlgoSimulator(Agent):
    def __init__(self):
        super().__init__(
            name="AlgoSimulator",
            description="The AlgoSimulator agent performs trade simulations using both historical and real-time data, storing performance metrics in a PostgreSQL database. It ensures continuous short-term trading operations and communicates with the CoinSelector and AlgoPerformanceAnalyst agents.",
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
