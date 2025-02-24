from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class Statistics24hrRetriever(BaseTool):
    """
    This tool retrieves 24-hour statistics for a specified symbol from Binance's public API endpoint '/api/v3/ticker/24hr'.
    It handles HTTP requests and parses the JSON response to extract relevant statistics such as price change, price change percent, weighted average price, etc.
    """

    symbol: str = Field(
        ..., description="The symbol for which to retrieve the 24-hour statistics, e.g., 'BTCUSDT'."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method retrieves 24-hour statistics for the specified symbol from Binance's API.
        """
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={self.symbol}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            statistics = {
                "price_change": data.get("priceChange"),
                "price_change_percent": data.get("priceChangePercent"),
                "weighted_avg_price": data.get("weightedAvgPrice"),
                "prev_close_price": data.get("prevClosePrice"),
                "last_price": data.get("lastPrice"),
                "bid_price": data.get("bidPrice"),
                "ask_price": data.get("askPrice"),
                "open_price": data.get("openPrice"),
                "high_price": data.get("highPrice"),
                "low_price": data.get("lowPrice"),
                "volume": data.get("volume"),
                "quote_volume": data.get("quoteVolume"),
            }
            return f"24-hour statistics for {self.symbol}: {statistics}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while retrieving the statistics: {e}"