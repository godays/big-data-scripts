'''reducer'''
#!/usr/bin/env python3
import sys

wrd_cnt = 0
cur_wrd = None

for line in sys.stdin:
    line = line.strip('\n').strip("\t")
    year, word, cnt = line.split("\t", 2)
    cnt = int(cnt)
    year = int(year)

    if word == cur_wrd:
        wrd_cnt += cnt
    else:
        if cur_wrd:
            print(year, cur_wrd, wrd_cnt, sep="\t")
        cur_wrd = word
        wrd_cnt = cnt

if cur_wrd:
    print(year, cur_wrd, wrd_cnt, sep="\t")
