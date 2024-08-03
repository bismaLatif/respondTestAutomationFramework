import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response

    def login(self, email, password):
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }
        payload = {
            "email": email,
            "password": password
        }
        response = self.post('/auth/login', json=payload, headers=headers)
        return response


