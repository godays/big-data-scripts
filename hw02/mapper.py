'''mapper'''
import sys
from random import randint

for line in sys.stdin:
    print(randint(1, 5), line.strip(), sep="")
