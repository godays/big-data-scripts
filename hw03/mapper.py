'''mapper'''
#!/usr/bin/env python3
import sys

import re


for line in sys.stdin:
    crd = 'CreationDate="'
    date_ind = line.find(crd)

    if date_ind == -1:
        continue

    start = date_ind + len(crd)
    date_year = line[start:start+4]

    tags = re.findall(r'Tags=\"(([\s\S]+?))\"', line)

    if tags:
        for cur_res in tags:
            tags_new = re.findall(r'&lt;(([\s\S]+?))&gt;', cur_res[0])
            for cur_res2 in tags_new:
                if int(date_year) == 2010:
                    print(date_year, cur_res2[0], 1, sep="\t")
                elif int(date_year) == 2016:
                    print(date_year, cur_res2[0], 1, sep="\t")
