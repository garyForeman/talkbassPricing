#! /usr/bin/env python
"""
Author: Gary Foreman\n
Last Modified: July 29, 2014\n
Searches, collects, and plots price data for used basses in the talkbass
classifieds html pages.
"""

import matplotlib.pyplot as plt
import numpy as np
import re
import time
import urllib
#from price_parse import price_parse


NUM_PAGES = 20
NUM_BINS = 50
MAX_PRICE = 11000
FLOAT_REGEX = r'\d+,?\d*\.?\d*\s?[kK]?'

if __name__ == "__main__":
    PRICE_LIST = np.array([])

    for i in xrange(1, NUM_PAGES+1):
        tb_classified_page = (
            "http://www.talkbass.com/forums/for-sale-bass-guitars.126/")
        if i > 1:
            tb_classified_page += "page-" + str(i)

        content = urllib.urlopen(tb_classified_page)
        lines = content.readlines()
        content.close()

        for j, line in enumerate(lines):
            if line.find("Price:") > 0:
                #html code for line containing price is
                #<big><span style="font-weight: bold;">PRICE</span></big>
                price_string = (
                    re.findall(FLOAT_REGEX, 
                               lines[j+3].split('>')[2].split('<')[0]))

                try:
                    price_string = price_string[0].replace(',', '')
                    if(price_string[-1] == 'k' or 
                       price_string[-1] == 'K'):
                        price_float = float(price_string[:-1]) * 1000.
                    else:
                        price_float = float(price_string)

                    PRICE_LIST = np.append(PRICE_LIST, price_float)
                except IndexError:
                    continue

    print len(PRICE_LIST)
    print np.mean(PRICE_LIST)
    print np.std(PRICE_LIST)
    print np.median(PRICE_LIST)
    plt.hist(PRICE_LIST, bins=NUM_BINS, range=(0, MAX_PRICE))
    plt.xticks(np.arange(11)*1000, [str(x) for x in np.arange(11)*1000],
               rotation=45, size="xx-large")
    plt.yticks(size="xx-large")
    plt.xlabel("Price ($)", size="xx-large")
    plt.ylabel("Number of basses", size="xx-large")
    plt.title(str(len(PRICE_LIST)) + " basses, " + time.strftime("%m/%d/%Y"),
              size="xx-large")
    plt.text(3000, 20, "median price: $" + str(np.median(PRICE_LIST)),
             size="xx-large")
    plt.savefig("prices_" + time.strftime("%m_%d_%Y") + ".png",
                bbox_inches="tight", pad_inches=0.05)
