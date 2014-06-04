#! /usr/bin/env python

def priceParse(priceString):
    """Searches priceString for first element that isdigit and stores index as i. Then searches for the first non-digit element greater than i and stores as j. returns float(priceString[i:j]). This will throw an IndexError if priceString does not contain any digits. This is useful for exception handling."""

    #remove commas so 1,500 -> 1500
    priceStringNoComma = priceString.replace(',', '')

    i = 0

    while not priceStringNoComma[i].isdigit():
        #Here's where the IndexError will potentially be thrown
        i += 1

    j=i
    allowDecimalPoint = True

    while len(priceStringNoComma) > j and \
          (priceStringNoComma[j].isdigit() or \
           priceStringNoComma[j] == '.'):
        if priceStringNoComma[j] == '.':
            if allowDecimalPoint:
                allowDecimalPoint = False
            else:
                break
        j += 1

    return float(priceStringNoComma[i:j])

if __name__ == "__main__": 
    stringList = ["300", "1000.00", "$500", "Five hundred dollars", 
                  "$2500not a number", "$1,500.00."]

    for string in stringList:
        try:
            print priceParse(string)
        except IndexError:
            print "I accept your exception!"
            continue
