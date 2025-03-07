import pandas as pd
from typing import List

# Constants
RECOMMENDATIONS_FILE = 'resources/hose_recommendations.csv'
STOCKS_FILE = 'resources/hose_stocks.csv'
UPDATED_RECOMMENDATIONS_FILE = 'resources/updated_hose_recommendations.csv'
DATE_FORMAT = '%d/%m/%Y'
SUGGESTION_BUY = 'Mua'


class StockComparator:
    @staticmethod
    def compare() -> None:
        """Merge stock data with recommendations, calculate price differences, and save to a new CSV."""
        recommendations_df = pd.read_csv(RECOMMENDATIONS_FILE)
        stocks_df = pd.read_csv(STOCKS_FILE)

        # Ensure 'Price' column is numeric
        recommendations_df['Price'] = pd.to_numeric(recommendations_df['Price'], errors='coerce')

        # Merge datasets on 'Ticker' (recommendations) and 'symbol' (stocks)
        merged_df = pd.merge(recommendations_df, stocks_df, left_on='Ticker', right_on='symbol', how='left')

        # Calculate price difference and percentage change
        merged_df['Price Difference'] = merged_df['Price'] - merged_df['price']
        merged_df['Percentage Change'] = (merged_df['Price Difference'] / merged_df['price']) * 100
        merged_df['Actual Price'] = merged_df['price']

        # Rename columns for clarity
        merged_df.rename(columns={'Price': 'Target Price'}, inplace=True)

        # Select relevant columns
        final_df = merged_df[
            ['Ticker', 'Date', 'Broker', 'Suggestion', 'Actual Price', 'Target Price', 'Percentage Change']]

        # Save to CSV
        final_df.to_csv(UPDATED_RECOMMENDATIONS_FILE, index=False)
        print(final_df)

    @staticmethod
    def should_buy(top_n: int = 10) -> None:
        """Filter buy recommendations, sort by latest date and percentage change, and display top N results."""
        df = pd.read_csv(UPDATED_RECOMMENDATIONS_FILE)
        df['Date'] = pd.to_datetime(df['Date'], format=DATE_FORMAT)
        df = df[df['Suggestion'] == SUGGESTION_BUY]
        df_sorted = df.sort_values(by=['Date', 'Percentage Change'], ascending=[False, False])
        print(df_sorted.head(top_n))

    @staticmethod
    def search_for_suggestions(ticker_ids: List[str]) -> None:
        """Find the most recent recommendation for each given ticker."""
        df = pd.read_csv(UPDATED_RECOMMENDATIONS_FILE)
        df['Date'] = pd.to_datetime(df['Date'], format=DATE_FORMAT)
        filtered_df = df[df['Ticker'].isin(ticker_ids)]
        latest_ones = filtered_df.loc[filtered_df.groupby('Ticker')['Date'].idxmax()]
        print(latest_ones)
