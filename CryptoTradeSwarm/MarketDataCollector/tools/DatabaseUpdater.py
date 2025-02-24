from agency_swarm.tools import BaseTool
from pydantic import Field
import sqlite3
from datetime import datetime

class DatabaseUpdater(BaseTool):
    """
    This tool updates the internal database with real-time market data collected from Binance's API.
    It ensures data integrity and handles any potential database errors gracefully.
    """

    symbol: str = Field(
        ..., description="The trading pair symbol for which the data is being updated, e.g., 'BTCUSDT'."
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
        Updates the internal database with the provided market data.
        Ensures data integrity and handles any potential database errors gracefully.
        """
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('market_data.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS market_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                price REAL NOT NULL,
                volume REAL NOT NULL,
                price_change_percent REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        try:
            # Insert the market data into the database
            cursor.execute('''
                INSERT INTO market_data (symbol, price, volume, price_change_percent)
                VALUES (?, ?, ?, ?)
            ''', (self.symbol, self.price, self.volume, self.price_change_percent))

            # Commit the transaction
            conn.commit()

            return f"Successfully updated the database with data for {self.symbol}."

        except sqlite3.Error as e:
            # Handle any database errors
            return f"An error occurred while updating the database: {e}"

        finally:
            # Close the database connection
            conn.close()