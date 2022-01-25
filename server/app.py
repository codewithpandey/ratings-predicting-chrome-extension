import re
from flask import Flask, request, jsonify
import brain.model as model
# The brain (main.py) file shall be imported here
# and all the function calls will be made from this file
# the brain will return the data required back here.
# the response will be sent back to the client as json.

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Predicto!"


@app.route('/getRating')
def getRating():
    review = request.args.get('review')

    # brain does the analysis and returns the star rating here
    # then return the rating in json format along with the review to the client
    # sample response below.
    brain = model.Model()
    # brain.train()
    # Absolutely love this watch! Get compliments almost every time I wear it. Dainty.
    rating = brain.predict([review])

    response = {
        "review": review,
        "rating": str(rating[0])
    }

    return jsonify(response)

    # head over to - localhost:5000/getRating?review=hello
    # and it should return a json representation of the above data.

@app.route('/train')
def train():
    brain = model.Model()
    brain.train()
    return "Predicto is an AI based star rating predictor"
    # I'll add templates and html pages in the next commit :P

@app.route('/predicto')
def about():
    return "Predicto is an AI based star rating predictor"
    # I'll add templates and html pages in the next commit :P

@app.route('/download')
def download():
    return "This route shall be used for providing downloads and installation instructions."
    # I'll add templates and html pages in the next commit :P

if __name__ == "__main__":
    app.run(debug=True)