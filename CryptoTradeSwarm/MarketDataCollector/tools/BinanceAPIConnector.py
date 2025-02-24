from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import requests

# Define global constants for API keys
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

class BinanceAPIConnector(BaseTool):
    """
    This tool connects to Binance's API to gather real-time market data, including prices, volumes, and trends.
    It handles authentication securely and ensures compliance with Binance's API usage policies.
    """

    symbol: str = Field(
        ..., description="The trading pair symbol to fetch data for, e.g., 'BTCUSDT'."
    )

    def run(self):
        """
        Connects to Binance's API to fetch real-time market data for the specified trading pair symbol.
        Returns the latest price, volume, and trend data.
        """
        base_url = "https://api.binance.com"
        endpoint = f"/api/v3/ticker/24hr"
        headers = {
            "X-MBX-APIKEY": api_key
        }
        params = {
            "symbol": self.symbol
        }

        try:
            response = requests.get(base_url + endpoint, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Extract relevant data
            price = data.get("lastPrice")
            volume = data.get("volume")
            price_change_percent = data.get("priceChangePercent")

            result = (
                f"Symbol: {self.symbol}\n"
                f"Last Price: {price}\n"
                f"Volume: {volume}\n"
                f"Price Change (24h): {price_change_percent}%"
            )
            return result

        except requests.exceptions.RequestException as e:
            return f"An error occurred while fetching data from Binance: {e}"