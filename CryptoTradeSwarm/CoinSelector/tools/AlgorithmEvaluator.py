from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class AlgorithmEvaluator(BaseTool):
    """
    This tool evaluates the performance of different algorithms using data from the AlgoPerformanceAnalyst.
    It compares algorithms based on criteria such as return on investment, risk, and consistency to decide which algorithms to prioritize for trading.
    """

    algorithm_data: List[Dict[str, float]] = Field(
        ..., description="A list of dictionaries containing algorithm performance data. Each dictionary should have keys: 'algorithm_name', 'return_on_investment', 'risk', and 'consistency'."
    )

    def run(self):
        """
        Evaluates algorithm performance and determines which algorithms to prioritize for trading.
        """
        try:
            # Evaluate each algorithm based on ROI, risk, and consistency
            evaluated_algorithms = [
                self.evaluate_algorithm(algo) for algo in self.algorithm_data
            ]

            # Sort algorithms by effectiveness score
            sorted_algorithms = sorted(
                evaluated_algorithms, key=lambda x: x['effectiveness_score'], reverse=True
            )

            # Determine which algorithms to prioritize
            prioritized_algorithms = [
                algo['algorithm_name'] for algo in sorted_algorithms if algo['effectiveness_score'] > 0.7
            ]

            return prioritized_algorithms

        except Exception as e:
            return f"An error occurred while evaluating algorithm performance: {e}"

    def evaluate_algorithm(self, algo):
        """
        Evaluates a single algorithm's performance and calculates an effectiveness score.
        """
        # Calculate effectiveness score as a weighted sum of ROI, inverse risk, and consistency
        effectiveness_score = (
            algo['return_on_investment'] * 0.5 +
            (1 - algo['risk']) * 0.3 +
            algo['consistency'] * 0.2
        )

        return {
            "algorithm_name": algo['algorithm_name'],
            "effectiveness_score": effectiveness_score
        }

# Example usage:
# evaluator = AlgorithmEvaluator(
#     algorithm_data=[
#         {"algorithm_name": "Algo1", "return_on_investment": 0.15, "risk": 0.05, "consistency": 0.9},
#         {"algorithm_name": "Algo2", "return_on_investment": 0.10, "risk": 0.03, "consistency": 0.85},
#         {"algorithm_name": "Algo3", "return_on_investment": 0.20, "risk": 0.07, "consistency": 0.95}
#     ]
# )
# print(evaluator.run())