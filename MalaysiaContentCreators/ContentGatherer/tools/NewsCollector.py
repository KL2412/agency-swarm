from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("Perplexity API key not found in .env file. Please set it.")

BASE_URL = "https://api.perplexity.ai"
DEFAULT_PROMPT = (
    "Provide a summary of the 15 most important news stories from Malaysia in the last 24 hours. "
    "Include diverse topics such as politics, economy, social issues, technology, entertainment, and more. "
    "For each story, provide the headline, a very detailed summary, and the original source."
)

class NewsCollector(BaseTool):
    """
    This tool interacts with the Perplexity AI API to retrieve summaries of the latest news articles from Malaysia.
    It covers diverse topics such as politics, economy, social issues, technology, and entertainment.
    """

    prompt: str = Field(
        DEFAULT_PROMPT,
        description="The query or prompt for Perplexity AI to generate news summaries. If not provided, the default prompt will be used."
    )

    def run(self):
        """
        Executes the prompt using the Perplexity AI API and returns the generated news summaries.
        """
        # Initialize the OpenAI-compatible client for Perplexity API
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

        # Prepare the messages payload
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an artificial intelligence assistant tasked with providing concise and informative news."
                ),
            },
            {
                "role": "user",
                "content": self.prompt,
            },
        ]

        try:
            # Send a request for a chat completion
            response = client.chat.completions.create(
                model="llama-3.1-sonar-large-128k-online",
                messages=messages,
            )

            # Extract the generated message content
            generated_message = response.choices[0].message.content
            return generated_message.strip()

        except Exception as e:
            # Handle errors gracefully
            return f"Error: Unable to retrieve news summaries. Details: {str(e)}"

if __name__ == "__main__":
    # Example usage with default prompt
    tool = NewsCollector()
    print(tool.run())
