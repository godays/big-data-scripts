'''reducer'''
import sys
from random import randint

def read_mapper_output(files):
    '''read mapper output'''
    for line in files:
        yield line[1:].strip()

def main():
    '''main fun'''
    ids = read_mapper_output(sys.stdin)

    index = 0
    new_line = False

    for word_id in ids:
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
