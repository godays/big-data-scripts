'''mapper'''
#!/usr/bin/env python3
import sys
from random import randint

for line in sys.stdin:
    id_list = line.strip('\n').split("\t")
    for cur_id in id_list:
        if cur_id:
            rand_num = randint(1, 1000000)
            print(rand_num, cur_id, sep=",")
