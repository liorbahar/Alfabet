import requests

from tests.integration_tests.config import TestConfig


def create_event() -> dict:
    data = {'participantsNumber': 42, 'location': 'Test Location', 'venue': 'Test Venue',
            'date': '2022-12-12T00:09:00Z'}
    response = requests.post(url=f'{TestConfig.url}/event', json=data)
    return response.json()
