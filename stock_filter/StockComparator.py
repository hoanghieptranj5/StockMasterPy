import pandas as pd


class StockComparator:
    def __init__(self):
        pass

    @staticmethod
    def compare():
        recommendations_df = pd.read_csv('resources/hose_recommendations.csv')
        stocks_df = pd.read_csv('resources/hose_stocks.csv')

        # Ensure the 'price' column in recommendations is numeric
        recommendations_df['Price'] = pd.to_numeric(recommendations_df['Price'], errors='coerce')

        # Merge the two DataFrames on the Ticker and symbol
        merged_df = pd.merge(recommendations_df, stocks_df, left_on='Ticker', right_on='symbol', how='left')

        # Calculate the difference and percentage change between recommendation price and current price
        merged_df['Price Difference'] = merged_df['Price'] - merged_df['price']
        merged_df['Percentage Change'] = (merged_df['Price Difference'] / merged_df['price']) * 100

        # Add two new columns to the original dataset: 'Actual Price' and 'Percentage Change'
        merged_df['Actual Price'] = merged_df['price']
        merged_df['Percentage Change'] = merged_df['Percentage Change']
        merged_df['Target Price'] = merged_df['Price']

        # Select relevant columns to keep
        final_df = merged_df[
            ['Ticker', 'Date', 'Broker', 'Suggestion', 'Actual Price', 'Target Price', 'Percentage Change']]

        # Save the final dataset to a new CSV file
        final_df.to_csv('resources/updated_hose_recommendations.csv', index=False)
        print(final_df)

    @staticmethod
    def should_buy():
        df = pd.read_csv('resources/updated_hose_recommendations.csv')
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
        df = df[df['Suggestion'] == 'Mua']
        df_sorted = df.sort_values(by=['Date', 'Percentage Change'], ascending=False)
        print(df_sorted.head(10))
