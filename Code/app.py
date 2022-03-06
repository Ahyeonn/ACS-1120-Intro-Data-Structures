from flask import Flask, render_template, request, redirect, url_for
from dictogram import Dictogram
from tokens import tokenize
from twitter import TwitterBot
from markov2 import markov, create_sentence

app = Flask(__name__)
bot = TwitterBot()

def open_file(text_file):
    file_words = []
    with open(text_file, 'r') as f:
        for line in f:
            for word in line.split(' '):
                    file_words.append(word)
        return file_words

@app.before_first_request
def before_first_request():
    tokened_word_list = tokenize()
    histogram = Dictogram(tokened_word_list)
    chain = markov(histogram, tokened_word_list)

    return create_sentence(histogram, chain)

@app.route("/")
def home():
    sentence = before_first_request()
    return render_template('index.html', sentence=sentence)

@app.route("/tweet", methods=['POST'])
def tweet():
    bot.tweet(request.form['sentence'])
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(port=5001, debug=True)
