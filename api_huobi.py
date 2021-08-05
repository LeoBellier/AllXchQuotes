from api_base import Base
from quote import Quote


class HuobiApi(Base):
    def __init__(self, host: str, prefix: str, url: str):
        super().__init__(host, prefix, url)

    def get_price(self):
        all_data = self.get_all_data()
        print(all_data)
        return Quote(exchange="hubio.io", price=all_data["tick"]["close"], coin=self.get_coin(), volume=all_data["tick"]["vol"])

    def get_coin(self) -> str:
        return self.url.split("xch")[1]


def get_list_quotes():
    api_usdt = HuobiApi("https://api.huobi.pro/", "market/detail/merged?symbol=", 'xchusdt')
    api_eth = HuobiApi("https://api.huobi.pro/", "market/detail/merged?symbol=", 'xchbtc')

    quotes = [api_eth.get_price(), api_usdt.get_price()]
    return quotes
