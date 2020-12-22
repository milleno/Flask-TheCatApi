import requests
import json


class CatApi:
    def __init__(self):
        self.url = 'https://api.thecatapi.com/v1/'
        self.api_key = '66839f69-23c8-44ed-a56b-4a6dbf57a872'
        self.user_id = 'ufmnaa'

    def get_breeds(self):
        url = self.url + 'breeds'
        r = requests.get(url, headers={'x-api-key': self.api_key})
        breeds = r.json()
        return breeds

    def get_breed_img(self, id):
        url = self.url + 'images/search'
        query_params = {
            'breed_id': id,
            'limit': 3
        }
        r = requests.get(url, headers={'x-api-key': self.api_key}, params=query_params)
        breed = r.json()
        return breed
