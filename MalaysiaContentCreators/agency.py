from agency_swarm import Agency
from ContentGatherer import ContentGatherer
from OpinionWriter import OpinionWriter
from MalaysiaContentCEO import MalaysiaContentCEO
from agency_swarm.util.oai import set_openai_key
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found in .env file. Please set it.")

set_openai_key(api_key)

malaysia_content_ceo = MalaysiaContentCEO()
content_gatherer = ContentGatherer()
opinion_writer = OpinionWriter()

agency = Agency([malaysia_content_ceo, [malaysia_content_ceo, content_gatherer],
                 [malaysia_content_ceo, opinion_writer],
                 [content_gatherer, opinion_writer]],
                shared_instructions='./agency_manifesto.md',
                max_prompt_tokens=25000,
                temperature=0.3)
                
if __name__ == '__main__':
    agency.demo_gradio()