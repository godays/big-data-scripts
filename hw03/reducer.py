'''reducer'''
#!/usr/bin/env python3
import sys

WRD_CNT = 0
CUR_WRD = ''

for line in sys.stdin:
    line = line.strip('\n').strip("\t")
    year, word, cnt = line.split("\t", 2)
    cnt = int(cnt)
    year = int(year)

    if word == CUR_WRD:
        WRD_CNT += cnt
    else:
        if CUR_WRD:
            print(year, CUR_WRD, WRD_CNT, sep="\t")
        CUR_WRD = word
        WRD_CNT = cnt

if CUR_WRD:
    print(year, CUR_WRD, WRD_CNT, sep="\t")
