import requests
import json
connection = "http://127.0.0.1:5000/"

choice = input("Please choose one of the following options:\n  1) Find a movie. \n  2) Update a movie.\n")
try:
	choice = int(choice)
except ValueError:
		print("That's not a valid choice. Please enter '1' or '2'")

if(choice == 1):
	product_id = input("Please enter the product ID:\n")
	try:
		product_id = int(product_id)
	except:
		print("That's not a valid choice. Please enter a product ID.")
		quit()
	response = requests.get(f"{connection}products/{product_id}")
	print(f"CALLING - GET {connection}products/{product_id} \n")
	print(response.json())

if(choice == 2):
	product_input = input("Please enter the complete JSON object with the updates:\n")
	try:
		product_data = eval(product_input)
		product_id = str(product_data.get('id'))
	except:
		print("That's not a valid choice. Please enter a JSON object.")
		quit()
	response = requests.put(f"{connection}products/{product_id}", product_data)
	print(f"CALLING - PUT {connection}products/{product_id} \n")
	print(response.json())

if(choice<1 or choice>2):
	print("That's not a valid choice. Please enter '1' or '2'")
	quit()
