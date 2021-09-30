import bcrypt
import app
import datetime
from datetime import timedelta
import jwt


def registration_verify_user(email, password):
    """
    verify user. password is hashed.
    investigate whether the user is on the system or not
    *Parameters:*
        - *username(string)*: holds the value of the username.
        - *password(string)*: holds the value of the password.
    *Returns:*
        -*True*: if the user is on the system.
        -*False*: if the user is not on the system.
    """
    try:
        users = app.database["users"]
        query = {"email": email}
        user = users.find_one(query)
        # User doesn't exit
        if not user:
            return False
        else:
            # Check that an un-hashed password matches one that has previously been hashed
            # if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            #     return True
            if password == user['password']:
                return True
        return False

    except:
        return False


def create_token(email, password):
    """
    Generate token.
    Encode the payload (date of expiration, username) with the secret key.
    *Parameters:*
        -*username(string)*: holds the value of the username.
        -*password(string)*: holds the value of the password.
    *Returns:*
        -*Token*:the token created.
    """
    exp = datetime.datetime.utcnow() + timedelta(days=30)
    payload = {
        'email': email,
        'password': password,
        'exp': exp
    }
    token = jwt.encode(payload, app.secret_key, algorithm='HS256')
    return token
