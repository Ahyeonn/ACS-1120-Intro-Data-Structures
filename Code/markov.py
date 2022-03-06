from dictogram import Dictogram
string = 'a plan A man a plan a canal: Panama! a plan A dog, a panic in a A a plan a canal: a canal:'

words = string.split(' ')

def markov_chain(word_list):
    data = {}
    for idx in range(len(word_list)-1):
        curr_word = word_list[idx]
        next_word = word_list[idx+1]

        if curr_word in data:
            data[curr_word].add_count(next_word)
        else:
            data[curr_word] = Dictogram([next_word])

    if word_list[-1] not in data:
        data[word_list[-1]] = Dictogram()
    return data

data = markov_chain(words)

def create_sentence(data):
    print(data)
    sentence = ''
    for key in data.keys():
        sentence += data[key].sample()+ ' '
    return sentence

print(create_sentence(data))