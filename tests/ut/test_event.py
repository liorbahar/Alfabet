import unittest
from flask import Flask
from unittest.mock import patch, MagicMock

from flask_restful import Api

from alfabet.database import db
from alfabet.database.models.event import Event
from alfabet.resources.view import init_view


class TestEventApi(unittest.TestCase):
    def setUp(self):
        self.db_session_patch = patch('alfabet.resources.event.db')
        self.db_session = self.db_session_patch.start()

        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        self.api = Api(app)
        init_view(self.api)
        self.mock_app = app.test_client()

    def tearDown(self):
        self.db_session_patch.stop()

    def test_post_event(self):
        data = {'participantsNumber': 42, 'location': 'Test Location', 'venue': 'Test Venue',  'date': '2022-12-12T00:09:00Z'}

        self.db_session.return_value.add.return_value = None
        self.db_session.return_value.commit.return_value = None
        self.db_session.return_value.scalar.return_value = 1

        response = self.mock_app.post('/event', json=data)

        # Assertions
        self.assertEqual(response.status_code, 200)

    @patch('alfabet.resources.event.find_event_by_uuid')
    def test_get_event(self, find_event_by_uuid: MagicMock):
        participants_number = 42
        location = 'Test Location'
        venue = 'Test Venue'
        date = '2022-12-12T00:09:00Z'
        uuid = 'dsfdsfds'
        expected_event = Event(uuid=uuid, location=location, date=date, venue=venue, participants_number=participants_number)

        find_event_by_uuid.return_value = expected_event

        response = self.mock_app.get(f'/event/{uuid}')

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(location, response.json.get('location'))
        self.assertEqual(venue, response.json.get('venue'))
        self.assertEqual(participants_number, response.json.get('participantsNumber'))

    @patch('alfabet.resources.event.find_event_by_uuid')
    def test_put_event(self, find_event_by_uuid: MagicMock):
        participants_number = 42
        location = 'Test Location'
        new_location = 'Test Location'
        venue = 'Test Venue'
        date = '2022-12-12T00:09:00Z'
        uuid = 'dsfdsfds'
        data = {'participantsNumber': participants_number, 'location': new_location, 'venue': venue,
                'date': date}
        expected_event = Event(uuid=uuid, location=location, date=date, venue=venue,
                               participants_number=participants_number)

        find_event_by_uuid.return_value = expected_event

        response = self.mock_app.put(f'/event/{uuid}', json=data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_location, response.json.get('location'))

    @patch('alfabet.resources.event.find_event_by_uuid')
    @patch('alfabet.resources.event.delete_event_by_uuid')
    def test_delete_event(self, delete_event_by_uuid: MagicMock, find_event_by_uuid: MagicMock):
        uuid = 'dsfdsfds'

        expected_event = Event(uuid=uuid,
                               location='Test Location',
                               date='2022-12-12T00:09:00Z',
                               venue='Test Venue',
                               participants_number=42)

        find_event_by_uuid.return_value = expected_event

        delete_event_by_uuid.return_value = None
        self.db_session.return_value.commit.return_value = None

        response = self.mock_app.delete(f'/event/{uuid}')

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, { 'message': f"Event with uuid: {uuid} delete successfully"})
