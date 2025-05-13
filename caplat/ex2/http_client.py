import httpx
from typing import Optional, Dict

class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=base_url)

    def get(self, endpoint: str, params: Optional[Dict] = None):
        response = self.client.get(endpoint, params=params)
        return response

    def post(self, endpoint: str, json: Optional[Dict] = None):
        response = self.client.post(endpoint, json=json)
        return response

    def put(self, endpoint: str, params: Optional[Dict] = None, json: Optional[Dict] = None):
        response = self.client.put(endpoint, params=params, json=json)
        return response

    def delete(self, endpoint: str, params: Optional[Dict] = None):
        response = self.client.delete(endpoint, params=params)
        return response

    def close(self):
        self.client.close()

