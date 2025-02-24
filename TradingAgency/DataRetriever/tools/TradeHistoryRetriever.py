from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class TradeHistoryRetriever(BaseTool):
    """
    This tool retrieves recent trade history for a specified symbol from Binance's public API endpoint '/api/v3/trades'.
    It handles HTTP requests and parses the JSON response to extract trade details such as price, quantity, and timestamp.
    """

    symbol: str = Field(
        ..., description="The symbol for which to retrieve the recent trade history, e.g., 'BTCUSDT'."
    )
    limit: int = Field(
        500, description="The limit of trade entries to retrieve. Default is 500."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method retrieves recent trade history for the specified symbol from Binance's API.
        """
        url = f"https://api.binance.com/api/v3/trades?symbol={self.symbol}&limit={self.limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            trades = response.json()
            trade_history = [
                {
                    "price": trade.get("price"),
                    "quantity": trade.get("qty"),
                    "timestamp": trade.get("time")
                }
                for trade in trades
            ]
            return f"Recent trade history for {self.symbol}: {trade_history}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while retrieving the trade history: {e}"