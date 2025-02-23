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
DEFAULT_PROMPT_TEMPLATE = (
    "Find at least 5 detailed and context-rich articles that are similar to the following article: \"{article_content}\". "
    "Ensure that these articles are full and provide as much context as possible. Include the full content of each article and the source."
)

class SimilarNewsCollector(BaseTool):
    """
    This tool interacts with the Perplexity AI API to retrieve similar news articles
    based on a user-provided article. It retrieves at least 5 full-context articles
    that are related to the input article.
    """

    article_content: str = Field(
        ...,
        description="The content of the news article for which similar articles should be retrieved."
    )

    def run(self):
        """
        Executes the request to the Perplexity AI API to retrieve similar news articles.
        """
        # Initialize the OpenAI-compatible client for Perplexity API
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

        # Generate the prompt using the provided article content
        prompt = DEFAULT_PROMPT_TEMPLATE.format(article_content=self.article_content)

        # Prepare the messages payload
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an artificial intelligence assistant tasked with retrieving highly relevant and detailed articles based on a provided piece of news."
                ),
            },
            {
                "role": "user",
                "content": prompt,
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
            return f"Error: Unable to retrieve similar news articles. Details: {str(e)}"

if __name__ == "__main__":
    # Example usage with a sample article content
    sample_article = (
        "The recent developments in the technology sector have sparked a wave of innovation. "
        "For instance, the release of new AI tools has significantly impacted various industries..."
    )
    tool = SimilarNewsCollector(article_content=sample_article)
    print(tool.run())
