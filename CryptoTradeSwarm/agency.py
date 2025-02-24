from agency_swarm import Agency
from CoinSelector import CoinSelector
from AlgoPerformanceAnalyst import AlgoPerformanceAnalyst
from AlgoSimulator import AlgoSimulator
from StrategyResearcher import StrategyResearcher
from BrowsingAgent import BrowsingAgent
from MarketDataCollector import MarketDataCollector
from CryptoTradeCEO import CryptoTradeCEO
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ceo = CryptoTradeCEO()
market_data_collector = MarketDataCollector()
strategy_researcher = StrategyResearcher()
algo_simulator = AlgoSimulator()
algo_performance_analyst = AlgoPerformanceAnalyst()
coin_selector = CoinSelector()

agency = Agency([ceo, [ceo, market_data_collector],
                 [ceo, strategy_researcher],
                 [ceo, algo_simulator],
                 [ceo, algo_performance_analyst],
                 [ceo, coin_selector],
                 [market_data_collector, coin_selector],
                 [algo_simulator, coin_selector],
                 [algo_simulator, algo_performance_analyst]],
                shared_instructions='./agency_manifesto.md',
                max_prompt_tokens=25000,
                temperature=0.3)

if __name__ == '__main__':
    agency.demo_gradio()