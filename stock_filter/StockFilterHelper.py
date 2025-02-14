class StockFilterHelper:
    def __init__(self):
        pass

    @staticmethod
    def get_page(ticker: str) -> str:
        return f'https://dstock.vndirect.com.vn/tong-quan/{ticker}/quan-diem-cac-cong-ty-ck-popup'

