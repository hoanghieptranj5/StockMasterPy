import time

import pandas as pd
from selenium.webdriver.common.by import By

from selenium_driver import WebDriverManager
from .StockFilterConstants import StockFilterConstants
from .StockFilterHelper import StockFilterHelper


class Recommender:
    def __init__(self, driver_path: str):
        self.driver_manager = WebDriverManager(driver_path)
        self.driver_manager.start_driver()

    def get_recommendations(self, save_file: bool = False) -> list:
        df = pd.read_csv('resources/hose_stocks.csv')

        recommendations = []
        for idx, ticker in enumerate(df['symbol']):
            print(f'Processing row {idx + 1} of {len(df)}...')
            self.driver_manager.go_to_page(StockFilterHelper.get_page(ticker))

            time.sleep(1)
            no_value = self.driver_manager.find_element_by_xpath('//h3')
            # Don't need to keep processing null values
            if no_value.text == '0.00':
                continue

            rows = self.driver_manager.find_elements_by_xpath(StockFilterConstants.BROKER_VIEW_TBODY_ROW_XPATH)

            for row in rows:
                recommend_data = {
                                  'Ticker': ticker,
                                  'Date': row.find_element(By.XPATH, './/td[1]').text.strip(),
                                  'Broker': row.find_element(By.XPATH, './/td[2]').text.strip(),
                                  'Suggestion': row.find_element(By.XPATH, './/td[3]').text.strip(),
                                  'Price': row.find_element(By.XPATH, './/td[4]').text.strip()}

                recommendations.append(recommend_data)

        if save_file:
            self.save_to_csv(recommendations)

        return recommendations

    @staticmethod
    def save_to_csv(recommendations):
        df = pd.DataFrame(recommendations)
        df.to_csv('resources/hose_recommendations.csv', index=False)

    def close_driver(self):
        self.driver_manager.quit_driver()