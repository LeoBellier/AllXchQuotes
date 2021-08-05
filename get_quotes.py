import api_gate
import api_huobi


def get_all():
    quotes = api_gate.get_list_quotes()
    quotes += api_huobi.get_list_quotes()
    return quotes
