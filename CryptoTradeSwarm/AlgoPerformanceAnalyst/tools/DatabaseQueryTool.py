from agency_swarm.tools import BaseTool
from pydantic import Field
import psycopg2
from psycopg2 import sql, OperationalError

class DatabaseQueryTool(BaseTool):
    """
    This tool connects to the PostgreSQL database and queries it to identify the most effective algorithms.
    It compares algorithm performances based on preset criteria such as return on investment, risk, and consistency.
    """

    db_host: str = Field(..., description="The hostname of the PostgreSQL database.")
    db_port: int = Field(..., description="The port number of the PostgreSQL database.")
    db_name: str = Field(..., description="The name of the PostgreSQL database.")
    db_user: str = Field(..., description="The username for the PostgreSQL database.")
    db_password: str = Field(..., description="The password for the PostgreSQL database.")

    def run(self):
        """
        Connects to the PostgreSQL database and queries it to identify the most effective algorithms.
        Compares algorithm performances based on return on investment, risk, and consistency.
        """
        try:
            # Establish a connection to the PostgreSQL database
            connection = psycopg2.connect(
                host=self.db_host,
                port=self.db_port,
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password
            )
            cursor = connection.cursor()

            # Define the SQL query to select the most effective algorithms
            query = sql.SQL("""
                SELECT algorithm_name, return_on_investment, risk, consistency
                FROM algorithm_performance
                ORDER BY return_on_investment DESC, risk ASC, consistency DESC
                LIMIT 5
            """)

            # Execute the query
            cursor.execute(query)

            # Fetch the results
            results = cursor.fetchall()

            # Close the database connection
            cursor.close()
            connection.close()

            # Format the results for output
            formatted_results = [
                {
                    "algorithm_name": row[0],
                    "return_on_investment": row[1],
                    "risk": row[2],
                    "consistency": row[3]
                }
                for row in results
            ]

            return formatted_results

        except OperationalError as e:
            return f"Database connection error: {e}"
        except Exception as e:
            return f"An error occurred while querying the database: {e}"

# Example usage:
# db_tool = DatabaseQueryTool(
#     db_host="localhost",
#     db_port=5432,
#     db_name="trading_db",
#     db_user="user",
#     db_password="password"
# )
# print(db_tool.run())