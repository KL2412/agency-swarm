from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class PerformanceComparator(BaseTool):
    """
    This tool compares the performances of different algorithms based on preset criteria such as return on investment, risk, and consistency.
    It provides insights into which algorithms are performing best and why.
    """

    algorithm_data: List[Dict[str, float]] = Field(
        ..., description="A list of dictionaries containing algorithm performance data. Each dictionary should have keys: 'algorithm_name', 'return_on_investment', 'risk', and 'consistency'."
    )

    def run(self):
        """
        Compares the performances of different algorithms and provides insights into their effectiveness.
        """
        try:
            # Sort algorithms by return on investment, risk, and consistency
            sorted_algorithms = sorted(
                self.algorithm_data,
                key=lambda x: (x['return_on_investment'], -x['risk'], x['consistency']),
                reverse=True
            )

            # Generate insights
            insights = []
            for algo in sorted_algorithms:
                insight = (
                    f"Algorithm '{algo['algorithm_name']}' has a return on investment of {algo['return_on_investment']}, "
                    f"risk level of {algo['risk']}, and consistency score of {algo['consistency']}."
                )
                insights.append(insight)

            return insights

        except Exception as e:
            return f"An error occurred while comparing algorithm performances: {e}"

# Example usage:
# comparator = PerformanceComparator(
#     algorithm_data=[
#         {"algorithm_name": "Algo1", "return_on_investment": 0.15, "risk": 0.05, "consistency": 0.9},
#         {"algorithm_name": "Algo2", "return_on_investment": 0.10, "risk": 0.03, "consistency": 0.85},
#         {"algorithm_name": "Algo3", "return_on_investment": 0.20, "risk": 0.07, "consistency": 0.95}
#     ]
# )
# print(comparator.run())