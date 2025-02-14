from all_stocks_finder import AllStockFinder
from stock_filter import Recommender, StockComparator

if __name__ == '__main__':
    run_collect_all_stocks = False
    run_recommender = False
    run_filter_stocks = True

    driver_path = 'resources/chromedriver'
    if run_collect_all_stocks:
        finder = AllStockFinder(driver_path)
        finder.scrape_hose_stocks()
        finder.close_driver()

    if run_recommender:
        recommender = Recommender(driver_path)
        recommendations = recommender.get_recommendations(save_file=True)
        recommender.close_driver()

    if run_filter_stocks:
        # StockComparator.compare()
        StockComparator.should_buy()
