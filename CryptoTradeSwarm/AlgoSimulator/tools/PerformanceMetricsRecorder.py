import os
from dotenv import load_dotenv
from agency_swarm.tools import BaseTool
from pydantic import Field
import psycopg2
from psycopg2 import sql, OperationalError

load_dotenv()

class PerformanceMetricsRecorder(BaseTool):
    """
    This tool stores performance metrics of trade simulations in a PostgreSQL database.
    It ensures data integrity and handles any potential database errors gracefully.
    """

    db_host: str = Field(default_factory=lambda: os.getenv("DB_HOST"), description="The hostname of the PostgreSQL database.")
    db_port: int = Field(default_factory=lambda: int(os.getenv("DB_PORT", 5432)), description="The port number of the PostgreSQL database.")
    db_name: str = Field(default_factory=lambda: os.getenv("DB_NAME"), description="The name of the PostgreSQL database.")
    db_user: str = Field(default_factory=lambda: os.getenv("DB_USER"), description="The username for the PostgreSQL database.")
    db_password: str = Field(default_factory=lambda: os.getenv("DB_PASSWORD"), description="The password for the PostgreSQL database.")
    metrics: dict = Field(..., description="The performance metrics to be stored in the database.")

    def run(self):
        """
        Stores the provided performance metrics in the PostgreSQL database.
        Ensures data integrity and handles any potential database errors gracefully.
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

            # Define the SQL query to insert performance metrics
            insert_query = sql.SQL("""
                INSERT INTO trade_performance_metrics (metric_name, metric_value)
                VALUES (%s, %s)
            """)

            # Insert each metric into the database
            for metric_name, metric_value in self.metrics.items():
                cursor.execute(insert_query, (metric_name, metric_value))

            # Commit the transaction
            connection.commit()

            # Close the database connection
            cursor.close()
            connection.close()

            return "Performance metrics successfully recorded in the database."

        except OperationalError as e:
            return f"Database connection error: {e}"
        except Exception as e:
            return f"An error occurred while recording performance metrics: {e}"