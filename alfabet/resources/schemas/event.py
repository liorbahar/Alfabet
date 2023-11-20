from marshmallow import Schema, fields
import datetime

class EventSchema(Schema):
    location = fields.String(required=True)
    date = fields.String(required=True)
    venue = fields.String(required=True)
    participants_number = fields.Integer(data_key="participantsNumber",required=True)

    def post_load(self, data, **kwargs):
        data['date'] = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%SZ")
        return data
