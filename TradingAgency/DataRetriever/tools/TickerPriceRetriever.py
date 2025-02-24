from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class TickerPriceRetriever(BaseTool):
    """
    This tool retrieves the latest ticker prices for a specified symbol from Binance's public API endpoint '/api/v3/ticker/price'.
    It handles HTTP requests and parses the JSON response to extract the price information.
    """

    symbol: str = Field(
        ..., description="The symbol for which to retrieve the latest ticker price, e.g., 'BTCUSDT'."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method retrieves the latest ticker price for the specified symbol from Binance's API.
        """
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            price = data.get("price")
            return f"The latest price for {self.symbol} is {price}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while retrieving the price: {e}"