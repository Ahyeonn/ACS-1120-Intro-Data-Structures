"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from sample import sample, open_file, hist

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    book = hist(open_file('book.txt'))
    return sample(book)


@app.route("/")
def home():
    random_word = before_first_request()
    return render_template('index.html', random_word = random_word)


if __name__ == "__main__":
    app.run(debug=True)
