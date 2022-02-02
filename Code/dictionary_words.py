import random

words = []

def generate_words():
    #open word_file and read
    with open('/usr/share/dict/words', 'r') as word_file:
        for word in word_file:
            #each word in word_File append it to words
            words.append(word.strip('\n'))
    #close the world_file
    word_file.close()

if __name__ == '__main__':
    num_words = int(input("How many words do you want to display?: "))
    generate_words()
    #Shuffle words in words
    random.shuffle(words)
    print(' '.join(words[:num_words]))
