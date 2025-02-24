from agency_swarm import Agency
from DataRetriever import DataRetriever
from TradeSimulator import TradeSimulator
from DataRetriever import DataRetriever
from TradingCEO import TradingCEO
import os
from dotenv import load_dotenv

load_dotenv()

trading_ceo = TradingCEO()
data_retriever = DataRetriever()
trade_simulator = TradeSimulator()

agency = Agency([trading_ceo, [trading_ceo, data_retriever],
                 [trading_ceo, trade_simulator],
                 [data_retriever, trade_simulator]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()