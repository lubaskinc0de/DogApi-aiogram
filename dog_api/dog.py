import requests
from .exceptions import ApiError

class DogApi:

    DOG_API_URL = 'https://dog.ceo/api/breeds/image/random'

    @staticmethod
    def validate_request(request: requests.Response) -> bool:
        if request.status_code == 200:
            request_json = request.json()
            if request_json.get('status') and request_json.get('message'):
                if request_json.get('status') == 'success':
                    return True
        return False
    
    @classmethod
    def get_dog(cls):
        r_to_api = requests.get(url=cls.DOG_API_URL)
        if cls.validate_request(r_to_api):
            img_request = requests.get(url=r_to_api.json().get('message'))
            return img_request.content
        else:
            raise ApiError()
