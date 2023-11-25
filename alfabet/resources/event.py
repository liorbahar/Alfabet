

from typing import List
from flask import jsonify, request
from flask_restful import Resource, abort
from sqlalchemy import update
from sqlalchemy.orm import Query

from alfabet.database.models.event import Event, find_event_by_uuid, delete_event_by_uuid
from alfabet.database import db
from alfabet.resources.schemas.event import EventSchema
import uuid

def validate_event_exists_middleware(func):
    def wrapper(*args, **kwargs):
        event_uuid: str = kwargs.get('event_uuid')
        event: Event = find_event_by_uuid(event_uuid)
        if not event:
            abort(404, message=f"Event {event_uuid} not found")
        return func(*args, **kwargs)
    return wrapper


class EventApi(Resource):
    def post(self):
        try:
            data: dict = EventSchema().load(request.get_json())
            event = Event(location=data.get('location'),
                          venue=data.get('venue'),
                          date=str(data.get('date')),
                          uuid=str(uuid.uuid4()),
                          participants_number=data.get('participants_number'))
            db.session.add(event)
            db.session.commit()
            return jsonify(event.to_json())
        except Exception as e:
            db.session.rollback()
            return {'message': f"Failed while insert event due to: {str(e)}"}, 500

    @validate_event_exists_middleware    
    def get(self, event_uuid: str):
        event: Event = find_event_by_uuid(event_uuid) 
        return jsonify(event.to_json())
    
    @validate_event_exists_middleware
    def delete(self, event_uuid: str):
        try:
            delete_event_by_uuid(event_uuid)
            db.session.commit()
            return {'message': f"Event with uuid: {event_uuid} delete successfully"}
        except Exception as e:
            db.session.rollback()
            return {'message': f"Failed while delete specific event due to: {str(e)}"}, 500
    
    @validate_event_exists_middleware
    def put(self, event_uuid: str):
        try:
            data: dict = request.get_json()
            update_statement = update(Event).values(
                location=data.get('location'),
                venue=data.get('venue'),
                date=data.get('date'),
                participants_number=data.get('participantsNumber')
            ).where(Event.uuid == event_uuid)
            db.session.execute(update_statement)
            db.session.commit()
            event: Event = find_event_by_uuid(event_uuid)
            return jsonify(event.to_json())
        except Exception as e:
            db.session.rollback()
            return { 'message': f"Failed while delete specific event due to: {str(e)}"}, 500
    

class EventsApi(Resource):
        
    def get(self):
        location: str = request.args.get('location')
        venue: str = request.args.get('venue')
        sort_option: str = request.args.get('sortOption')

        query: Query = db.session.query(Event)
        if location:
            query = query.filter_by(location=location)

        if venue:
            query = query.filter_by(venue=venue)

        if sort_option:
            query = self.__sort_events(sort_option, query)
        
        events: List[Event] = query.all() 
        return {"events": [event.to_json() for event in events] }

    def __sort_events(self, sort_option: str,query: Query):
        if sort_option == "date":
            return query.order_by(Event.date.desc())
        elif sort_option == "participants":
            return query.order_by(Event.participants_number.desc())
        elif sort_option == "creationTime":
            return query.order_by(Event.created_at.desc())

