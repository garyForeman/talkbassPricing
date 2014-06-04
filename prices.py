#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last Modified: April 20, 2014
#Searches, collects, and plots price data for used basses in the talkbass 
#classified html pages
################################################################################

import matplotlib.pyplot as plt
import numpy as np
import time
import urllib
from priceParse import priceParse

NUM_PAGES = 20
NUM_BINS = 50
priceList = np.array([])

for i in xrange(1, NUM_PAGES+1):
    tbClassifiedPage="http://www.talkbass.com/forums/for-sale-bass-guitars.126/"
    if i > 1:
        tbClassifiedPage += "page-" + str(i)

    content = urllib.urlopen(tbClassifiedPage)
    lines = content.readlines()
    content.close()

    for j, line in enumerate(lines):
        if line.find("Price:") > 0:
            #html code for line containing price is 
            #<big><span style="font-weight: bold;">PRICE</span></big>
            priceString = lines[j+3].split('>')[2].split('<')[0]

            try:
                priceList = np.append(priceList, priceParse(priceString))
            except IndexError:
                continue

print len(priceList)
print np.mean(priceList)
print np.std(priceList)
print np.median(priceList)
plt.hist(priceList, bins=NUM_BINS, range=(0,10000))
plt.xticks(np.arange(11)*1000, [str(x) for x in np.arange(11)*1000], 
           rotation=45, size="xx-large")
plt.yticks(size="xx-large")
plt.xlabel("Price ($)", size="xx-large")
plt.ylabel("Number of basses", size="xx-large")
plt.title(str(len(priceList)) + " basses, " + time.strftime("%m/%d/%Y"), 
          size="xx-large")
plt.text(3000, 20, "median price: $" + str(np.median(priceList)), 
         size="xx-large")
plt.savefig("prices_" + time.strftime("%m_%d_%Y") + ".png", bbox_inches="tight",
            pad_inches=0.05)
