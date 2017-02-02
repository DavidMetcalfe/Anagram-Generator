import re, string

''' Anagram generator that currently only 
works on whole word matches, instead of 
spreading the input string across multiple
words.

David Metcalfe, Jan 23 2017 
'''

pattern = re.compile('[\W_]+', re.UNICODE)
dictionary = set()

with open('Dictionary.txt', 'r') as f:
    for line in f:
        dictionary.add(line.strip())

anagram_input = pattern.sub('', ''.join(input("Input word(s) to find anagrams for: ")).lower())

print("")
print([word for word in dictionary if sorted(word) == sorted(anagram_input) and word not in anagram_input])