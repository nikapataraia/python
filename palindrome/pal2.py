""" function takes a string and counts MINIMUM how many characters
should be appended from the right to make it palindrome with rearranging
the initial characters """ 

from xml.dom import minicompat


def minforpol(str):
    lst = []
    for chr in str:
        if chr in lst :
            lst.remove(chr)
        else :
            lst.append(chr)
    if len(str)%2 == 0 : return len(lst)
    return len(lst) - 1
