from flask import Flask,request
import numpy as np

import flasgger
from flasgger import Swagger 
from flasgger.utils import swag_from
app =Flask(__name__)
Swagger(app) # initialize app

@app.route("/")
def index():
	return "Testing"

@app.route("/swagui",methods =["GET"])
def get_form_value():
	#documentation code

	"""
    This is the feedback API
    Call this api passing a name, age and income
    ---
    tags:
      - Feedback API
    parameters:
      - name: name
        in: query
        type: string
        required: true
        description: Name of user
      - name: age
        in: query
        type: integer
        description: Age of user
      - name: income
        in: query
        type: integer
        description: Income of user

    responses:
      500:
        description: Something went wrong. Try again
      200:
        description: Thanks
        schema:
          id: get_endpoint
          properties:
            name:
              type: string
              description: The  name
              default: Divine
            age:
              type: integer
              description: The age name
              default: 4
            income:
              type: integer
              description: The income name
              default: 100


    """
	name =request.args.get("name")
	age =request.args.get("age")
	income =request.args.get("income")
	reply ="Hi {} Thanks for checking out our services. Based on your input your  age is {} and {} is your income".format(name,age,income)
	return reply

@app.route("/postend",methods =["POST"])
@swag_from('index.yml')
def post_test():

	mark1 = request.args.get("mark1")
	mark2 =request.args.get("mark2")
	mark3 =request.args.get("mark3")
	print(mark1)
	sum_mark =int(mark1)+int(mark2)+int(mark3)
	average = int(sum_mark)/3
	return str(average)

if __name__ == '__main__':
	app.run(debug =True)