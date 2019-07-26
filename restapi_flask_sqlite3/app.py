from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, GetItem

app = Flask(__name__)
app.secret_key = 'ramki'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# items = [] #in memory database
# using sqlite3 to store the data

api.add_resource(Item, '/item/<string:name>')
api.add_resource(GetItem, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
