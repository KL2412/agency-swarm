from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class OrderBookDataRetriever(BaseTool):
    """
    This tool retrieves order book data for a specified symbol from Binance's public API endpoint '/api/v3/depth'.
    It handles HTTP requests and parses the JSON response to extract bid and ask data.
    """

    symbol: str = Field(
        ..., description="The symbol for which to retrieve the order book data, e.g., 'BTCUSDT'."
    )
    limit: int = Field(
        100, description="The limit of order book entries to retrieve. Default is 100."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method retrieves order book data for the specified symbol from Binance's API.
        """
        url = f"https://api.binance.com/api/v3/depth?symbol={self.symbol}&limit={self.limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            order_book = {
                "bids": data.get("bids"),
                "asks": data.get("asks"),
            }
            return f"Order book data for {self.symbol}: {order_book}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while retrieving the order book data: {e}"