from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class AlgorithmSender(BaseTool):
    """
    This tool sends the converted algorithms to the AlgoSimulator agent for testing.
    It ensures that the data is transmitted accurately and efficiently, and handles any communication errors gracefully.
    """

    algorithm: dict = Field(
        ..., description="The converted algorithm to be sent to the AlgoSimulator agent."
    )
    simulator_url: str = Field(
        ..., description="The URL of the AlgoSimulator agent's API endpoint."
    )

    def run(self):
        """
        Sends the converted algorithm to the AlgoSimulator agent for testing.
        Ensures accurate and efficient data transmission, and handles communication errors gracefully.
        """
        try:
            # Send a POST request to the AlgoSimulator agent's API endpoint
            response = requests.post(self.simulator_url, json=self.algorithm)
            response.raise_for_status()  # Raise an error for bad responses

            # Return the response from the AlgoSimulator agent
            return f"Algorithm successfully sent to AlgoSimulator: {response.json()}"

        except requests.exceptions.RequestException as e:
            return f"An error occurred while sending the algorithm: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"