# myRetail

## Python Requirements
Flask==1.1.2
Flask_RESTful==0.3.8
Flask_SQLAlchemy==2.4.3
pymongo==4.1.1
requests==2.28.1

## Run Requirements
You need to create a local SQLAlchemy DB and MongoDB in order to run this program.
I used the local_SQLAlchemyDB.py and local_MongoDB.py files to generate the DBs.
Make sure that the local MongoDB and server.py are running in separate command prompts.
Run rest.py and follow the on-screen prompts.

## Exercise Prompt
Your goal is to create a RESTful service that can retrieve product and price details by ID. The URL structure is up to you to define, but try to follow some sort of logical convention.
Build an application that performs the following actions: 
Responds to an HTTP GET request at /products/{id} and delivers product data as JSON (where {id} will be a number. 
Example product IDs: 13860428, 54456119, 13264003, 12954218) 
Example response: {"id":13860428,"name":"The Big Lebowski (Blu-ray) (Widescreen)","current_price":{"value": 13.49,"currency_code":"USD"}}
Performs an HTTP GET to retrieve the product name from an external API. (For this exercise the data will come from redsky.target.com, but let’s just pretend this is an internal resource hosted by myRetail) 
Example: 
https://redsky-uat.perf.target.com/redsky_aggregations/v1/redsky/case_study_v1?key=3yUxt7WltYG7MFKPp7uyELi1K40ad2ys&tcin=13860428
Reads pricing information from a NoSQL data store and combines it with the product id and name from the HTTP request into a single response.  
BONUS: Accepts an HTTP PUT request at the same path (/products/{id}), containing a JSON request body similar to the GET response, and updates the product’s price in the data store. 

## Example Inputs
Option 1
13860428
54456119
13264003
12954218
35645454

Option 2
{'id': 12954218, 'name': 'Gone with the Wind', 'video_type': 'DVD', 'value': 10.15, 'currency': 'USD'}
{'id': 13264003, 'name': 'Casablanca', 'video_type': 'DVD', 'value': 20.25, 'currency': 'USD'}
{'id': 13860428, 'name': 'The Big Lebowski', 'video_type': 'Blu-Ray', 'value': 13.49, 'currency': 'USD'}
{'id': 35645454, 'name': 'Pacific Rim', 'video_type': 'Blu-Ray', 'value': 59.99, 'currency': 'USD'}
{'id': 54456119, 'name': 'The Shawshank Redemption', 'video_type': 'DVD', 'value': 60.22, 'currency': 'USD'}
