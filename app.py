from flask import Flask, request

from functions.travel_requirement import travel_requirement
from functions.get_score import get_score
app = Flask(__name__)

@app.route('/requirement', methods=['POST'])
def general_travel_requirement():
    user_input = request.form['input']
    return travel_requirement(user_input)


@app.route('/score', methods=['GET'])
def get_country_score():
    #we can store the results somewhere so this code is supposed to run only once
    #but for demonstration purpose we calculate it everytime api calls
    return get_score()