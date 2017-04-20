# This should be a simple word counter which give us the most common word in a file
# If ran from the command line without arguments it should print out the usage:
# python most_common_word.py [source]
# When the argument provided and the source is a file
# count all words in the given file and print the most common
# ("cat", "CAT", "cat," "cat." are different words )

import sys

words = 0

if len(sys.argv) == 1:
    print('Use this command: python most_common_word.py [source]')
else:
    try:
        textfile = open(sys.argv[1], 'r')
        text_string = textfile.read().rstrip()
        text_list = text_string.split(" ")
        word_counter = {}
        for word in text_list:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        textfile.close()

        most_common_word = max(word_counter, key = word_counter.get)
        print(most_common_word, word_counter[most_common_word])

    except FileNotFoundError:
        print('No source file.')
