from agency_swarm.tools import BaseTool
from pydantic import Field
import schedule
import time
import threading

class ContinuousTradingManager(BaseTool):
    """
    This tool ensures continuous short-term trading operations by managing the execution of trade simulations at regular intervals.
    It handles scheduling and execution of simulations, ensuring that the system operates smoothly without interruptions.
    """

    simulation_function: callable = Field(
        ..., description="The function to execute for running trade simulations."
    )
    interval: int = Field(
        ..., description="The interval in seconds at which to run the trade simulations."
    )

    def run(self):
        """
        Manages the scheduling and execution of trade simulations at regular intervals.
        Ensures continuous operation without interruptions.
        """
        def job():
            try:
                # Execute the simulation function
                self.simulation_function()
                print("Trade simulation executed successfully.")
            except Exception as e:
                print(f"An error occurred during trade simulation execution: {e}")

        # Schedule the job at the specified interval
        schedule.every(self.interval).seconds.do(job)

        # Run the scheduler in a separate thread to avoid blocking
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(1)

        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.daemon = True
        scheduler_thread.start()

        return "Continuous trading manager started. Simulations will run at regular intervals."

# Example usage:
# def my_simulation_function():
#     print("Running trade simulation...")

# manager = ContinuousTradingManager(simulation_function=my_simulation_function, interval=60)
# manager.run()