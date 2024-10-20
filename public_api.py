from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Define Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

# Define Post schema
class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'image_link', 'publisher')

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
