## Names: Darina Kamikazi
## Student ID: 873670932
## Class: COMP 3006
## Assignment: PSET 1
## Description: Program that loops through multiple files, counts how many times each character appears in the file(s), 
##and maps each character and its respective frequency to a dictionary according to specific flag rules.

import string
#Function for loading the words
def load_words(filename): 
    """ Loads words from filename

    Args:
        filename (str): name of the file(s)

    Returns:
        lst: list of words from that file name
    """
    try:
        with open(filename) as f:
            return [i.strip() for i in f]
    except FileNotFoundError:
        print("File not found")
        return []

#Function for computing the frequencies
def add_frequencies(d,file,remove_case):
    """ Maps characters and their respective frequencies from file to dictionary d according to remove_case

    Args:
        d (dictionary): dictionary
        file(lst): list of characters from a specific file
        remove_case(bool): whether or not case sensitivity rules apply.


    Returns:
        dict: dictionary of mapped characters and frequencies
    """

    for line in file:
        for word in line:
            if word.isalpha():
                if remove_case == True:
                    word = word.lower()
                    if word not in d:
                        d[word] = 0
                    d[word] += 1
                else:
                    if word not in d:
                        d[word] = 0
                    d[word] += 1
    return d

#Main function
def main ():
    """ Main function that maps characters from files to their frequencies in a dictionary according to specific flags

    Returns:
        dict: dictionary of mapped characters and frequencies
    """
    filename = list(input("choose txt file(s): ").lower())
    file = load_words(filename)
    c = False
    z = False
    l = False
    flag = input("input flag('-c','-z','-l' or ''): ").lower()
#Setting flags
    if flag == '-c':
        c = True
    elif flag == '-z':
        z = True
    elif flag == '-l':
        l = True
        letters = input ("Choose input letters: ").lower()
    else:
        c = False
        z = False
        l = False
#Creating parameters for an empty dictionary
    d = {}
    if z == True:
        if c == True:
            for i in string.ascii_letters:
                d[i] = 0
        else:
            for i in string.ascii_lowercase:
                d[i] = 0
    else:
        d = {}
    if c == True:
        add_frequencies(d,file, remove_case= False)
    else:
        add_frequencies(d,file, remove_case= True)
    if z == True:
        if c == True:
            add_frequencies(d,file, remove_case= False)
        else:
            add_frequencies(d,file, remove_case= True)
        return d
    if l == True:
        for char in d:
            if char not in letters:
                del d[char]
    return d


main()  



    