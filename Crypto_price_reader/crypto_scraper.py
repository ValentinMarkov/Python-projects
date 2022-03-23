import requests

api_key = 'pk_e2179c5d0a894d499eec1c8dc4cc2cca'


class CryptoCurrency:
    base_url = "https://cloud.iexapis.com/stable/crypto"

    def __init__(self, symbol):
        self.symbol = symbol

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/price?token={api_key}"

    @property
    def price(self):
        req = requests.get(self.complete_url).json()  # This method convert JSON data to Python dictionary
        return float(req.get('price'))
