import requests


class Base:

    def __init__(self, host: str, prefix: str, url: str):
        self.host = host
        self.prefix = prefix
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.url = url

    def get_all_data(self):
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.headers)
        return r.json()
