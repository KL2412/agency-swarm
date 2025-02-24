from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class DecisionCommunicator(BaseTool):
    """
    This tool communicates trading decisions to the MarketDataCollector and AlgoSimulator agents.
    It ensures that the decisions are transmitted accurately and efficiently, and handles any communication errors gracefully.
    """

    trading_decisions: List[Dict[str, str]] = Field(
        ..., description="A list of trading decisions to be communicated. Each decision should be a dictionary with keys: 'decision', 'target_agent', and 'details'."
    )

    def run(self):
        """
        Communicates trading decisions to the specified agents and handles any communication errors.
        """
        try:
            for decision in self.trading_decisions:
                self.send_decision(decision)

            return "Trading decisions communicated successfully to the respective agents."

        except Exception as e:
            return f"An error occurred while communicating trading decisions: {e}"

    def send_decision(self, decision):
        """
        Simulates sending a trading decision to the specified agent.
        """
        # Placeholder for actual communication logic
        # Replace with actual communication code
        print(f"Sending decision to {decision['target_agent']}: {decision['decision']} - {decision['details']}")

# Example usage:
# communicator = DecisionCommunicator(
#     trading_decisions=[
#         {"decision": "Buy", "target_agent": "MarketDataCollector", "details": "Buy 100 shares of XYZ."},
#         {"decision": "Sell", "target_agent": "AlgoSimulator", "details": "Sell 50 shares of ABC."}
#     ]
# )
# print(communicator.run())