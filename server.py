import pymongo
from pymongo import MongoClient
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields
from flask_sqlalchemy import SQLAlchemy

# --- Creating Flask API
app = Flask(__name__)
api = Api(app)

# --- SQLAlchemy DB Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
db_s = SQLAlchemy(app)

# --- Mongo DB Connection
connection = "mongodb://127.0.0.1:27017"
client = MongoClient(connection)
db_m = client["myRetail"]
collection = db_m["pricing"]

# --- Creating MovieModel class used with SQLAlchemy to query and update DB
class MovieModel(db_s.Model):
	id = db_s.Column(db_s.Integer, primary_key=True)
	name = db_s.Column(db_s.String, nullable=False)
	video_type = db_s.Column(db_s.String, nullable=False)

class Products(Resource):
	# --- GET Request
	def get(self, movie_id):
		products_result = MovieModel.query.filter_by(id=movie_id).first()
		if not products_result:
			abort(404, message="Movie not found")
		mongo_result = collection.find({"_id":movie_id})
		if not mongo_result:
			abort(404, message="Movie not found")
		for pricing_result in mongo_result:
			priceV = pricing_result["value"]
			priceC = pricing_result["currency"]
		final_result = {"id":products_result.id, 
						"name":products_result.name,
						"video_type":products_result.video_type,
						"value":priceV,
						"currency":priceC
						}
		return final_result

	# --- PUT Request
	def put(self, movie_id):
		# --- Parsing input from PUT requests
		video_put_args = reqparse.RequestParser()
		video_put_args.add_argument("id", type=int)
		video_put_args.add_argument("name", type=str)
		video_put_args.add_argument("video_type", type=str)
		video_put_args.add_argument("value", type=float)
		video_put_args.add_argument("currency", type=str)

		args = video_put_args.parse_args()
		products_result = MovieModel.query.filter_by(id=movie_id).first()
		if not products_result:
			abort(404, message="Movie not found")
		mongo_result = collection.find({"_id":movie_id})
		if not mongo_result:
			abort(404, message="Movie not found")

		#Uncomment the code below to update any of the attributes in either database.
		#products_result.id = args['id']
		#products_result.name = args['name']
		#products_result.video_type = args['video_type']
		#db_s.session.commit()
		#collection.update_one({"_id":movie_id}, {"$set":{"currency":args['currency']}})

		collection.update_one({"_id":movie_id}, {"$set":{"value":args['value']}})
		
		mongo_result = collection.find({"_id":movie_id})
		for pricing_result in mongo_result:
			priceV = pricing_result["value"]
			priceC = pricing_result["currency"]
		final_result = {"id":products_result.id, 
						"name":products_result.name,
						"video_type":products_result.video_type,
						"value":priceV,
						"currency":priceC
						}
		return final_result, 201


api.add_resource(Products, "/products/<int:movie_id>")

if __name__ == "__main__":
	app.run(debug=True)