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
    check_existing = User.query.filter(User.email == data['email']).first()
    if check_existing:
        return {"error": "Entered email already exists"}, 400
    if not data["email"]:
        return {"error": "Please provide a email"}, 400
    if not data["name"]:
        return {"error": "Please provide a your full name"}, 400
    if not data["username"]:
        return {"error": "Please provide a username"}, 400
    if not data["password"]:
        return {"error": "Please provide a password"}, 400
    if not data["confirmPassword"]:
        return {"error": "Please confirm your password"}, 400
    if data["password"] != data["confirmPassword"]:
        return {"error": "Passwords do not match"}, 400
        
    user = User(name=data["name"], username=data["username"], email=data['email'], profile_pic_url="https://elbows.s3.us-east-2.amazonaws.com/uploads/avatar.jpg", bio=data["bio"],
                password=data['password'], created_at=date.today(), updated_at=date.today())
    db.session.add(user)
    db.session.commit()
    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}


@bp.route("/users/<userId>")
def get_user_name(userId):
    # data = request.json
    user = User.query.filter(User.id == int(userId)).first()
    user_name = user.name
    return {"userName": user_name}


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

@bp.route('/userinfo/<userId>')
def get_user_information(userId):
    post_count = Post.query.filter(Post.user_id == userId).count()
    followers = Follow.query.filter(Follow.follow_user_id == userId).all()
    follows = Follow.query.filter(Follow.user_id == userId).all()
    user = User.query.filter(User.id == userId).first()
    posts = Post.query.filter(Post.user_id == userId).all()
    posts.reverse()
    
    followers_list = []
    follows_list = []
    post_list = []

    for follower in followers:
        followers_list.append(follower.to_dict())

    for follower in follows:
        follows_list.append(follower.to_dict())

    num_followers = len(followers_list)
    num_follows = len(follows_list)

    for post in posts:
        post_dict = post.to_dict()
        num_likes = Like.query.filter(Like.post_id == post_dict["id"]).count()
        num_comments = Comment.query.filter(Comment.post_id == post_dict["id"]).count()
        post_dict["like_count"] = num_likes
        post_dict["comment_count"] = num_comments
        post_list.append(post_dict)
    return {"num_posts": post_count, "posts": post_list, "followersList": followers_list, "numFollower": num_followers, "followsList": follows_list, "numFollow": num_follows, "user": user.to_dict() }


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


@bp.route("/main/<int:userId>")
def get_mainpage_post(userId):
    post_list = []
    
    follows = Follow.query.filter(Follow.user_id == userId).all()
    for follow in follows:
        posts = Post.query.filter((Post.user_id == follow.follow_user_id) | (Post.user_id == userId)).all()
        
        found_users = {}
        for post in posts:
            post_dict = post.to_dict()
            if post.user_id in found_users:
                post_dict["user_info"] = found_users[post.user_id]
            else:
                user = post.user
                found_users[post.user_id] = {"username": user.username, "profilePicUrl": user.profile_pic_url}
                post_dict["user_info"] = found_users[post.user_id]

            likes = Like.query.filter(Like.post_id == post.id).all()
            post_dict['numLikes'] = len(likes)
            likes_list = []
            for like in likes:
                likes_list.append(like.user.to_dict())
            post_dict['likesList'] = likes_list
            
            comments = post.comment
            comments_list = []
            for comment in comments:
                comment_dict = comment.to_dict()
                comment_likes = Like.query.filter(Like.comment_id == comment.id).all()
                user_list = []
                for like in comment_likes:
                    username = like.user.to_dict()
                    user_list.append(username)

                comment_dict['likes_comment'] = user_list

                if comment.user_id in found_users:
                    comment_dict["username"] = found_users[comment.user_id]
                else:
                    user = comment.user
                    found_users[user.id] = {"username": user.username, "profilePic": user.profile_pic_url}
                    comment_dict["username"] = found_users[comment.user_id]

                comments_list.append(comment_dict)

            post_dict["comments"] = { "commentsList": comments_list }

            post_list.append(post_dict)
            new_list = post_list
    return {"result": new_list}


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
        comment = Comment(user_id=data["userId"], user_name=data["userName"], post_id=data["postId"],
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
