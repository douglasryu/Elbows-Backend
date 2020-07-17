from flask import Blueprint, request, jsonify
from datetime import date
import jwt

from ..models import db
from ..models.users import User
from ..models.posts import Post
from ..models.comments import Comment
from ..models.likes import Like
from ..models.follows import Follow

from ..config import Configuration


bp = Blueprint("api", __name__, url_prefix="/api")


# User routes
@bp.route("/users", methods=["POST"])
def signup_user():
    data = request.json
    user = User(name=data["name"], username=data["userName"], email=data['email'], bio=data["bio"],
                password=data['password'], created_at=date.today(), updated_at=date.today())
    db.session.add(user)
    db.session.commit()
    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}


@bp.route("/users/session", methods=['POST'])
def signin_user():
    data = request.json
    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return {"error": "Email not found"}, 422
    if user.check_password(data['password']):
        access_token = jwt.encode(
            {'email': user.email}, Configuration.SECRET_KEY)
        return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}
    else:
        return {"error": "Incorrect password"}, 401


# Post routes
@bp.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    try:
        post = Post(user_id=data["userId"], location=data["location"], post_image=data["postImage"],
                    post_body=data["postBody"], created_at=date.today(), updated_at=date.today())
        db.session.add(post)
        db.session.commit()
        return jsonify({"post": "post created"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/posts/<int:userId>")
def get_user_post(userId):
    try:
        fetched_posts = Post.query.filter(Post.user_id == userId).all()
        posts = [post.to_dict() for post in fetched_posts]
        return jsonify({"posts": posts})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


# @bp.route("/posts/<int:userId>")
# def get_followee_posts():
#     follows = Follow.query.filter(Follow.user_id == userId).all()
#     followee_list = [follow.follow_user_id for follow in follows]

#     for followee_id in followee_list:
#         followee_posts = Post.query.filter(Post.user_id == followee).all()


# Comment routes
@bp.route("/comments", methods=["POST"])
def create_comment():
    data = request.json
    try:
        comment = Comment(user_id=data["userId"], post_id=data["postId"],
                          comment_body=data["commentBody"], created_at=date.today(), updated_at=date.today())
        db.session.add(comment)
        db.session.commit()
        return jsonify({"comment": "comment created"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/comments/<int:postId>")
def get_comment(postId):
    try:
        fetched_comments = Comment.query.filter(
            Comment.post_id == postId).all()
        comments = [comment.to_dict() for comment in fetched_comments]
        return jsonify({"comments": comments})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


# Like routes
@bp.route("/likes", methods=["POST"])
def create_like():
    data = request.json
    try:
        like = Like(
            user_id=data["userId"], post_id=data["postId"], comment_id=data["commentId"])
        db.session.add(like)
        db.session.commit()
        return jsonify({"like": "like created"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/likes/<int:postId>")
def get_post_like(postId):
    try:
        fetched_likes = Like.query.filter(Like.post_id == postId).all()
        likes = [like.to_dict() for like in fetched_likes]
        return jsonify({"postLikes": likes})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/likes/<int:commentId>")
def get_comment_like(commentId):
    try:
        fetched_likes = Like.query.filter(Like.comment_id == commentId).all()
        likes = [like.to_dict() for like in fetched_likes]
        return jsonify({"commentLikes": likes})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


# Follow routes
@bp.route("/follows", methods=["POST"])
def create_follow():
    data = request.json
    try:
        follow = Follow(user_id=data["userId"],
                        follow_user_id=data["followUserId"])
        db.session.add(follow)
        db.session.commit()
        return jsonify({"follow": "follow created"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/follows/<int:userId>")
def get_follow(userId):
    try:
        fetched_follows = Follow.query.filter(Follow.user_id == userId).all()
        follows = [follow.to_dict() for follow in fetched_follows]
        return jsonify({"follows": follows})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400
