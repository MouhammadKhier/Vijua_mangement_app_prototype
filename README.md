# README
## Vijua_mangement_app_prototype

### about the project

this project is a prototype that solve a problem we are facing in our company "Vijua" while working online.
we agreed on a protocol that each one should mention its status (signed in, signed out, away, ...etc) in a group that all the company employess are participated in, the problem with this was to follow up with each one status, and also can't keep track how money hours each employee spent working.
so our applicatoin can provide customized fucntionality that provide this status in one click away for each user, and also keep track in the database each user sign in, sign out and away time, also keep track how many hours each user spent working.

Sure this is just a prototype and provide very tiny part of it could be capable of in the future, like making privilaged account for the owner and HR in the company so they can be provided with states and charts about each user activities and commitment.
Also it can be chat, call and video app just for this company so all members can communicate with each other, organize meets and a lot more.

### about the project technical side

We used flask (a python web framework) to manage and control the endpoints and the coming requests, the framework has no database abstaction layer so we used our own, pymongo was the library we used to connect our code to cloud hosted mongodb database on atlas using a connection URI provided by atlas.
Also we use some auxialary libraries (like JWT for encoding and decoding).

### project structure

the main three folders are (routes, controllers and handler).
each collection in the database should have file in each folder (for more structured code) so flask framework can serve the requests that will interact with this collection.

### project flow

As the main function runs it will invoke the run function that flask provide to make the server up and running.
To make flask able to serve the requests it should be provides with lists of endpoints with each controller that will handle this endpoint.
```python
def add_user_routes():
    # POST requests
    app.app.add_url_rule(user_url_prefix + "/signin", view_func=user_sign_in, methods=["POST"])
    app.app.add_url_rule(user_url_prefix + "/signout", view_func=user_sign_out, methods=["POST"])
    app.app.add_url_rule(user_url_prefix + "/away", view_func=user_away, methods=["POST"])
    app.app.add_url_rule(user_url_prefix + "/back", view_func=user_back, methods=["POST"])
```
In the previous block of code this function provides list of endpoints to flask with the type and controller function of each one.

As for the controller function it is responsible for calling the handler of its endpoint and return a request (success or fail) based on the handler result.
And for handler it does what the endpoint responsible for (e.g. interacting with database to change some value or add a new one).
