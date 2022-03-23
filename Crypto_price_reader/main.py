from crypto_scraper import CryptoCurrency


if __name__ == '__main__':
    symbol_1 = CryptoCurrency(symbol='btcusd')
    print(symbol_1.price)
