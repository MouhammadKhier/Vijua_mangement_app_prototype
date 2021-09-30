from controllers.user_controller import *
import app

user_url_prefix = '/user'


def add_user_routes():
    # POST requests
    app.app.add_url_rule(user_url_prefix + "/signin", view_func=user_sign_in, methods=["POST"])
    app.app.add_url_rule(user_url_prefix + "/signout", view_func=user_sign_out, methods=["POST"])
    app.app.add_url_rule(user_url_prefix + "/away", view_func=user_away, methods=["POST"])
    app.app.add_url_rule(user_url_prefix + "/back", view_func=user_back, methods=["POST"])
    app.app.add_url_rule(user_url_prefix + "/test", view_func=user_test, methods=["POST"])
