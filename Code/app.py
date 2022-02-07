"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from dictogram import Dictogram 

app = Flask(__name__)

histogram = None 

def open_file(text_file):
    file_words = [] # Convert it to list
    with open(text_file, 'r') as f:
        for line in f:
            for word in line.split(' '):
                    file_words.append(word)
        return file_words

@app.before_first_request
def before_first_request():
    word_list = open_file('book.txt')
    histogram = Dictogram(word_list=word_list)
    return histogram

@app.route("/")
def home():
    histogram = before_first_request()
    random_word = histogram.sample()
    return render_template('index.html', random_word = random_word)


if __name__ == "__main__":
    app.run(debug=True)
