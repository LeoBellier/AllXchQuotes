from api_gate import get_list_quotes


def get_all():
    quotes = get_list_quotes()
    return quotes
