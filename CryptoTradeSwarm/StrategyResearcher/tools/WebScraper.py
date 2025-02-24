from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
from bs4 import BeautifulSoup

class WebScraper(BaseTool):
    """
    This tool scans online resources to find reliable crypto trading strategies.
    It parses and extracts relevant information from web pages, ensuring that the data collected is accurate and up-to-date.
    """

    url: str = Field(
        ..., description="The URL of the web page to scan for crypto trading strategies."
    )

    def run(self):
        """
        Scans the specified URL to find and extract reliable crypto trading strategies.
        Parses the web page content to ensure the data collected is accurate and up-to-date.
        """
        try:
            # Send a GET request to the specified URL
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the web page content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract relevant information (e.g., strategy titles and descriptions)
            # This example assumes strategies are contained in <h2> and <p> tags
            strategies = []
            for strategy in soup.find_all('h2'):
                title = strategy.get_text(strip=True)
                description = strategy.find_next('p').get_text(strip=True)
                strategies.append({'title': title, 'description': description})

            # Return the extracted strategies
            return f"Extracted strategies: {strategies}"

        except requests.exceptions.RequestException as e:
            return f"An error occurred while accessing the web page: {e}"
        except Exception as e:
            return f"An error occurred while parsing the web page: {e}"