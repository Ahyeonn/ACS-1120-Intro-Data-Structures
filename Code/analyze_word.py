def open_file(text_file):
    file_words = ""
    with open(text_file, 'r') as f:
        for line in f:
            file_words += line.strip('\n').lower()
        return file_words
#./(){}\--(split & words)"" replace : with emtpy space ....
def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

def frequency2(word, histogram):
    for item in histogram:
        if item[0] == word: # item[0] = 'string word'
            return item[1]
        else:
            print('checking word:', item[0]) # check words that are not == word that we are looking

def histogram(source_text):
    words = source_text.split(' ')
    word_counter = {}
    for word in words:
        # word.strip(',')
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter

def histogram2(source_text):
    words = source_text.split(' ')
    histogram_lists = []
    for word in words:
        counter = 0
        for another_word in words:
            if word == another_word: # Checking if the words are the same. if same, then increment the value by one
                counter += 1
        if [word, counter] not in histogram_lists: #Check if each word is listed in a empty list with a counter value
            histogram_lists.append([word, counter])
    return histogram_lists


if __name__ == '__main__':
    text = open_file('book.txt')
    x = histogram(text)
    print(histogram(text))
    # print(unique_words(x))
    # print(frequency('one', x))
    # print(histogram2(text))
    # print(frequency2('one', histogram2(text)))