from . import db
from sqlalchemy import func


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location = db.Column(db.String(50))
    post_image = db.Column(db.String(200), nullable=False)
    post_body = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user = db.relationship("User", back_populates="post")
    comment = db.relationship("Comment", back_populates="post")
    like = db.relationship("Like", back_populates="post")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "location": self.location,
            "postImage": self.post_image,
            "postBody": self.post_body,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
