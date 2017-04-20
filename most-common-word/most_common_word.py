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
        file = open(sys.argv[1], 'r')
        text_string = textfile.read().rstrip()
        text_list = text_string.split("")
        word_counter = {}
