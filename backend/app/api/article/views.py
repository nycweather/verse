# This file defines the API endpoints for blog-related operations.
# It uses Flask's Blueprint to create the 'blog' API endpoints.

from flask import Blueprint, jsonify, request

from app.utils.http_constants import HTTP_CODES
from app.api.article.models import Article
from app.database.db import db
from app.api.article.serializers import ArticleSchema

# Create a Blueprint for 'blog' API endpoints.
article_bp = Blueprint('article', __name__)

# Define API endpoints here (e.g., CRUD for blog articles).

@article_bp.get('/<int:id>')
def article(id):
    if request.method == 'GET':
        article = Article.query.filter_by(id=id).first()
        if article:
            return jsonify({'message': 'article found!', 'article': article.serialize()}), HTTP_CODES.HTTP_200_OK
        else:
            return jsonify({'message': 'article not found!'}), HTTP_CODES.HTTP_404_NOT_FOUND

@article_bp.route('/', methods=['POST'])
def get_all_articles():
    if request.method == 'POST':
        title=request.json['title']
        content=request.json['content']
        owner_id=int(request.json['owner_id'])
        category_id = int(request.json['category_id'])
        errors = ArticleSchema().validate(request.json)
        if errors:
            return jsonify({'message': 'Validation errors', 'errors': errors}), HTTP_CODES.HTTP_400_BAD_REQUEST
        article = Article(title=title, content=content, owner_id=owner_id, category_id=category_id)
        db.session.add(article)
        db.session.commit()
        return jsonify({'message': "Article created"}), HTTP_CODES.HTTP_201_CREATED
    

@article_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
def update_article(id):
    if request.method == 'PUT':
        article = Article.query.filter_by(id=id).first()
        if article:
            article.title = request.json['title']
            article.content = request.json['content']
            article.category_id = int(request.json['category_id'])
            db.session.commit()
            return jsonify({'message': 'Article updated successfully!'}), HTTP_CODES.HTTP_200_OK
        else:
            return jsonify({'message': 'Article not found!'}), HTTP_CODES.HTTP_404_NOT_FOUND
    elif request.method == 'DELETE':
        article = Article.query.filter_by(id=id).first()
        if article:
            db.session.delete(article)
            db.session.commit()
            return jsonify({'message': 'Article deleted successfully!'}), HTTP_CODES.HTTP_200_OK
        else:
            return jsonify({'message': 'Article not found!'}), HTTP_CODES.HTTP_404_NOT_FOUND
