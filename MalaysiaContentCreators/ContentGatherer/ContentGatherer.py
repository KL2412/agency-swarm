from agency_swarm.agents import Agent

class ContentGatherer(Agent):
    def __init__(self):
        super().__init__(
            name="ContentGatherer",
            description="The ContentGatherer utilizes the Perplexity AI API to gather the latest, detailed news articles from Malaysia according to what other agent needs.",
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
