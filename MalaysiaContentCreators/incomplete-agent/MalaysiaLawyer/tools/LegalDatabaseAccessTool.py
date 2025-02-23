from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

# Constants for accessing the legal database API
LEGAL_DATABASE_API_URL = "https://api.legaldatabase.com/malaysia"
API_KEY = "YOUR_API_KEY"

class LegalDatabaseAccessTool(BaseTool):
    """
    This tool provides access to a comprehensive legal database that includes Malaysian laws, regulations, and legal precedents.
    It allows the MalaysiaLawyer agent to search for specific laws or legal information relevant to the content being reviewed.
    The tool supports keyword searches, filtering by legal categories, and retrieving detailed legal documents or summaries.
    """

    keyword: str = Field(
        ..., description="Keyword to search for in the legal database."
    )
    category: str = Field(
        None, description="Optional legal category to filter the search results."
    )

    def run(self):
        """
        Executes the search in the legal database using the provided keyword and optional category.
        Retrieves and returns detailed legal documents or summaries.
        """
        # Prepare the request parameters
        params = {
            "keyword": self.keyword,
            "category": self.category,
            "api_key": API_KEY
        }

        # Make the request to the legal database API
        response = requests.get(LEGAL_DATABASE_API_URL, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the search results
            return response.json()
        else:
            # Handle errors
            return f"Error: Unable to access the legal database. Status code: {response.status_code}"