from agency_swarm.agents import Agent


class MalaysiaContentCEO(Agent):
    def __init__(self):
        super().__init__(
            name="MalaysiaContentCEO",
            description="The MalaysiaContentCEO oversees the entire content creation process, coordinates between agents, and ensures the agency's goals are met.",
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
