import requests
from requests import Response

from tests.integration_tests.config import TestConfig
from tests.integration_tests.event_helper import create_event


class TestEvent:
    def test_create_event(self):
        data = {'participantsNumber': 42, 'location': 'Test Location', 'venue': 'Test Venue',  'date': '2022-12-12T00:09:00Z'}
        response: Response = requests.post(url=f'{TestConfig.url}/event', json=data)

        assert response.status_code == 200

    def test_get_event(self):
        event: dict = create_event()
        event_id = event.get('id')
        response: Response = requests.get(url=f'{TestConfig.url}/event/{event_id}')

        assert response.status_code == 200
        assert response.json().get('id') == event_id

    def test_delete_event(self):
        event: dict = create_event()
        event_id = event.get('id')
        delete_response: Response = requests.delete(url=f'{TestConfig.url}/event/{event_id}')

        get_response: Response = requests.get(url=f'{TestConfig.url}/event/{event_id}')

        assert delete_response.status_code == 200
        assert delete_response.json() == {'message': f"Event with uuid: {event_id} delete successfully"}
        assert get_response.status_code == 404

    def test_put_event(self):
        event: dict = create_event()
        data = {'participantsNumber': 42, 'location': 'new Test Location', 'venue': 'Test Venue',
                'date': '2022-12-12T00:09:00Z'}
        event_id = event.get('id')

        response: Response = requests.put(url=f'{TestConfig.url}/event/{event_id}', json=data)

        assert response.status_code == 200
        assert event.get('location') == 'Test Location'
        assert response.json().get('location') == 'new Test Location'
