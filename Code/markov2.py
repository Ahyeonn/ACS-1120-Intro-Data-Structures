from dictogram import Dictogram
from tokens import tokenize

def markov(dicto, word_list):
    data = {}
        
    for idx, word in enumerate(word_list[:-1]):
        if word in data:
            data[word].add_count(word_list[idx+1])
        else:
            data[word] = Dictogram([word_list[idx+1]])

    if word_list[-1] not in data:
        data[word_list[-1]] = Dictogram()
    return data


def create_sentence(dicto, chain, n=3):
    next_words = dicto.sample()
    sentence = f'{next_words} '

    for count in range(n):
        markov_words = chain[next_words].sample()
        next_words = markov_words
        sentence += next_words + ' '

    return sentence

