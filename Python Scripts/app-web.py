from flask import Flask, render_template, jsonify, json, url_for
import os
app = Flask(__name__)
books=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]

def load_books():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "json", "books.json")
    return json.load(open(json_url))

books_data = load_books()


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('index.html',name=name)

@app.route("/api/books")
def allBooks():
    return jsonify(books_data)

@app.route("/api/book/id/<id>")
def book_by_id(id=1):
    id = int(id)
    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
            return jsonify(results)


@app.route("/api/book/title/<title>")
def book_by_title(title=None):
    results = []
    for book in books:
        if book['titre'] == title:
            results.append(book)
            return jsonify(results)





@app.route('/about')
def about():
    return 'The about page'


if __name__ == "__main__":
    app.run(debug=True)