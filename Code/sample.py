import random
from analyze_word import open_file, histogram as hist

def sample(histogram):
    count_values = 0
    items_values = 0

    # the total value
    for i in histogram.values():
        count_values += i
    
    #generate random int
    dart = random.randint(0, count_values-1) #random 0 - 7

    #1 >= 0 5 >= 4 6 >= 5 7>= 6 8>=7
    for key,value in histogram.items():
        items_values += value  
        if items_values >= dart:
            return key

def test_sample(histogram, number):
    word_count = 0
    dic = {}

    for value in histogram.values():
        word_count += value

    for key,value in histogram.items():
        num = "{:.3f}".format((value/word_count)*100)
        print(f'The word {key} has {num} % probability of appearnace')
    
    number_of_words = range(number)
    for number in number_of_words:
        random_word = sample(histogram)
        if random_word in dic:
            dic[random_word] += 1
        else:
            dic[random_word] = 1
    for key,value in dic.items():
        print(f'{key} appeared {value} times.')

if __name__ == '__main__':
    dic = {'red': 1,
            'fish': 4,
            'blue': 1,
            'one': 1,
            'two': 1
            }
    text = hist(open_file('book.txt'))
    print(sample(text))
    # test_sample(text, 10000)


