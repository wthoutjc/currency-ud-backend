from marshmallow import Schema, fields

class CurrencySchema(Schema):
    name = fields.Str(required=True)
    code = fields.Str(required=True)