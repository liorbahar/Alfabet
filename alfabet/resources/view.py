
from flask_restful import Api
from alfabet.resources.event import EventApi, EventsApi

def init_view(api: Api):
    api.add_resource(EventApi, '/event', '/event/<event_uuid>')
    api.add_resource(EventsApi, '/events')
    