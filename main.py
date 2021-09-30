import app
import click
import pymongo
import datetime


@click.command()
@click.option('--env', default='dev')
def cli(env):
    app.run(env=env)


def test():
    client = pymongo.MongoClient("mongodb+srv://Prototype:123456789123456789@prototype.38psx.mongodb.net/Prototype?retryWrites=true&w=majority")
    database = client["Prototype"]
    users = database['users']
    # user = users.find_one({"username": "admin"})
    # update values
    # newValues = {"$set": {"email": "eissapk44@gmail.com", "days": [{"id": 0, "signin": str(datetime.datetime.utcnow()), "signout": str(datetime.datetime.utcnow()), "away":[{"begin_time": str(datetime.datetime.utcnow()), "end_time": str(datetime.datetime.utcnow()), "duration": 5}]}]}}
    # users.update_one({"username": "admin"}, newValues)
    # push to array
    # newValues = {"$push": {"away": {"begin_time": str(datetime.datetime.utcnow()), "end_time": str(datetime.datetime.utcnow()), "duration": 5}}}
    # update array inside array
    # newValues = {"$push": {"days.$.away": {"begin_time": str(datetime.datetime.utcnow()), "end_time": str(datetime.datetime.utcnow()), "duration": 5}}}
    # users.update_one({"username": "admin", "days.id": 0}, newValues)
    users.insert_one({"username": "Mohamad","email": "eng.mhd.sh@gmail.com", "password": "admin", "days": []})
    # users.update_one({"username": "admin"})
    #print(str(datetime.datetime.utcnow()))


if __name__ == '__main__':
    test()
