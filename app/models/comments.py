from . import db
from sqlalchemy import func


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    comment_body = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user = db.relationship("User", back_populates="comment")
    post = db.relationship("Post", back_populates="comment")
    like = db.relationship("Like", back_populates="comment")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "postId": self.post_id,
            "commentBody": self.comment_body,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
