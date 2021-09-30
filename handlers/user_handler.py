from functools import wraps
from utils import *
from flask import request, abort


def verify_user(email, password):
    return registration_verify_user(email, password)


def user_sign_out_handler(email):
    users = app.database["users"]
    query = {"email": email}
    user = users.find_one(query)
    count = len(user["days"])
    new_values = {"$set": {"days.$.signout": str(datetime.datetime.utcnow())}}
    users.update_one({"email": email, "days.id": count-1}, new_values)
    return True


def user_away_handler(email):
    users = app.database["users"]
    query = {"email": email}
    user = users.find_one(query)
    days_count = len(user["days"])
    away_count = len(user["days"][days_count - 1]["away"])
    new_values = {"$push": {"days.$.away": {"id": away_count, "begin_time": str(datetime.datetime.utcnow()), "end_time": "NULL", "duration": request.json['duration']}}}
    users.update_one({"email": email, "days.id": days_count - 1}, new_values)
    return True


def user_back_handler(email):
    users = app.database["users"]
    query = {"email": email}
    user = users.find_one(query)
    days_count = len(user["days"])
    away = user["days"][days_count - 1]["away"]
    away_count = len(away)
    away[away_count - 1]["end_time"] = str(datetime.datetime.utcnow())
    new_values = {"$set": {"days.$.away": away}}
    users.update_one({"email": email, "days.id": days_count - 1}, new_values)
    return True


def user_sign_in_handler(email):
    users = app.database["users"]
    query = {"email": email}
    user = users.find_one(query)
    days_count = len(user["days"])
    new_values = {"$push": {"days": {"id": days_count, "signin": str(datetime.datetime.utcnow()), "signout": "NULL", "away": []}}}
    users.update_one({"email": email}, new_values)
    return True

def get_user_data(email):
    users = app.database["users"]
    query = {"email": email}
    user = users.find_one(query)
    return user


def authorize_user(f):
    """
    Token verification Decorator. This decorator validate the token passed in the header with the endpoint.
    *Returns:*
        -*Error Response,401*: if the token is not given in the header, expired or invalid.
                                Or the user is not on the system.
        -*Username*:if the token is valid it allows the access and return the username of the user.
    """

    @wraps(f)  # pragma:no cover
    def decorated(*args, **kwargs):
        token = None
        user = None
        if 'TOKEN' in request.headers:
            token = request.headers['TOKEN']

        if not token:
            abort(401, 'Token is missing.')

        try:
            user = jwt.decode(token, app.secret_key, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            abort(401, 'Signature expired. Please log in again.')

        except jwt.InvalidTokenError:
            abort(401, 'Invalid token. Please log in again.')

        if not verify_user(user['email'], user['password']):
            abort(401, 'No authorized user found.')

        return f(authorized_email=user['email'], *args, **kwargs)

    return decorated
