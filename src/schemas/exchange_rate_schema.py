from marshmallow import Schema, fields

class ExchangeRateSchema(Schema):
    from_currency_id = fields.Int(required=True)
    to_currency_id = fields.Int(required=True)
    rate = fields.Float(required=True)

class ConvertSchema(Schema):
    from_currency_id = fields.Int(required=True)
    to_currency_ids = fields.List(fields.Int(), required=True)
    amount = fields.Float(required=True)