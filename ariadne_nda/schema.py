from marshmallow import Schema, fields, validate


class ExperimentSchema(Schema):
    min_max_message = 'must be between {min} and {max} characters'

    name = fields.String(
        attribute='name',
        required=True,
        validate=validate.Length(min=1, max=300, error=min_max_message)
    )
    description = fields.String(
        attribute='description',
        validate=validate.Length(min=1, max=600, error=min_max_message)
    )
