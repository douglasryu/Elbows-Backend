from . import db
from sqlalchemy import func


class Follow(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    follow_user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user = db.relationship("User", back_populates="follow")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "followUserId": self.follow_user_id,
        }
