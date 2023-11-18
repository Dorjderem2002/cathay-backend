from flask import Flask, request

from functions.travel_requirement import travel_requirement

app = Flask(__name__)

@app.route('/requirement', methods=['POST'])
def general_travel_requirement():
    user_input = request.form['input']
    return travel_requirement(user_input)