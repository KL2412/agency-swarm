from agency_swarm.tools import BaseTool
from pydantic import Field
import numpy as np

class MarketDataAnalyzer(BaseTool):
    """
    A tool to analyze market data and identify trading opportunities.
    This tool processes current prices, order book details, and recent trades
    to identify buy and sell signals based on predefined trading strategies.
    """

    current_prices: list = Field(
        ..., description="List of current prices for analysis."
    )
    order_book: dict = Field(
        ..., description="Order book details including bids and asks."
    )
    recent_trades: list = Field(
        ..., description="List of recent trades for analysis."
    )

    def analyze_price_trends(self):
        """Analyze price trends to identify potential buy/sell signals."""
        if len(self.current_prices) < 2:
            return "Insufficient data for trend analysis."

        # Simple moving average strategy
        short_window = 5
        long_window = 10

        if len(self.current_prices) < long_window:
            return "Insufficient data for moving average analysis."

        short_mavg = np.mean(self.current_prices[-short_window:])
        long_mavg = np.mean(self.current_prices[-long_window:])

        if short_mavg > long_mavg:
            return "Buy signal based on moving average crossover."
        elif short_mavg < long_mavg:
            return "Sell signal based on moving average crossover."
        else:
            return "No clear signal from moving average crossover."

    def analyze_order_book_depth(self):
        """Analyze order book depth to identify potential buy/sell signals."""
        bids = self.order_book.get('bids', [])
        asks = self.order_book.get('asks', [])

        if not bids or not asks:
            return "Insufficient order book data."

        # Calculate total volume for top 5 bids and asks
        top_bids_volume = sum(float(bid[1]) for bid in bids[:5])
        top_asks_volume = sum(float(ask[1]) for ask in asks[:5])

        if top_bids_volume > top_asks_volume:
            return "Buy signal based on order book depth."
        elif top_bids_volume < top_asks_volume:
            return "Sell signal based on order book depth."
        else:
            return "No clear signal from order book depth."

    def analyze_trade_volume(self):
        """Analyze trade volume to identify potential buy/sell signals."""
        if not self.recent_trades:
            return "Insufficient trade data."

        # Calculate average trade volume
        volumes = [float(trade['qty']) for trade in self.recent_trades]
        avg_volume = np.mean(volumes)

        # Simple strategy: if recent trade volume is significantly higher than average, signal a buy
        recent_volume = float(self.recent_trades[-1]['qty'])
        if recent_volume > 1.5 * avg_volume:
            return "Buy signal based on increased trade volume."
        elif recent_volume < 0.5 * avg_volume:
            return "Sell signal based on decreased trade volume."
        else:
            return "No clear signal from trade volume."

    def run(self):
        """
        Execute analysis on market data to identify trading opportunities.
        """
        price_trend_signal = self.analyze_price_trends()
        order_book_signal = self.analyze_order_book_depth()
        trade_volume_signal = self.analyze_trade_volume()

        return {
            "price_trend_signal": price_trend_signal,
            "order_book_signal": order_book_signal,
            "trade_volume_signal": trade_volume_signal
        }