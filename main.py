import json

from all_stocks_finder import AllStockFinder
from stock_filter import Recommender, StockComparator
from config_manager import ConfigManager

if __name__ == '__main__':
    config = ConfigManager('config.json')

    if config.run_collect_all_stocks:
        finder = AllStockFinder(config.driver_path)
        finder.scrape_hose_stocks()
        finder.close_driver()

    if config.run_recommender:
        recommender = Recommender(config.driver_path)
        recommendations = recommender.get_recommendations(save_file=True)
        recommender.close_driver()

    if config.run_filter_stocks:
        # StockComparator.compare()
        StockComparator.should_buy()
