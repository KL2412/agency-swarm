from agency_swarm.agents import Agent


class MalaysiaLawyer(Agent):
    def __init__(self):
        super().__init__(
            name="MalaysiaLawyer",
            description="The MalaysiaLawyer reviews content to ensure compliance with Malaysian laws.",
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
