import http.client as http

class Client:
    def __init__(self, url):
        self.connection = http.HTTPConnection(url, 443, 10)