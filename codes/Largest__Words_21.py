#Find Largest/Longest Word in a sentence

import string

def largest_word(s):
    l=""
    for word in s.split():
        c=word.strip(string.punctuation) #removes punctuations
        if len(c)>len(l):
            l=c
    return l

if __name__=="__main__":
    text=input("Enter Sentence:\n")
    print("Largest Word:",largest_word(text))