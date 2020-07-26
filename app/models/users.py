from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from sqlalchemy.orm import validates


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    profile_pic_url = db.Column(db.String(200))
    bio = db.Column(db.String(1000))
    hashed_password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(
        timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    post = db.relationship("Post", back_populates="user")
    comment = db.relationship("Comment", back_populates="user")
    follow = db.relationship("Follow", back_populates="user")
    like = db.relationship("Like", back_populates="user")
    # saved = db.relationship("Saved_Post", back_populates="user")
    # messages = db.relationship("Message", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "profilePicUrl": self.profile_pic_url,
            "bio": self.bio,
            "createdAt": self.created_at,
        }
