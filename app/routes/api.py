from flask import BluePrint, request, jsonify
import jwt

from ..config import Configuration

bp = BluePrint("api", __name__, url_prefix="/api")


@bp.route("/users", methods=["POST"])
def signup_user():
    data = request.json
    user = User(first_name=data["firstName"], last_name=data["lastName"],
                email=data['email'], password=data['password'])
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
