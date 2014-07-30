#! /usr/bin/env python
"""
Author: Gary Foreman\n
Last Modified: July 30, 2014\n
Searches, collects, and plots price data for used basses in the talkbass
classifieds html pages.
"""

import matplotlib.pyplot as plt
import numpy as np
from pyquery import PyQuery as pq
import re
import time


NUM_PAGES = 20
NUM_BINS = 60
MAX_PRICE = 12000
FLOAT_REGEX = r'\d+,?\d*\.?\d*\s?[kK]?'

if __name__ == "__main__":
    PRICE_LIST = np.array([])

    for i in xrange(1, NUM_PAGES+1):
        tb_classified_page = (
            "http://www.talkbass.com/forums/for-sale-bass-guitars.126/")
        if i > 1:
            tb_classified_page += "page-" + str(i)
        
        #initialize PyQuery
        d = pq(tb_classified_page)

        price_strings = d('.pairsInline').find('span').contents()
        for price_string in price_strings:
            price_string = re.findall(FLOAT_REGEX, price_string)
            try:
                price_string = price_string[0].replace(',', '')
                if price_string[-1] == 'k' or price_string[-1] == 'K':
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
    print np.max(PRICE_LIST)
    plt.hist(PRICE_LIST, bins=NUM_BINS, range=(0, MAX_PRICE))
    plt.xticks(np.arange(13)*1000, [str(x) for x in np.arange(13)*1000],
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
