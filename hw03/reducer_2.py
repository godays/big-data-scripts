"""reducer 2 job"""
#!/usr/bin/env python3
import sys

CNTER_2010 = 0
CNTER_2016 = 0
TOP = 10

for line in sys.stdin:
    line = line.strip('\n').strip("\t")
    year, word, cnt = line.split("\t", 2)
    cnt = int(cnt)
    year = int(year)
    cur_wrd = word
    wrd_cnt = cnt

    if year == 2010:
        if CNTER_2010 < TOP:
            print(year, cur_wrd, wrd_cnt, sep="\t")
            if CNTER_2010 < TOP:
                CNTER_2010 += 1

    elif year == 2016:
        if CNTER_2016 < TOP:
            print(year, cur_wrd, wrd_cnt, sep="\t")
            if CNTER_2016 < TOP:
                CNTER_2016 += 1
