from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

# Constants for accessing Malaysian law resources
GOV_WEBSITES = [
    "https://www.malaysia.gov.my",
    "https://www.agc.gov.my",
    "https://www.parlimen.gov.my"
]
LEGAL_PUBLICATIONS_API_URL = "https://api.legalpublications.com/malaysia"
API_KEY = "YOUR_API_KEY"

class MalaysianLawResourceTool(BaseTool):
    """
    This tool provides access to Malaysian law resources, including government websites, legal publications, and other authoritative sources.
    It enables the MalaysiaLawyer agent to verify the authenticity and compliance of content with Malaysian laws by cross-referencing multiple sources.
    The tool supports accessing and retrieving information from these resources efficiently.
    """

    query: str = Field(
        ..., description="Query to search for in Malaysian law resources."
    )

    def run(self):
        """
        Executes the search across multiple Malaysian law resources using the provided query.
        Retrieves and returns information from government websites and legal publications.
        """
        results = {}

        # Search government websites
        for website in GOV_WEBSITES:
            try:
                response = requests.get(f"{website}/search", params={"q": self.query})
                if response.status_code == 200:
                    results[website] = response.json()
                else:
                    results[website] = f"Error: Unable to access {website}. Status code: {response.status_code}"
            except Exception as e:
                results[website] = f"Error: {str(e)}"

        # Search legal publications
        try:
            response = requests.get(LEGAL_PUBLICATIONS_API_URL, params={"query": self.query, "api_key": API_KEY})
            if response.status_code == 200:
                results["legal_publications"] = response.json()
            else:
                results["legal_publications"] = f"Error: Unable to access legal publications. Status code: {response.status_code}"
        except Exception as e:
            results["legal_publications"] = f"Error: {str(e)}"

        return results