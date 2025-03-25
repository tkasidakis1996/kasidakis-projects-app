from marshmallow import Schema, fields

class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    technologies_used = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

class ProjectListSchema(Schema):
    projects = fields.List(fields.Nested(ProjectSchema))
