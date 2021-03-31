# '''#######################
#
# Courtesy : codebasic (youtube channel)
#
# Tutorial (youtube) : https://www.youtube.com/watch?v=rdfbcdP75KI&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg&index=1
#
# git : https://github.com/codebasics/py/tree/master/DataScience/BangloreHomePrices
#
# Disclaimer: I don't own the rights of this project/code, The code was all written as followed
#             by tutorial.
#             P.S. Some of the file/variable names has been changed for personal refrences.
#
#

from flask import Flask, request, jsonify


import util

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hi Codebasic-BHP"


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # this has to run before calling functions from 'util.py'
    app.run()
