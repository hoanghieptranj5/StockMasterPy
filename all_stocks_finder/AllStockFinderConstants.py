class AllStockFinderConstants:
    RESOURCES_FOLDER_NAME = "resources"
    HOSE_STOCKS_CSV_FILE_NAME = "hose_stocks.csv"

    ALL_TR_XPATH = '//*[@id="tbody"]//tr'
    INNER_STOCK_SYMBOL_OF_TR_XPATH = './/div[1]'
    INNER_STOCK_NAME_OF_TR_XPATH = './/div[2]'