#!/usr/bin/env python3
# AnagramFinder :: Index Builder
# Copyright (c) 2018 TotallyNotHuman

# Imports
import json
import sys
import time

# Functions
def main():
    if len(sys.argv) != 2:
        print('Usage: indexbuilder.py [filename]')
    else:
        index_builder()


def index_builder():
    try:
        t_0 = time.time()
        print(f'Building index from {sys.argv[1]}')
        with open(sys.argv[1]) as file:
            words = [line.rstrip('\n') for line in file]
            wordmap = {}
            for i in range(len(words)):
                l = list(words[i])
                l.sort()
                w = ''.join(l)
                try:
                    wordmap[w].append(words[i])
                except KeyError:
                    wordmap[w] = [words[i]]
                print(f'Word {i} of {len(words) - 1} processed')
            with open('index.json', 'w+') as index:
                json.dump(wordmap, index)
        t_1 = time.time()
        elapsed = t_1 - t_0
        print(f'Index construction complete. Elapsed time: {elapsed} seconds')
    except IOError:
        print(f'{sys.argv[1]} could not be opened.')
        quit(1)


# Main
if __name__ == '__main__':
    main()