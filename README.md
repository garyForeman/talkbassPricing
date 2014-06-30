talkbassPricing
===============

Author: Gary Foreman  
email: gforema2@illinois.edu  
[talkbass thread](http://www.talkbass.com/threads/price-distribution-tb-classifieds.1074921/)

Requirements
------------
- matplotlib.pyplot
- numpy
- time
- urllib


If you wish to run this code, make sure `priceParse.py` and `prices.py` are in the
same directory because `priceParse.py` is imported by `prices.py`. Make sure both
these files have executable permissions, and run by typing `./prices.py` at the
command line. `prices.py` creates a png file containing a histogram of the prices
read from the specified talkbass classifieds section.
