# This file contains request/response serializers for the blog-related data.
# It can use libraries like Marshmallow to define serializers.

from marshmallow import Schema, fields

# Define serializers for 'Post' and 'Category' models (if using Marshmallow).

class CategorySchema(Schema):
    # Define the 'Category' serializer schema here.
    id = fields.Integer()
    name = fields.String()
    verified = fields.Boolean()

class ArticleSchema(Schema):
    # Define the 'Post' serializer schema here.
    title = fields.String()
    owner_id = fields.Integer()
    content = fields.String()
    category_id = fields.Integer()
