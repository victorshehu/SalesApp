from flask import Flask, jsonify, request


app = Flask (__name__) # Created an object of flask using a unique name

stores = [
    {
        'name': 'MyStore',
        'items':[
            {
                'name': 'MyItem',
                'price': '15.00'
            }
        ]
    }
]


#POST /store data: {name:} - creates a new store
@app.route('/store',methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

#Gets the name of the store specified
@app.route('/store/<string:name>')
def get_store(name):
    #Iterate over stores
    #if  the store name matches, return it
    #else note match return error
    found = False
    for store in stores:
        if store['name'] ==name :
           return jsonify(f'{name} was found as a store')

        return("The of the store you passed was not found")

#Gets the name of all the stores
@app.route('/store')
def get_stores():
   return jsonify({'stores': stores})

#Creates an Item in the specificed store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            
            store['items'].append(new_item)
            return jsonify(new_item)
        
        return jsonify({'message' : 'store not found'})

#Gets an Item in the specificed store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name :
                
                 return jsonify({'items': store['items']})

        return jsonify("This item was not found")

app.run(port = 5000) #port for our application to run on 