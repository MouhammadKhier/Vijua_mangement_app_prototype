import json

from flask import request, jsonify, make_response
from handlers import *
from utils import *

@authorize_user
def user_test():
    call_handler
    return response


def user_sign_in():
    try:
        email = request.json["email"]
        password = request.json["password"]
        if email and password:
            is_verified = verify_user(email, password)
            if is_verified:
                token = create_token(email, password)
                user_sign_in_handler(email)
                user = get_user_data(email)
                return make_response(jsonify({"success": True, "token": token, "data": {"username": user['username'], "email": user['email'], "password": user['password'], "days": user['days'] }}), 200)
            else:
                return make_response(jsonify({'success': False}), 200)
        else:
            return make_response("missing parameters", 400)
    except:
        return make_response("Server error", 500)


@authorize_user
def user_sign_out(authorized_email):
    if user_sign_out_handler(authorized_email):
        return make_response(jsonify({'success': True}), 200)
    return make_response(jsonify({'success': False}), 200)


@authorize_user
def user_away(authorized_email):
    if user_away_handler(authorized_email):
        user = get_user_data(authorized_email)
        return make_response(jsonify({'success': True, "data": {"username": user['username'], "email": user['email'], "password": user['password'], "days": user['days'] }}), 200)
    return make_response(jsonify({'success': False}), 200)


@authorize_user
def user_back(authorized_email):
    if user_back_handler(authorized_email):
        user = get_user_data(authorized_email)
        return make_response(jsonify({'success': True, "data": {"username": user['username'], "email": user['email'], "password": user['password'], "days": user['days'] }}), 200)
    return make_response(jsonify({'success': False}), 200)
