class AllStockFinderConstants:
    """
    This class defines constants to be used by the `AllStockFinder` module. 

    It includes configuration details such as file paths and XPath expressions 
    for scraping HOSE (Ho Chi Minh Stock Exchange) stock data. These constants 
    help ensure consistency and maintainability across the codebase.
    """
    RESOURCES_FOLDER_NAME = "resources"
    HOSE_STOCKS_CSV_FILE_NAME = "hose_stocks.csv"

    ALL_TR_XPATH = '//*[@id="tbody"]//tr'
    INNER_STOCK_SYMBOL_OF_TR_XPATH = './/div[1]'
    INNER_STOCK_NAME_OF_TR_XPATH = './/div[2]'
