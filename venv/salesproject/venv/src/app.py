from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required


from security import identity, authenticate

app = Flask (__name__)
app.secret_key = 'test'
api = Api(app)

jwt = JWT(app , authenticate , identity)

items = []

class Item(Resource): # inheritance of the Resource class
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items ), None)
        return { 'item': item}, 200 if item  else 404  #Not Found status code


    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items) , None):
            return {'message' : "An item with name '{}' already exists.".format(name)}, 400


        request_data = request.get_json()
        item = {'name': name , 'price': request_data['price']}
        items.append(item)
        return item , 201 #Created status code

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message' : 'Item deleted'}

    def put (self, name):
        data = request.get_json()
        item = list(filter(lambda x: x['name'] != name, items), None)
        if item is None:
            item = {'name' : name , 'price': data['price']}
            items.append(item)
        
        else:
            item.update(data)

        return {'item' : item }

class ItemList(Resource):
    def get(self):
        return {'items': items}



api.add_resource(Item, '/item/<string:name>') # replacement for the route app@route decorator
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)