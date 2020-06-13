'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    #To do--
    # Recursive function that, with every recursion checks the string for 'th' 
    #must account for mixed cases
    # TBC
    ## for every word
    ### find every th in the word, only if the letters 't' and 'h' are next to each other, not just rando ts and hs
    #### calculate the number of th-s in the word
    ### return that number

    #need to figure out a way to count words because of error
    #need to figure out a way to account for mixed case -- getting error
    #removed lowercase -- it was unnecessary
    
    if word[0:2] == 'th':
        count += 1
        return count_th(word[2:len(word)], count)
    elif len(word[1:len(word)]) > 1:
        count = count_th(word[1:len(word)], count)


    return count
