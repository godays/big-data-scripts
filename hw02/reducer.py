'''reducer'''
#!/usr/bin/env python3
import sys
from random import randint


def main():
    '''main fun'''
    index = 0
    new_line = False

    for line in sys.stdin:
        line = line.strip('\n').strip("\t")
        prefix, word_id = line.split(",")


        if index == 0:
            index = randint(1, 5)
            if new_line:
                print(f'\n{word_id}', end='')
            else:
                print(f'{word_id}', end='')
        else:
            print(f',{word_id}', end='')

        new_line = True
        index -= 1
    print()

main()