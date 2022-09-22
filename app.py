import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = {'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'}


@app.route('/books', methods=['GET'])
def book_all():
    return jsonify(books)


if __name__ == "__main__":
    book_all()
