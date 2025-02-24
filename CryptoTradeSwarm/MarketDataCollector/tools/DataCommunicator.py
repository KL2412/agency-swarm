from agency_swarm.tools import BaseTool
from pydantic import Field

class DataCommunicator(BaseTool):
    """
    This tool facilitates communication with the CoinSelector agent, providing it with the necessary market data
    for decision-making. It ensures that the data is transmitted accurately and efficiently.
    """

    symbol: str = Field(
        ..., description="The trading pair symbol for which the data is being communicated, e.g., 'BTCUSDT'."
    )
    price: float = Field(
        ..., description="The latest price of the trading pair."
    )
    volume: float = Field(
        ..., description="The 24-hour trading volume of the trading pair."
    )
    price_change_percent: float = Field(
        ..., description="The 24-hour price change percentage of the trading pair."
    )

    def run(self):
        """
        Facilitates communication with the CoinSelector agent by providing the necessary market data.
        Ensures that the data is transmitted accurately and efficiently.
        """
        # Construct the data payload to be sent to the CoinSelector agent
        data_payload = {
            "symbol": self.symbol,
            "price": self.price,
            "volume": self.volume,
            "price_change_percent": self.price_change_percent
        }

        # Simulate sending data to the CoinSelector agent
        # In a real-world scenario, this could involve sending data over a network or through an API
        # For demonstration purposes, we'll just return the data payload
        return f"Data sent to CoinSelector agent: {data_payload}"