from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict
import numpy as np

class MarketEvaluator(BaseTool):
    """
    This tool evaluates market conditions by analyzing data from the MarketDataCollector.
    It assesses factors such as price trends, volume changes, and market sentiment to identify potential trading opportunities.
    """

    market_data: List[Dict[str, float]] = Field(
        ..., description="A list of dictionaries containing market data. Each dictionary should have keys: 'price', 'volume', and 'sentiment'."
    )

    def run(self):
        """
        Evaluates market conditions and identifies potential trading opportunities.
        """
        try:
            # Analyze price trends
            prices = [data['price'] for data in self.market_data]
            price_trend = self.analyze_trend(prices)

            # Analyze volume changes
            volumes = [data['volume'] for data in self.market_data]
            volume_change = self.analyze_volume_change(volumes)

            # Analyze market sentiment
            sentiments = [data['sentiment'] for data in self.market_data]
            average_sentiment = np.mean(sentiments)

            # Identify potential trading opportunities
            opportunities = self.identify_opportunities(price_trend, volume_change, average_sentiment)

            return opportunities

        except Exception as e:
            return f"An error occurred while evaluating market conditions: {e}"

    def analyze_trend(self, prices):
        """
        Analyzes the price trend based on historical price data.
        """
        if len(prices) < 2:
            return "Insufficient data for trend analysis."

        trend = "upward" if prices[-1] > prices[0] else "downward"
        return trend

    def analyze_volume_change(self, volumes):
        """
        Analyzes the change in trading volume.
        """
        if len(volumes) < 2:
            return "Insufficient data for volume analysis."

        volume_change = "increasing" if volumes[-1] > volumes[0] else "decreasing"
        return volume_change

    def identify_opportunities(self, price_trend, volume_change, average_sentiment):
        """
        Identifies potential trading opportunities based on market analysis.
        """
        opportunities = []

        if price_trend == "upward" and volume_change == "increasing" and average_sentiment > 0.5:
            opportunities.append("Consider buying due to upward trend, increasing volume, and positive sentiment.")
        elif price_trend == "downward" and volume_change == "increasing" and average_sentiment < 0.5:
            opportunities.append("Consider selling due to downward trend, increasing volume, and negative sentiment.")
        else:
            opportunities.append("Market conditions are not favorable for trading.")

        return opportunities

# Example usage:
# evaluator = MarketEvaluator(
#     market_data=[
#         {"price": 100, "volume": 1500, "sentiment": 0.6},
#         {"price": 105, "volume": 1600, "sentiment": 0.7},
#         {"price": 110, "volume": 1700, "sentiment": 0.8}
#     ]
# )
# print(evaluator.run())