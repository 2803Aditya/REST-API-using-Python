# Import required libraries/dependencies
from flask import Flask, jsonify, request
import urllib
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import dns
from bson.json_util import dumps


# Impementation of Flask Object / Acts Cental Object
app = Flask(__name__)

# Database Name
db_name = 'FirstDB'
# MongoDB Atlas Database URI / Connection string
db_URI = 'mongodb+srv://SisodiyaAditya:'+urllib.parse.quote_plus('Siso@28adi')+'@myfirstcluster.csb3w.mongodb.net/FirstDB?retryWrites=true&w=majority'

# Configuration of Database / Connection to Database
app.config['MONGODB_NAME'] = db_name
app.config['MONGO_URI'] = db_URI

# It'll manage MongoDB connections for your Flask app.
mongo = PyMongo(app)

'''
    Sample Request Body
    {
        'name' : <Product_Name>,
        'brand_name' : <Brand_Name>,
        'regular_offer_value' : <Regular Price>,
        .
        .
        .
    }
'''

# Just for a test
@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return 'Hello World'


'''
    This API Endpoint will Render entire data from our MongoDB Collection.
'''
@app.route('/api/Products', methods = ['GET'])   # Allowed Method "GET"               
def get_data():

    data = mongo.db.Titanic    # Collection name is "Titanic"
    output = []

    for i in data.find():      # Query the database
        output.append({'Product Name' : i['name'], 'Offer Price' : i['offer_price_value']}) 

    return jsonify({'Result' : output}) # JSON serialization and this'll return a JSON response to our Browser
    

'''
    This API Endpoint will create a new object in our collection.
'''
@app.route('/api/Products/add', methods = ['POST'])     # Allowed Method "POST"
def add_data():

    create = request.json       # Access the incoming data in Flask Application

    name = create['Product Name']    # 
    brand = create['Brand Name']
    price = create['Regular Price']
    offer = create['Offer Price']
    currency = create['Currency']
    class_l1 = create['Classification_l1']
    class_l2 = create['Classification_l2']
    class_l3 = create['Classification_l3']
    class_l4 = create['Classification_l4']
    image_url = create['Image URL']

    if name and brand and price and request.method == 'POST':

        add = mongo.db.Titanic.insert({'name' : name, 'brand_name' : brand, 'regular_price_value' : price, 'offer_price_value' : offer,
                                        'currency' : currency, 'classification_l1' : class_l1, 'classification_l2' : class_l2,
                                        'classification_l3' : class_l3, 'classification_l4' : class_l4, 'image_url' : image_url})
        
        return jsonify('Object Added Successfully', 201)

    else:
        return jsonify('Operation Unsuccessful!!', 404)

@app.route('/api/Products/delete/<id>', methods = ['DELETE'])
def delete_obj(id):

    if request.method == 'DELETE':
        mongo.db.Titanic.delete_one({'_id' : ObjectId(id)})

        return jsonify('Object Deleted Successfully!', 204)

    else:
        return jsonify('Operation Unsuccessful...', 404)

@app.route('/api/Products/update/<id>', methods = ['PUT'])
def update_obj(id):

    upd = request.json
    price = upd['Regular Price']
    offer = upd['Offer Price']

    result = mongo.db.Titanic.find_one_and_update({'_id' : ObjectId(id)}, {'$set' : {'regular_price_value' : price,
                                                     'offer_price_value' : offer}})

    if result is None:
        return jsonify('Update Unsuccessful, Check id', 404)

    else:
        return jsonify('Object Successfully Updated', 201)

@app.route('/api/Products/find/<id>', methods = ["GET"])
def find_Obj(id):

    f = mongo.db.Titanic.find({'_id' : ObjectId(id)})

    if f is None:
        return jsonify("No Object Found", 404)

    return dumps(f)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5500)
