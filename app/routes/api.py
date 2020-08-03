from flask import Blueprint, request, jsonify
from datetime import date
from sqlalchemy import func
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
                password=data['password'], created_at=func.now(), updated_at=func.now())
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


@bp.route("/users/search")
def get_all_user_information():
    users = User.query.all()
    user_list = []
    for user in users:
        user_dict = user.to_dict()
        user_list.append(user_dict)
    return {"search": user_list}


@bp.route("/user/search/<username>")
def get_user_id(username):
    user = User.query.filter(User.username == username).first()
    return {"userId": user.id}


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


@bp.route("/users/update/<int:userId>", methods=['POST'])
def update_user(userId):
    data = request.json
    user = User.query.filter(User.id == userId).first()
    # old_user = user.to_dict()
    if data["newProfilePicUrl"]:
        if user.profile_pic_url != data["newProfilePicUrl"]:
            user.profile_pic_url = data["newProfilePicUrl"]
    if data["newFullName"]:
        if user.name != data["newFullName"]:
            user.name = data["newFullName"]
    if data["newUserName"]:
        if user.username != data["newUserName"]:
            user.username = data["newUserName"]
    if data["newBio"]:
        if user.bio != data["newBio"]:
            user.bio = data["newBio"]
    db.session.commit()
    return {"result": "User information updated successfully!"}
    

@bp.route('/userinfo/<int:userId>')
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

    for follow in follows:
        follows_list.append(follow.to_dict())

    num_followers = len(followers_list)
    num_follows = len(follows_list)

    for post in posts:
        post_dict = post.to_dict()
        num_likes = Like.query.filter(Like.post_id == post_dict["id"]).count()
        num_comments = Comment.query.filter(Comment.post_id == post_dict["id"]).count()
        post_dict["numLikes"] = num_likes
        post_dict["comment_count"] = num_comments
        post_dict["profilePic"] = user.profile_pic_url
        post_list.append(post_dict)
    return {"num_posts": post_count, "posts": post_list, "followersList": followers_list, "numFollower": num_followers, "followsList": follows_list, "numFollow": num_follows, "user": user.to_dict() }


@bp.route("/notification/<int:userId>")
def get_user_notification(userId):
    follows_list = []
    likes_list = []
    comments_list = []

    user = User.query.filter(User.id == userId).first()
    user_post_ids = list(map(lambda post: post.id, user.post))
    user_comment_ids = list(map(lambda comment: comment.id, user.comment))

    follows = Follow.query.filter(Follow.follow_user_id == userId).order_by(Follow.created_at.desc()).all()

    for follow in follows:
        follows_dict = follow.to_dict()
        user = follow.user.to_dict()
        follows_dict['user'] = user
        follows_dict['type'] = 'follow'
        follows_dict['created_at'] = follow.created_at
        follows_list.append(follows_dict)

    likes = Like.query.filter(Like.post_id.in_(user_post_ids)).order_by(Like.created_at.desc()).all()

    for like in likes:
        like_dict = {}
        user = like.user.to_dict()
        post = like.post.to_dict()
        like_dict['user'] = user
        like_dict['post'] = post
        like_dict['type'] = 'like'
        like_dict['created_at'] = like.created_at
        likes_list.append(like_dict)

    comments = Comment.query.filter(Comment.post_id.in_(user_post_ids)).order_by(Comment.created_at.desc()).all()

    for comment in comments:
        comment_dict = {}
        user = comment.user.to_dict()
        post = comment.post.to_dict()
        comment_dict['user'] = user
        comment_dict['post'] = post
        comment_dict['type'] = 'comment'
        comment_dict['created_at'] = comment.created_at
        comments_list.append(comment_dict)

    notification_list = follows_list + likes_list + comments_list
    
    sorted_note_list = sorted(notification_list, key=lambda notification_list: notification_list['created_at'])
    sorted_note_list.reverse()

    return {"notifications": sorted_note_list}


# Post routes
@bp.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    try:
        post = Post(user_id=data["userId"], location=data["location"], post_image=data["postImage"],
                    post_body=data["postBody"], created_at=func.now(), updated_at=func.now())
        db.session.add(post)
        db.session.commit()
        return jsonify({"post": "post created"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/posts/delete/<int:postId>")
def delete_post(postId):
    try:
        post_to_delete = Post.query.filter(Post.id == postId).first()
        comments_to_delete = Comment.query.filter(Comment.post_id == postId).all()
        for comment in comments_to_delete:
            db.session.delete(comment)
        db.session.delete(post_to_delete)
        db.session.commit()
        return jsonify({"delete": "delete success"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/main/<int:userId>")
def get_mainpage_post(userId):
    post_list = []
    
    follows = Follow.query.filter(Follow.user_id == userId).all()
    for follow in follows:
        posts = Post.query.filter(Post.user_id == follow.follow_user_id).all()
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
            check_user_liked = False
            for like in likes:
                if like.user_id == userId:
                    check_user_liked = True
                else:
                    check_user_liked = False
                likes_list.append(like.user.to_dict())
            post_dict['likesList'] = likes_list
            post_dict['check_user_liked'] = check_user_liked
            
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
                    found_users[user.id] = {"username": user.username, "profilePicUrl": user.profile_pic_url}
                    comment_dict["username"] = found_users[comment.user_id]

                comments_list.append(comment_dict)

            post_dict["comments"] = { "commentsList": comments_list }

            post_list.append(post_dict)
    return {"result": post_list}


@bp.route("/posts/info/<int:userId>/<int:postId>")
def get_post_information(userId, postId):
    post = Post.query.filter(Post.id == postId).first()
    post_dict = post.to_dict()
    post_dict["user"] = post.user.to_dict()
    comments = post.comment
    comments_list = []

    for comment in comments:
        comment_dict = comment.to_dict()
        comment_likes = Like.query.filter(Like.comment_id == comment.id).all()
        user_list = []
        for like in comment_likes:
            user = like.user.to_dict()
            user_list.append(user)
        comment_dict['likes_comment'] = user_list
        user = comment.user
        comment_dict["username"] = user.to_dict()
        comments_list.append(comment_dict)

    likes = Like.query.filter(Like.post_id == postId).all()
    user_list = []
    check_user_liked = False
    for like in likes:
        if like.user_id == userId:
            check_user_liked = True
        else:
            check_user_liked = False
        post_dict['check_user_liked'] = check_user_liked
        user = like.user.to_dict()
        user_list.append(user)
    
    return {"post": post_dict, "comments": comments_list, "likes": user_list}


@bp.route("/posts/<int:userId>")
def get_user_post(userId):
    try:
        fetched_posts = Post.query.filter(Post.user_id == userId).all()
        posts = [post.to_dict() for post in fetched_posts]
        return jsonify({"posts": posts})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/posts/favorites/<int:userId>")
def get_liked_posts(userId):
    post_list = []
    try:
        liked_posts = Like.query.filter(Like.user_id == userId).all()
        for liked_post in liked_posts:
            post = Post.query.filter(Post.id == liked_post.post_id).first()
            post_list.append(post.to_dict())
        # posts = [post.to_dict() for post in liked_posts]
        return jsonify({"posts": post_list})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/posts")
def get_all_posts():
    posts = Post.query.all()
    posts_list = []
    for post in posts:
        creator = User.query.filter(User.id == post.user_id).first()
        post_dict = post.to_dict()
        post_dict["creator"] = creator.to_dict()["username"]
        num_likes = Like.query.filter(Like.post_id == post_dict["id"]).count()
        num_comments = Comment.query.filter(Comment.post_id == post_dict["id"]).count()
        post_dict["numLikes"] = num_likes
        post_dict["numComments"] = num_comments
        posts_list.append(post_dict)
    return {"posts": posts_list}


# Comment routes
@bp.route("/comments", methods=["POST"])
def create_comment():
    data = request.json
    try:
        comment = Comment(user_id=data["userId"], user_name=data["userName"], post_id=data["postId"],
                          comment_body=data["commentBody"], created_at=func.now(), updated_at=func.now())
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
@bp.route("/createlike/<int:userId>", methods=["POST"])
def create_like(userId):
    data = request.json
    try:
        if data["postId"]:
            post_likes = Like.query.filter(Like.post_id == data["postId"]).all()
            for post_like in post_likes:
                if(post_like.user_id == userId):
                    return jsonify({"result": "already liked"}), 400

        like = Like(
            user_id=userId, post_id=data["postId"], comment_id=data["commentId"], created_at=func.now(), updated_at=func.now())
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
    check_follow = Follow.query.filter(Follow.user_id == data['userId']).filter(Follow.follow_user_id == data['followUserId']).first()
    if check_follow:
        return {"error": "Already following!"}, 400
    try:
        follow = Follow(user_id=data["userId"],
                        follow_user_id=data["followUserId"], created_at=func.now(), updated_at=func.now())
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
