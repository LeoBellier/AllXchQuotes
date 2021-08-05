from api_base import Base
from quote import Quotes


class GateApi(Base):
    def __init__(self, host: str, prefix: str, url: str):
        super().__init__(host, prefix, url)

    def get_price(self):
        all_data = self.get_all_data()
        print(all_data)
        return Quotes(exchange='gate.io', price=all_data['last'], coin='eth', volume=all_data['volume'])


def get_list_quotes():
    api_usdt = GateApi("https://data.gateapi.io/", "api/1/", 'ticker/xch_usdt')
    api_eth = GateApi("https://data.gateapi.io/", "api/1/", 'ticker/xch_eth')

    quotes = [api_eth.get_price(), api_usdt.get_price()]
    return quotes
