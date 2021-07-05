#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:22:52 2021

@author: janakisajja
"""

import itertools
import json
import argparse


def dishes_combo():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ifile",
                        dest='original_filename',
                        action="store")
    args = parser.parse_args()
    file_name = args.original_filename
    file = open(file_name, "r")
    json_str = file.read()
    jdata = json.loads(json_str)
    target_price = jdata['Target Price']
    dishes_found = []
    for L in range(0, len(jdata['Items']) + 1):
        for subset in itertools.combinations(jdata['Items'], L):
            total = 0.00
            dishes = []
            for data in subset:
                total += float(data['Price'][1:])
                dishes.append(data['Name'])
            if target_price == total:
                dishes_found.append(','.join(dishes))
    if len(dishes_found) > 0:
        print("Below Dishes found..: \n", '\n'.join(dishes_found))
    else:
        print("No Combinations of dishes that equals the Target Price")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dishes_combo()