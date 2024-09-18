import requests
import json


class ApiService:
    @staticmethod
    def get_cat_facts():
        response = requests.get('https://catfact.ninja/fact')
        return json.loads(response.content.decode()) if response.status_code == 200 else None

    @staticmethod
    def get_random_joke():
        response = requests.get(
            'https://official-joke-api.appspot.com/jokes/random')
        return json.loads(response.content.decode()) if response.status_code == 200 else None

    @staticmethod
    def request_to_api():
        return ApiService.get_cat_facts(), ApiService.get_random_joke()
