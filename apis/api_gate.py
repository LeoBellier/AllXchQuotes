from .api_base import Base
from ..database.cotizacion import Cotizacion

class GateApi(Base):
    def __init__(self, host: str, prefix: str, url: str):
        self.host = host
        self.prefix = prefix
        self.url = url

    def get_price(self):
        all_data = self.get_all_data()
        print(all_data)
        return Cotizacion(exchange='gate.io', precio=all_data['last'], moneda='eth', volumen=all_data['volume'])

def get_list_cotizacion():
    api_usdt = GateApi("https://data.gateapi.io/","api/1/",'ticker/xch_usdt')
    api_eth = GateApi("https://data.gateapi.io/","api/1/",'ticker/xch_eth')

    cotizaciones = [api_eth.get_price, api_usdt.get_price]
    return cotizaciones

