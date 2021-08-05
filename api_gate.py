from api_base import Base
from quote import Quote


class GateApi(Base):
    def __init__(self, host: str, prefix: str, url: str):
        super().__init__(host, prefix, url)

    def get_price(self):
        all_data = self.get_all_data()
        return Quote(exchange='gate.io', price=all_data['last'], coin=self.get_coin(), volume=all_data['volume'])

    def get_coin(self) -> str:
        return self.url.split("_")[1]


def get_list_quotes():
    api_usdt = GateApi("https://data.gateapi.io/", "api/1/", 'ticker/xch_usdt')
    api_eth = GateApi("https://data.gateapi.io/", "api/1/", 'ticker/xch_eth')

    quotes = [api_eth.get_price(), api_usdt.get_price()]
    return quotes
