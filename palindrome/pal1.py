""" function takes a string and counts MINIMUM how many characters
should be appended from the right to make it palindrome without rearranging
the initial characters """ 
def check(str):
    return str == str[::-1]



def minforpol(word):
    if(word == ""): return 0
    ri = len(word) - 1
    for i in range(len(word)):
        if check(word[i:]):
            ri = i
            break
    return ri

 
