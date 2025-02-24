from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List

class InsightsCommunicator(BaseTool):
    """
    This tool communicates insights on algorithm performance to the AlgoSimulator agent.
    It ensures that the insights are transmitted accurately and efficiently, and handles any communication errors gracefully.
    """

    insights: List[str] = Field(
        ..., description="A list of insights on algorithm performance to be communicated to the AlgoSimulator agent."
    )

    def run(self):
        """
        Communicates insights to the AlgoSimulator agent and handles any communication errors.
        """
        try:
            # Simulate sending insights to the AlgoSimulator agent
            for insight in self.insights:
                self.send_to_algo_simulator(insight)

            return "Insights communicated successfully to the AlgoSimulator agent."

        except Exception as e:
            return f"An error occurred while communicating insights: {e}"

    def send_to_algo_simulator(self, insight):
        """
        Simulates sending a single insight to the AlgoSimulator agent.
        """
        # Placeholder for actual communication logic
        # Replace with actual communication code
        print(f"Sending insight to AlgoSimulator: {insight}")

# Example usage:
# communicator = InsightsCommunicator(
#     insights=[
#         "Algorithm 'Algo1' has a return on investment of 0.15, risk level of 0.05, and execution time of 120 seconds.",
#         "Algorithm 'Algo2' has a return on investment of 0.10, risk level of 0.03, and execution time of 90 seconds."
#     ]
# )
# print(communicator.run())