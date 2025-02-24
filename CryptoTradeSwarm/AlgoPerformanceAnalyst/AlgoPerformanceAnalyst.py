from agency_swarm.agents import Agent


class AlgoPerformanceAnalyst(Agent):
    def __init__(self):
        super().__init__(
            name="AlgoPerformanceAnalyst",
            description="The AlgoPerformanceAnalyst agent queries the PostgreSQL database to identify the most effective algorithms, comparing their performances based on preset criteria. It communicates with the AlgoSimulator agent to provide insights on algorithm performance.",
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
