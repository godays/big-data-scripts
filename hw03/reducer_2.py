"""reducer 2 job"""
#!/usr/bin/env python3
import sys

cur_wrd = ''
wrd_cnt = 0
cnter_2010 = 0
cnter_2016 = 0
top = 10

for line in sys.stdin:
    line = line.strip('\n').strip("\t")
    year, word, cnt = line.split("\t", 2)
    cnt = int(cnt)
    year = int(year)
    cur_wrd = word
    wrd_cnt = cnt

    if year == 2010:
        if cnter_2010 < top:
            print(year, cur_wrd, wrd_cnt, sep="\t")
            if cnter_2010 < top:
                cnter_2010 += 1

    elif year == 2016:
        if cnter_2016 < top:
            print(year, cur_wrd, wrd_cnt, sep="\t")
            if cnter_2016 < top:
                cnter_2016 += 1
