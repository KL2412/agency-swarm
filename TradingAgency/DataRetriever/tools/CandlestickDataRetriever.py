from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class CandlestickDataRetriever(BaseTool):
    """
    This tool retrieves candlestick (Klines) data for a specified symbol and interval from Binance's public API endpoint '/api/v3/klines'.
    It handles HTTP requests and parses the JSON response to extract open, high, low, close prices, and volume data.
    """

    symbol: str = Field(
        ..., description="The symbol for which to retrieve the candlestick data, e.g., 'BTCUSDT'."
    )
    interval: str = Field(
        ..., description="The interval for the candlestick data, e.g., '1m', '5m', '1h', '1d'."
    )
    limit: int = Field(
        500, description="The limit of candlestick entries to retrieve. Default is 500."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method retrieves candlestick data for the specified symbol and interval from Binance's API.
        """
        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.interval}&limit={self.limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            klines = response.json()
            candlestick_data = [
                {
                    "open_time": kline[0],
                    "open": kline[1],
                    "high": kline[2],
                    "low": kline[3],
                    "close": kline[4],
                    "volume": kline[5],
                    "close_time": kline[6]
                }
                for kline in klines
            ]
            return f"Candlestick data for {self.symbol} at {self.interval} interval: {candlestick_data}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while retrieving the candlestick data: {e}"