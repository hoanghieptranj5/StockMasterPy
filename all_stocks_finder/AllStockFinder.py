from selenium.webdriver.common.by import By
import pandas as pd

from all_stocks_finder.AllStockFinderConstants import AllStockFinderConstants
from selenium_driver import WebDriverManager

class AllStockFinder:
    def __init__(self, driver_path: str):
        self.driver_manager = WebDriverManager(driver_path)
        self.driver_manager.start_driver()
        self.base_url = "https://www.cophieu68.vn/market/markets.php?id=^hose"


    def scrape_stock_row(self, row):
        try:
            # Extract stock data
            stock_data = {}

            # Stock symbol and name (from <a> tag inside <td>)
            symbol_xpath = AllStockFinderConstants.INNER_STOCK_SYMBOL_OF_TR_XPATH
            name_xpath = AllStockFinderConstants.INNER_STOCK_NAME_OF_TR_XPATH
            stock_data['symbol'] = row.find_element(By.XPATH, symbol_xpath).text.strip().lower()
            stock_data['name'] = row.find_element(By.XPATH, name_xpath).get_attribute('title').strip()

            # Current price (from <td> with data-attr="close")
            price_xpath = './/td[@data-attr="close"]'
            stock_data['price'] = row.find_element(By.XPATH, price_xpath).text.strip()

            # Price change (from <td> with data-attr="price_change")
            price_change_xpath = './/td[@data-attr="price_change"]'
            stock_data['price_change'] = row.find_element(By.XPATH, price_change_xpath).text.strip()

            # Volume (from <td> with data-attr="volume")
            volume_xpath = './/td[@data-attr="volume"]'
            stock_data['volume'] = row.find_element(By.XPATH, volume_xpath).text.strip()

            # Market cap (from <td> with no specific data-attr)
            market_cap_xpath = './/td[5]'
            stock_data['market_cap'] = row.find_element(By.XPATH, market_cap_xpath).text.strip()

            # Total value (from <td> with no specific data-attr)
            total_value_xpath = './/td[6]'
            stock_data['total_value'] = row.find_element(By.XPATH, total_value_xpath).text.strip()

            # Percentage change (from <td>)
            percentage_change_xpath = './/td[7]'
            stock_data['percentage_change'] = row.find_element(By.XPATH, percentage_change_xpath).text.strip()

            # Chart link (from <a> tag inside <td>)
            chart_link_xpath = './/td[last()]/a'
            stock_data['chart_link'] = row.find_element(By.XPATH, chart_link_xpath).get_attribute('href').strip()

            # Print or return the extracted data
            return stock_data
        except Exception as e:
            print(f"Error scraping stock row: {str(e)}")
            return None

    def scrape_hose_stocks(self):
        # go to the page
        self.driver_manager.go_to_page(self.base_url)

        # get all stock rows
        rows = self.driver_manager.find_elements_by_xpath('//*[@id="tbody"]//tr')

        # list to hold all stock data dictionaries
        all_stock_data = []

        for idx, row in enumerate(rows):
            print(f'Processing row {idx + 1} of {len(rows)}...')
            stock_data = self.scrape_stock_row(row)
            if stock_data:
                all_stock_data.append(stock_data)

        # convert the list of stock data into pandas DataFrame
        if all_stock_data:
            df = pd.DataFrame(all_stock_data)
            df.to_csv(f'{AllStockFinderConstants.RESOURCES_FOLDER_NAME}/{AllStockFinderConstants.HOSE_STOCKS_CSV_FILE_NAME}', index=False)
            print(f'Saved {len(df)} rows to {AllStockFinderConstants.HOSE_STOCKS_CSV_FILE_NAME} file.')

    def close_driver(self):
        self.driver_manager.quit_driver()