from ..apis.api_gate import get_list_cotizacion

class GetAllCotizaciones():
    def get_all(self):
        cotizaciones = get_list_cotizacion()
        return cotizaciones
        