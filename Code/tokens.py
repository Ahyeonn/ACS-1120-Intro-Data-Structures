punctuation = { i: True for i in '''.,?!""„'"()[]{}-;:\/@#$%‼^&*_~<>”“’'''}
#Set i : True

def tokenize(filename='book.txt'):
    words = []
    string = ''
    with open(filename) as f:
        for line in f:
            for char in line:
                if char not in punctuation:
                    string += char

        words += string.lower().split()
    words2 = []
    for i in range(0, len(words)-1, 2):
        words2.append(' '.join(words[i:i+2]))
    return words2



