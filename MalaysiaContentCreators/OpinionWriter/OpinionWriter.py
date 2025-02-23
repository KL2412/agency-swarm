from agency_swarm.agents import Agent


class OpinionWriter(Agent):
    def __init__(self):
        super().__init__(
            name="OpinionWriter",
            description="The OpinionWriter selects engaging articles and crafts opinion pieces with strong, clear viewpoints designed to attract significant attention.",
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
